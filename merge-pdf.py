# https://medium.com/daily-python/python-script-to-merge-pdf-files-daily-python-28-54acdf5c0473
# Purpose: Combine multiple PDFs into a single PDF
# Operation Requirements:
#   - Store PDF files to be combined into one folder
#     + Note: When downloading PDFs, opt to print the PDF and
#       then save the print output to a PDF (see Bugs below.)
#   - Name PDF files in a manner that will sort them in the
#     appropriate ascending order you want the files organized
#     + i.e. 1_file1.pdf, 2_file2.pdf
#   - Optional: name folder PDF folder what you would like the
#     name of the combined PDF to be
# Bugs:
#   - Not all PDFs are readable by PdfFileReader. This library
#     seems to have gone stale as there is no maintenance or 
#     new development activity. 

from os import listdir,mkdir,startfile
from os.path import isfile, join, exists, basename
from PyPDF2 import PdfFileMerger, PdfFileReader

# Input file path and print the pdf files in that path
path = input("Enter the folder location: ")
if isfile(path):
    print(basename(path) + ' is not a directory!')
    exit()

pdffiles = [f for f in listdir(path) if isfile(join(path, f)) and '.pdf'  in f]
print('\nList of PDF files:\n')
for file in pdffiles:
    print(file)

# Input the name of the result file
defaultName = basename(path) + '.pdf'
resultFile = (input('\nEnter the name of the result file (enter for \'' + defaultName + '\'): ') or defaultName)
if '.pdf' not in resultFile:
    resultFile += '.pdf'

# Append the pdf files
merger = PdfFileMerger()
for pdf in pdffiles:
    print('\nreading ' + pdf + '...')
    rdr = PdfFileReader(path + '\\' + pdf, 'rb')
    print('appending ' + pdf + '...')
    merger.append(rdr)

# If the output directory does not exist then create one
outputPath = path + '\\Output'
if not exists(outputPath):
    mkdir(outputPath)

# Write the merged result file to the output directory
merger.write(outputPath + '\\' + resultFile)
merger.close()

# Launch the result file
print('\n' + resultFile,'Successfully created at ', outputPath)
startfile(outputPath + '\\' + resultFile)
