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
- **Save PDF & Print** saves the PDF, checks that the whole file was written, then shows a preview with **Print** and **Share** (WhatsApp / email).
- PDFs go to `<Bills folder>\DD-MM-YYYY\<number>.pdf`, and quotations to `<Bills folder>\Quotations\DD-MM-YYYY\<number>.pdf`.
  The Bills folder is chosen the first time you save; change it with **📁 Bills Folder**.
- **Export / Import File** saves a bill as `.json` and opens it again later.

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
