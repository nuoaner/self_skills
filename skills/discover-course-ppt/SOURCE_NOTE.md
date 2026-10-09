# Source note

This repository entry records the V3 control-plane and engineering-QA upgrade for `discover-course-ppt`.

The complete installable skill package also contains the existing teaching references, brand PNG assets, teacher template PPTX, reference deck PPTX, metadata helper, course validator, and local copies of the engineering audit scripts. Those binary/course assets are intentionally kept in the packaged `skill.zip` delivered with this upgrade rather than re-encoded through the GitHub connector.

V3 adds:

- three independent delivery gates: teaching semantics, PPTX package integrity, rendered appearance;
- template inventory before layout mapping;
- content-placeholder audit;
- font substitution preflight;
- regression-aware package validation using an original template baseline;
- repeated structural validation after XML/template changes.

The reusable, source-controlled engineering implementation lives in `skills/slides-production-engine/`.
