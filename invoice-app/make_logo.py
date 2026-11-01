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
# Small icon sizes: the handshake + arches only, enlarged, so they stay recognisable at 16-48 px.
emblem = im.crop((int(big * 0.13), int(big * 0.08), int(big * 0.87), int(big * 0.55)))
small = Image.new("RGBA", (big, big), (0, 0, 0, 0))
face = im.getpixel((big // 2, int(big * 0.07)))[:3] + (255,)          # the badge's own background colour
ImageDraw.Draw(small).ellipse((8, 8, big - 8, big - 8), fill=face, outline=(200, 205, 215, 255), width=14)
ew = int(big * 0.84); eh = int(emblem.height * ew / emblem.width)
small.alpha_composite(emblem.resize((ew, eh), Image.LANCZOS), ((big - ew) // 2, (big - eh) // 2 + int(big * 0.03)))

small.putalpha(Image.composite(small.getchannel('A'), Image.new('L', (big, big), 0), mask))   # keep it round
sizes = [16, 24, 32, 48, 64, 128, 256]
frames = [(small if s <= 48 else im).resize((s, s), Image.LANCZOS) for s in sizes]
frames[-1].save(here / "mitrsetu.ico", sizes=[(s, s) for s in sizes], append_images=frames[:-1])
print("vendor/logo.png and mitrsetu.ico updated")
