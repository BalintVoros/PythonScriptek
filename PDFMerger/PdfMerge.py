#PDF merge
# A program a PyPDF2 modul segítségével két pdf fájlt egyesít egy fájlba.

import PyPDF2
import os
import sys

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
merger.write("merged.pdf")
