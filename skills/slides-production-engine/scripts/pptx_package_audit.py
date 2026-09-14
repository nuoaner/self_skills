#!/usr/bin/env python3
import argparse
import posixpath
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import PurePosixPath
import xml.etree.ElementTree as ET

REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
DOC_REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
C_NS = "http://schemas.openxmlformats.org/drawingml/2006/chart"

REQUIRED_PARTS = {"[Content_Types].xml", "_rels/.rels", "ppt/presentation.xml", "ppt/_rels/presentation.xml.rels"}


def q(ns, tag):
    return "{%s}%s" % (ns, tag)


def rel_source_part(rels_name):
    p = PurePosixPath(rels_name)
    if p.name == ".rels" and str(p.parent) == "_rels":
        return ""
    if p.parent.name != "_rels" or not p.name.endswith(".rels"):
        return None
    source_dir = str(p.parent.parent)
    source_name = p.name[:-5]
    return posixpath.join(source_dir, source_name) if source_dir != "." else source_name


def resolve_target(source_part, target):
    if not target:
        return None
    if target.startswith("/"):
        return target.lstrip("/")
    base = posixpath.dirname(source_part) if source_part else ""
    return posixpath.normpath(posixpath.join(base, target))


def parse_xml(zf, name, issues):
    try:
        return ET.fromstring(zf.read(name))
    except Exception as exc:
        issues.append(("ERROR", "xml_parse", "%s: %s" % (name, exc)))
        return None


def content_type_maps(root):
    defaults = {}
    overrides = {}
    if root is None:
        return defaults, overrides
    for elem in root.findall(q(CT_NS, "Default")):
        ext = (elem.get("Extension") or "").lower()
        defaults[ext] = elem.get("ContentType") or ""
    for elem in root.findall(q(CT_NS, "Override")):
        part = (elem.get("PartName") or "").lstrip("/")
        overrides[part] = elem.get("ContentType") or ""
    return defaults, overrides


