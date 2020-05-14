# Information extraction from PDF
- In this repo we will go through multiple techniques to exxtract various types of inforamtion from a PDF document.

As Pdf can be of multiple types. we can separate the PDF files into two classes:
- **Text-based files:** containing text that can be copied and pasted
- **Image-based files:** contained images such as scanned documents

Here we will use multiple python libraries to handle both the types:
- Image-based pdf files
	- 1.1. OCRMYPDF
- Text-based pdf files
	- 2.1. PyPDF2
	- 2.2. PDF2IMG
	- 2.4. Camelot
	- 2.5. Camelot mixed with YOLOV3

### OCRMYPDF
Ocrmypdf is a python package which allow to turn an image-based pdf into a text-based one, where text can be selected, copied and pasted.
In order to install ocrmypdf you can use apt in Linux using the command line:
``sudi apt-get install ocrmypdf``

Once the package is installed, you can ocrise your pdf file by running the following command line:
``ocrmypdf input_file.pdf output_file.pdf``


### PyPDF2
PyPDF2 is a python tool which enables us to parse basic information about the pdf file such the author the title…etc. It also allows the get the text of a given page along with splitting pages and opening encrypted files under the assumption of having the password.
PyPDF2 can be installed used pip by running the following command line:
``pip install PyPDF2``

### PDF2IMG
PDF2IMG is a python library that allows turning pdf pages into images that can be processed, for instance, by computer vision algorithms.
PDF2IMG can be installed using pip by running the following command line:
``pip install pdf2image``


### Camelot
Camelot is a python library specialized in parsing tables of pdfs pages. It can be installed using pip by running the following command line:
``pip install camelot-py[cv]``

for better detection of tables using YOLOv3: https://github.com/ismail-mebsout/Parsing-PDFs-using-YOLOV3

## References:
- https://towardsdatascience.com/pdfs-parsing-using-yolov3-987c85c639dc

