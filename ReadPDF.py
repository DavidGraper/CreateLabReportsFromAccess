import PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject

import AccessDatabaseLinking

def readPDF(filename):

    # f:\\NameGender.pdf
    pdfObj = open(filename, 'rb')

    reader = PyPDF2.PdfFileReader(
        pdfObj,
        strict=True,
        warndest=None,
        overwriteWarnings=True
        )

    print(reader.getFormTextFields())

    # Print values from PDF file
    # print("Textbox value = {0}".format(reader.getFields()['txtName']['/V']))
    # print("Textbox value = {0}".format(reader.getFields()['txtPIName']['/V']))

    # if reader.getFields()['Option Button 1']['/V'] == '/1':
    #     print("Gender = Male")
    # else:
    #     print("Gender = Female")
    #
    # print("Checkbox 1 value = {0}".format(reader.getFields()['chk1']['/V']))
    # print("Checkbox 2 value = {0}".format(reader.getFields()['chk2']['/V']))
    #
    # print("Gender = ")

    print(reader.getFields())
