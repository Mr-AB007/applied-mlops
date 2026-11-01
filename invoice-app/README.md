# Invoice / Quotation Maker

A single offline HTML file for making and printing a GST quotation or invoice. Nothing to install.

## Install as an app (own icon, own window)
1. Put the whole `invoice-app` folder somewhere permanent, for example `D:\MITRSETU Billing`.
2. Double-click **Create Desktop Shortcut.bat**.
3. A **MITRSETU Billing** icon appears on the Desktop and in the Start Menu. It opens the bill maker in its own window, without browser tabs.
   To pin it, right-click the icon and choose **Pin to taskbar** or **Pin to Start**.

If you move the folder later, run **Create Desktop Shortcut.bat** again.

## How to use (Windows)
1. Copy `index.html` anywhere, for example to your Desktop.
2. Double-click it to open it in Chrome or Edge.
3. Type your GSTIN once in the box at the top (it is remembered). Then edit the blue boxes: customer billing info, items (HSN/SAC code, Qty, Unit, MRP, Dis %), and GST rates.
   The MITRSETU name, address and Tel./Email are fixed. The date is set to today's date each time the app opens.
4. **PRICE**, **Amount**, CGST/SGST/IGST, round-off, **Grand Total** and *amount in words* update as you type.
5. Click **Save PDF & Print** (or press Ctrl+P). The app saves the PDF, checks that the whole file was written, and opens a preview.
   Click **🖨️ Print** in the preview to print it on paper. What prints is exactly the saved PDF.

## Where PDFs are saved
The first time you print, the app asks you to choose a **Bills folder**. Make a folder such as `D:\MITRSETU Bills` or `Documents\MITRSETU Bills` and pick it.
Every PDF is saved inside it as:

```
MITRSETU Bills\07-10-2026\MS-26-27-0001.pdf
```

The date folder is created automatically if it isn't there yet. Printing the same bill again replaces its PDF.
Use **📁 Bills Folder** to change the folder. Chrome or Edge may ask "Allow this site to edit files?". Click **Allow**,
and choose "Allow on every visit" if it's offered. In other browsers the PDF goes to Downloads as `07-10-2026_MS-26-27-0001.pdf`.

## Buttons
- **+ Add Item** / **✕**: add or remove an item row.
- **📁 Bills Folder**: choose where PDFs are saved.
- **Save**: saves the bill in the browser. Your work is also saved automatically as you type.
- **New Bill**: clears the customer and items and gives the bill the next invoice number.
- **Set Invoice No.**: sets the number by hand, for example to carry on from bills made before this app.
- **Export File / Import File**: save a bill as a `.json` file and open it again later (also lets you move it to another PC).

## Formula
- Price = MRP × (1 − Dis% / 100)
- Amount = Price × Qty
- Grand Total = Taxable + CGST + SGST + IGST, rounded to the nearest rupee (GST is 0% by default because the bill is a Bill of Supply)

## Invoice number
Format: `MS/26-27/0001`, which is prefix / financial year / running number.
It goes up by one with each **New Bill** and starts again at 0001 every April, at the start of a new financial year.
The counter is stored in the browser, so always use the same browser on the same PC.

To change the business details, GSTIN or invoice prefix, edit the `BUSINESS` block near the bottom of `index.html`.

## How the PDF is made
The PDF is drawn directly with jsPDF, using real text and lines. It never depends on the window size, zoom or scrolling,
which is what used to cut bills in half. After saving, the app reads the file back and checks that it is complete
(it retries up to 3 times and warns you if the save failed). Long bills continue onto extra pages ("Page 1 of 2").

## For developers
- Edit `src/app.html`, then run `python build.py` to rebuild `index.html` (the single file that runs on the PC).
- `vendor/jspdf.umd.min.js`: jsPDF 2.5.2 (MIT).
- `vendor/pdf-fonts.js`: Liberation Sans (SIL OFL 1.1), plus the Rupee sign from DejaVu Sans, cut down to the characters a bill needs.
  Hindi or other non-Latin text is not in these fonts.
