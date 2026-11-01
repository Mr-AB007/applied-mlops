"""Bundle src/app.html + vendor/*.js into the single index.html that runs on the PC.

Run after editing src/app.html:  python build.py
"""
from pathlib import Path

here = Path(__file__).parent
app = (here / "src" / "app.html").read_text(encoding="utf-8")
vendor = ""
for name in ["pdf-fonts.js", "jspdf.umd.min.js"]:
    js = (here / "vendor" / name).read_text(encoding="utf-8")
    assert "</script" not in js, name
    vendor += f"<!-- vendor/{name} -->\n<script>\n{js}\n</script>\n"
assert app.count("<!--VENDOR-->") == 1
(here / "index.html").write_text(app.replace("<!--VENDOR-->", vendor), encoding="utf-8")
print("index.html built")