def audit(path):
    issues = []
    try:
        zf = zipfile.ZipFile(path)
    except Exception as exc:
        return [("ERROR", "zip_open", str(exc))]

    with zf:
        names = set(zf.namelist())
        for part in sorted(REQUIRED_PARTS - names):
            issues.append(("ERROR", "missing_required", part))

        ct_root = parse_xml(zf, "[Content_Types].xml", issues) if "[Content_Types].xml" in names else None
        defaults, overrides = content_type_maps(ct_root)

        xml_names = [n for n in names if n.endswith(".xml") or n.endswith(".rels")]
        for name in sorted(xml_names):
            parse_xml(zf, name, issues)

        for rels_name in sorted(n for n in names if n.endswith(".rels")):
            root = parse_xml(zf, rels_name, issues)
            if root is None:
                continue
            ids = [rel.get("Id") for rel in root.findall(q(REL_NS, "Relationship"))]
            dup_ids = [rid for rid, count in Counter(ids).items() if rid and count > 1]
            for rid in dup_ids:
                issues.append(("ERROR", "duplicate_rel_id", "%s: %s" % (rels_name, rid)))
            source = rel_source_part(rels_name)
            if source is None:
                continue
            for rel in root.findall(q(REL_NS, "Relationship")):
                if (rel.get("TargetMode") or "").lower() == "external":
                    continue
                target = resolve_target(source, rel.get("Target") or "")
                if target and target not in names:
                    issues.append(("ERROR", "broken_rel_target", "%s -> %s" % (rels_name, target)))

        for name in sorted(n for n in names if not n.endswith("/") and not n.endswith(".rels")):
            if name == "[Content_Types].xml":
                continue
            if name in overrides:
                continue
            ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
            if ext not in defaults:
                issues.append(("WARN", "missing_content_type", name))

        pres_root = parse_xml(zf, "ppt/presentation.xml", issues) if "ppt/presentation.xml" in names else None
        pres_rels = parse_xml(zf, "ppt/_rels/presentation.xml.rels", issues) if "ppt/_rels/presentation.xml.rels" in names else None
        rel_map = {}
        if pres_rels is not None:
            for rel in pres_rels.findall(q(REL_NS, "Relationship")):
                rel_map[rel.get("Id")] = rel
        if pres_root is not None:
            slide_ids = []
            sld_list = pres_root.find(q(P_NS, "sldIdLst"))
            if sld_list is not None:
                for sld in sld_list.findall(q(P_NS, "sldId")):
                    sid = sld.get("id")
                    rid = sld.get(q(DOC_REL_NS, "id"))
                    slide_ids.append(sid)
                    rel = rel_map.get(rid)
                    if rel is None:
                        issues.append(("ERROR", "slide_missing_rel", "slide id %s references %s" % (sid, rid)))
                        continue
                    target = resolve_target("ppt/presentation.xml", rel.get("Target") or "")
                    if target not in names:
                        issues.append(("ERROR", "slide_missing_part", "slide id %s -> %s" % (sid, target)))
            for sid, count in Counter(slide_ids).items():
                if sid and count > 1:
                    issues.append(("ERROR", "duplicate_slide_id", sid))

        notes_refs = defaultdict(list)
        for slide_name in sorted(n for n in names if n.startswith("ppt/slides/slide") and n.endswith(".xml")):
            rels_name = posixpath.join("ppt/slides/_rels", posixpath.basename(slide_name) + ".rels")
            if rels_name not in names:
                issues.append(("ERROR", "slide_missing_rels", slide_name))
                continue
            root = parse_xml(zf, rels_name, issues)
            if root is None:
                continue
            layout_count = 0
            for rel in root.findall(q(REL_NS, "Relationship")):
                rtype = rel.get("Type") or ""
                target = resolve_target(slide_name, rel.get("Target") or "")
                if rtype.endswith("/slideLayout"):
                    layout_count += 1
                if rtype.endswith("/notesSlide") and target:
                    notes_refs[target].append(slide_name)
            if layout_count != 1:
                issues.append(("ERROR", "slide_layout_count", "%s has %d slideLayout relationships" % (slide_name, layout_count)))

        for notes_name, slides in sorted(notes_refs.items()):
            if len(slides) > 1:
                issues.append(("ERROR", "notes_reused", "%s referenced by %s" % (notes_name, ", ".join(slides))))

        for chart_name in sorted(n for n in names if n.startswith("ppt/charts/chart") and n.endswith(".xml")):
            root = parse_xml(zf, chart_name, issues)
            if root is None:
                continue
            ax_ids = [e.get("val") for e in root.findall(".//" + q(C_NS, "axId")) if e.get("val")]
            for ax_id, count in Counter(ax_ids).items():
                if count == 1:
                    issues.append(("WARN", "chart_axis_singleton", "%s axis %s appears once" % (chart_name, ax_id)))
    return issues


def issue_key(item):
    return (item[1], item[2])


def main():
    ap = argparse.ArgumentParser(description="Audit PPTX package integrity and optionally baseline against an original deck.")
    ap.add_argument("pptx")
    ap.add_argument("--original")
    ap.add_argument("--fail-on-warn", action="store_true")
    args = ap.parse_args()

    current = audit(args.pptx)
    original = audit(args.original) if args.original else []
    original_keys = {issue_key(i) for i in original}

    new_issues = [i for i in current if issue_key(i) not in original_keys]
    inherited = [i for i in current if issue_key(i) in original_keys]

    print("PPTX package audit")
    print("File: %s" % args.pptx)
    if args.original:
        print("Baseline: %s" % args.original)
    print("New issues: %d" % len(new_issues))
    for level, code, message in new_issues:
        print("%s [%s] %s" % (level, code, message))
    if inherited:
        print("Inherited issues: %d" % len(inherited))
        for level, code, message in inherited:
            print("INHERITED %s [%s] %s" % (level, code, message))

    errors = [i for i in new_issues if i[0] == "ERROR"]
    warns = [i for i in new_issues if i[0] == "WARN"]
    if errors or (args.fail_on_warn and warns):
        sys.exit(1)


if __name__ == "__main__":
    main()
