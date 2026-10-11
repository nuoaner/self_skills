# Font preflight

Font rendering varies between PowerPoint, LibreOffice, and the QA environment.

Use font preflight to identify explicit typefaces in the package and whether the current environment appears to substitute them. A substitution is a warning, not an automatic failure.

For substituted fonts:

- keep extra horizontal and vertical fit slack;
- avoid text boxes that fit only at the exact measured boundary;
- visually inspect wrapped titles, dense tables, and labels first;
- preserve required brand fonts unless the user asks for a fallback;
- record a safe fallback only when the target delivery environment is known.
