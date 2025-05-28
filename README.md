# merge-pdf.py

## Purpose
Combine multiple PDFs into a single PDF

## Requirements
- Python (at least version 3.10)
  - Download at https://www.python.org/downloads/
  - Wherever you choose to install Python, make sure that file path is added to your computer's "PATH" environment variable
    - This is so you can run Python and Python scripts from command line, no matter what directory your terminal is pointing at.
  - To confirm you have Python installed correctly, run `python -V` from your terminal.

## How to launch
1. Save merge-pdf.py to your computer
2. From your terminal, navigate to the folder where you saved merge-pdf.py (or just add that folder path to your PATH environment variable to skip this step in the future)
3. Type `merge-pdf.py` in your terminal
   - You'll see a prompt asking for the folder that contains the PDFs you want to merge, just provide that and it'll create a folder in that directory called "Output" where you'll find your combined PDF.

### Tips
- The default name for the created PDF is the name of the folder containing the original PDFs. Name the folder whatever you want the final PDF to be named so you can skip the naming step in the command prompt.
- Sometimes there's an encoding issue with downloaded PDFs that will break this script. To avoid it, always "Print to PDF" instead of downloading the PDF directly.

## Credit
My code is based off of ["Python script to merge PDF Files | Daily Python #28"](https://medium.com/daily-python/python-script-to-merge-pdf-files-daily-python-28-54acdf5c0473)  by [Ajinkya Sonawane](https://ajinkyasonawane.medium.com/). The
