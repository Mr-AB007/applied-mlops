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
assert app.count("<!--VENDOR-->") == 1 and app.count("<!--BRAND-->") == 1
logo = here / "vendor" / "logo.png"             # made by make_logo.py; optional
brand = "null"
if logo.exists():
    import base64
    brand = "'data:image/png;base64," + base64.b64encode(logo.read_bytes()).decode() + "'"
app = app.replace("<!--BRAND-->", f"<script>window.BRAND_LOGO = {brand};</script>")
(here / "index.html").write_text(app.replace("<!--VENDOR-->", vendor), encoding="utf-8")
print("index.html built")
