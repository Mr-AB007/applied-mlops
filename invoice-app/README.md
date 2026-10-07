# Invoice / Quotation Maker

A single offline HTML file for making and printing a GST quotation or invoice. Nothing to install.

## How to use (Windows)
1. Copy `index.html` anywhere, for example to your Desktop.
2. Double-click it to open it in Chrome or Edge.
3. Edit the blue boxes: shop details, customer billing info, items (Qty, Unit, MRP, Dis %), and GST rates.
4. **PRICE**, **Amount**, CGST/SGST/IGST, round-off, **Grand Total** and *amount in words* update as you type.
5. Click **Print / Save as PDF**. To print on paper, pick your printer. For a PDF, pick "Save as PDF".

## Buttons
- **+ Add Item** / **✕**: add or remove an item row.
- **Save**: saves the bill in the browser. Your work is also saved automatically as you type.
- **New Bill**: clears the customer and items but keeps your shop details.
- **Export File / Import File**: save a bill as a `.json` file and open it again later (also lets you move it to another PC).

## Formula
- Price = MRP × (1 − Dis% / 100)
- Amount = Price × Qty
- Grand Total = Taxable + CGST + SGST + IGST, rounded to the nearest rupee

To change the starting shop details, edit the `DEFAULTS` block near the bottom of `index.html`.
