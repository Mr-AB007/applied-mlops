"""Build the install package: dist/MITRSETU-Billing-Setup.zip

  python build.py       # bundle src/ + vendor/ into index.html
  python build_zip.py   # make the zip to copy to any Windows PC
"""
import zipfile
from pathlib import Path

here = Path(__file__).parent
top = "MITRSETU Billing Setup"
files = {f"{top}/{n}": here / "installer" / n for n in
         ["INSTALL.bat", "UNINSTALL.bat", "install.ps1", "uninstall.ps1", "README.txt"]}
files[f"{top}/app/index.html"] = here / "index.html"
files[f"{top}/app/mitrsetu.ico"] = here / "mitrsetu.ico"

out = here / "dist" / "MITRSETU-Billing-Setup.zip"
out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for arc, src in files.items():
        z.write(src, arc)
print(out)
