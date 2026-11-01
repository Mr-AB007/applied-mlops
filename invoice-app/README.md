# MITRSETU Billing

Offline bill maker for Windows (Chrome / Edge). Three tabs, each with its own draft and number series:

| Tab | PDF title | Numbers | GST |
|---|---|---|---|
| 🧾 GST Invoice | TAX INVOICE | `MST/26-27/0001` | GST % per item; CGST+SGST (Bihar) or IGST (other state); GST summary by rate |
| 📄 Non-GST Bill | BILL OF SUPPLY | `MS/26-27/0001` | none |
| 💬 Quotation | QUOTATION | `QT/26-27/0001` | optional (With / Without GST); has a "Valid till" date |

Numbers go up with **New Bill / New Quotation** and restart at 0001 every April (financial year).
**Make Bill from Quote** copies a quotation's customer and items into a new GST or Non-GST bill.

## Install on a PC
Copy `dist/MITRSETU-Billing-Setup.zip` to the PC, extract it, and double-click **INSTALL.bat**.
It copies the app to `%LOCALAPPDATA%\MITRSETU Billing`, adds Desktop and Start Menu icons, and opens the app.
Run it again to update the app (drafts, numbers and settings are kept). **UNINSTALL.bat** removes it; saved PDFs are kept.

## Using it
- Type your GSTIN once at the top (it is remembered).
- **💾 Save PDF** (Ctrl+S) saves the PDF straight into the Bills folder and checks that the whole file was written.
- **🖨️ Print** (Ctrl+P) opens Chrome's print window. The printed page is drawn by the same code as the PDF, so the two look the same.
  Print does not save a file; click Save PDF for that.
- **📤 Share PDF** sends the bill with WhatsApp / email (Windows share window).
- PDFs go to `<Bills folder>\GST Bills\`, `<Bills folder>\Non-GST Bills\` or `<Bills folder>\Quotations\`, each with a `DD-MM-YYYY` folder inside, named `<customer>_<number>.pdf`.
- **📂 Open Bill (PDF)**: every PDF carries the bill's data (in its Keywords field). Opening one fills everything in again,
  either to correct and reprint it (same number) or as a new GST bill, Non-GST bill or quotation (next number). `.json` files open too.
- Product names are typed in CAPITALS. Number boxes have no arrows and ignore the mouse wheel.
  The Bills folder is chosen the first time you save; change it with **📁 Bills Folder**.

## How the PDF is made
The PDF is drawn directly with jsPDF (real text and lines), so it never depends on window size, zoom or scrolling.
After writing, the file is read back and checked; the save is retried up to 3 times.
Long bills continue onto more pages ("Page 1 of 2").

## For developers
- Edit `src/app.html`, run `python build.py` to make `index.html`, then run `python build_zip.py` to make the install zip.
- Business details and number prefixes are in `BUSINESS` and `DOC_TYPES` in `src/app.html`.
- `vendor/jspdf.umd.min.js`: jsPDF 2.5.2 (MIT). `vendor/pdf-fonts.js`: Liberation Sans (SIL OFL 1.1) and the Rupee sign from DejaVu Sans,
  cut down to the characters a bill needs (no Hindi characters).
- `installer/`: Windows install / uninstall scripts.
- Logo: `python make_logo.py <logo.png>` makes `vendor/logo.png` (used in the bill header, as a faint watermark and in the toolbar)
  and `mitrsetu.ico` (app icon). Then rebuild. Turn the watermark off with `watermark: false` in `BUSINESS`.
