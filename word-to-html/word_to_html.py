## https://blog.aspose.com/2021/11/01/convert-word-to-html-in-python/

import os
os.chdir("D:\\Research\\here\\Book_propo")
os.getcwd()
os.listdir()
import pypandoc
output = pypandoc.convert('Book Proposal Form.docx', 'html')
with open('output_file.html', 'w', encoding='utf-8') as f:
    f.write(output)

## https://stackabuse.com/how-to-convert-docx-to-html-with-python-mammoth/

import mammoth

custom_styles = "b => i"

with open(input_filename, "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file, style_map = custom_styles)
    text = result.value
    with open('output.html', 'w') as html_file:
        html_file.write(text)

## https://stackoverflow.com/questions/47008593/how-to-convert-docx-file-to-html-using-python

import win32com.client as win32
# Open MS Word
word = win32.gencache.EnsureDispatch('Word.Application')

doc = word.Documents.Open("D:\filename.docx")
# change to a .html
txt_path = word_file.split('.')[0] + '.html'

# wdFormatFilteredHTML has value 10
# saves the doc as an html
doc.SaveAs(txt_path, 10)

doc.Close()
# noinspection PyBroadException
try:
    word.ActiveDocument()
except Exception:
    word.Quit()

## https://github.com/mwilliamson/python-mammoth [text, styles, images, etc...]
## https://blog.katastros.com/a?ID=00600-61d85bfd-6a7f-4bca-9709-0ac96ca45f0a [mammoth tutorial]


## https://blog.aspose.com/2021/11/01/convert-word-to-html-in-python/
## https://blog.aspose.cloud/2022/02/21/convert-word-to-html-using-python/ [highly efficient but has water mark]
## https://blog.aspose.com/2021/10/28/create-word-documents-using-python/

import aspose.words as aw

# Load the document from disk
doc = aw.Document("Document.docx")

# Enable export of fonts
options = aw.saving.HtmlSaveOptions()
options.export_font_resources = True
  
# Save the document as HTML
doc.save("Document.html", options)


## https://www.quora.com/What-is-the-best-way-to-convert-thousands-of-PDF-files-to-HTML-using-Python
## https://pdfminersix.readthedocs.io/en/latest/
#pip install pdfminer.six
# pip install 'pdfminer.six[image]

pdf2txt.py -o output.html -t html file.pdf
import os 
for i in range(len(pdf_list)):
    command = 'pdf2txt.py -o output'+str(i)+'.html -t html '+pdf_list[i]
    os.system(command) 

## https://pandoc.org/demos.html
## https://github.com/coolwanglu/pdf2htmlEX

## https://www.codegrepper.com/code-examples/python/python+to+convert+pdf+to+html
## https://github.com/JazzCore/python-pdfkit
    
# Shell
pip install pdfkit
sudo apt-get install wkhtmltopdf

# Python
import pdfkit 
pdfkit.from_file('input.html','shaurya.pdf') # .from_url and .from_string also exist

# Source: https://www.geeksforgeeks.org/python-convert-html-pdf/

##https://tug.org/tex4ht/doc/mn.html [final solution]
