"""Turn the business logo into the app icon and the image used on bills.

  python make_logo.py path/to/logo.png      (then: python build.py && python build_zip.py)

Makes:
  vendor/logo.png  - round logo with a transparent outside (bill header, watermark, toolbar)
  mitrsetu.ico     - Windows app icon (16..256 px)
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

here = Path(__file__).parent
src = Image.open(sys.argv[1]).convert("RGBA")

# square crop around the centre, then keep only the round badge (removes black/coloured corners)
side = min(src.size)
src = ImageOps.fit(src, (side, side), Image.LANCZOS)
big = 1024
im = src.resize((big, big), Image.LANCZOS)
mask = Image.new("L", (big * 4, big * 4), 0)
inset = int(big * 4 * 0.012)                      # trim the dark edge of the badge
ImageDraw.Draw(mask).ellipse((inset, inset, big * 4 - inset, big * 4 - inset), fill=255)
mask = mask.resize((big, big), Image.LANCZOS)
alpha = Image.composite(im.getchannel("A"), Image.new("L", (big, big), 0), mask)
im.putalpha(alpha)

im.resize((560, 560), Image.LANCZOS).save(here / "vendor" / "logo.png", optimize=True)
im.save(here / "mitrsetu.ico", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print("vendor/logo.png and mitrsetu.ico updated")
