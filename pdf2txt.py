""" Author - Aryamaan Parikh

Python 2.7
Look at pdfTextExtractor for documentation on this
"""
import subprocess
from pypdfocr.pypdfocr import PyPDFOCR
import PyPDF2
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def validator(path):
    pdfFileObj = open(path, 'rb')  # 'rb' for read binary mode
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(2)
    t = pageObj.extractText()
    if t:
        return True
    else:
        return False


def scan2vec(path):  # This code extracts text from a vectorized pdf
    converter = PyPDFOCR()
    converter.go([path])
    print("Converted")
    return path[:-4] + "_ocr.pdf"

def vecTextExtractor(vecPath):  # This converts Scanned docs to vectorized docs and then use pdf2txt to extract data from them
    pdfFileObj = open(vecPath, 'rb')  # 'rb' for read binary mode
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    s = pdfReader.getNumPages()
    text_list = [""]
    for i in range(1, s):
        pageObj = pdfReader.getPage(i)
        t = pageObj.extractText()
        text_list.append(t)
    text_list = text_list[1:]
    ## so now you have page numbers as well, as index of list
    return text_list

# converts pdf, returns its text content as a string

def convertWithPdfMiner(fname):
        pages_text = []
        rsrcmgr = PDFResourceManager()
        sio = StringIO()
        codec = 'utf-8'  # ISO-8859-1 is good for foreign languages
        laparams = LAParams()
        device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        pdf = open(fname, "rb")
        count = 0

        for page in PDFPage.get_pages(pdf):
            # Get (and store) the "cursor" position of stream before reading from PDF
            # On the first page, this will be zero
            read_position = sio.tell()
            interpreter.process_page(page)
            sio.seek(read_position, 0)
            page_text = sio.read()
            pages_text.append(page_text)
        return pages_text



