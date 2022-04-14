import PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject

import AccessDatabaseLinking


def set_need_appearances_writer(writer: PdfFileWriter):
    # See 12.7.2 and 7.7.2 for more information: http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
    try:
        catalog = writer._root_object
        # get the AcroForm tree
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)
            })

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        # del writer._root_object["/AcroForm"]['NeedAppearances']
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer


def write_PHDPDF():
    myfile = PdfFileReader("C:\\TEMP\\PhD Requirements.pdf")
    first_page = myfile.getPage(0)

    writer = PdfFileWriter()
    set_need_appearances_writer(writer)
    data_dict = {
                'lblStudentName': 'David Graper',
                'lblAdvisorName:': 'Catherine Kirkland'
                }

    writer.updatePageFormFieldValues(first_page, fields=data_dict)

def write_PDF(labname, labwebsite, labmembers, rooms):
    myfile = PdfFileReader("C:\\TEMP\\PI Form 7.pdf")
    first_page = myfile.getPage(0)

    writer = PdfFileWriter()
    set_need_appearances_writer(writer)

    pipersonid = -1
    piname = ""
    pioffice = ""
    piphone = ""

    members = []

    for labmember in labmembers:
        if labmember[3] == "Principal Investigator":
            pipersonid = labmember[0]
            piname = "{0}, {1}".format(labmember[1], labmember[2])
            pioffice = AccessDatabaseLinking.get_officeroomnumber_by_personid(pipersonid)
            piphone = AccessDatabaseLinking.get_officephone_by_personid(pipersonid)
        else:
            members.append("{0}, {1}".format(labmember[0], labmember[1]))

    data_dict = {
                'txtPIName': piname,
                'txtPIOffice': pioffice,
                'txtPIOfficePhone': piphone,
                'txtLabName': labname,
                'txtLabWebsite': labwebsite
                }

    i = 1
    for labmember in labmembers:
        if i < 10:
            dictfirstname = "txtLM0{0}Fname".format(str(i))
            dictlastname = "txtLM0{0}Lname".format(str(i))
        else:
            dictfirstname = "txtLM{0}Fname".format(str(i))
            dictlastname = "txtLM{0}Lname".format(str(i))

        data_dict[dictfirstname] = labmember[1]
        data_dict[dictlastname] = labmember[2]

        i += 1

    i = 1
    for room in rooms:
        dictroomname = "txtLabRoom0{0}".format(str(i))
        data_dict[dictroomname] = room[0]
        i += 1

    writer.updatePageFormFieldValues(first_page, fields=data_dict)
    writer.addPage(first_page)

    filename = "c:\\temp\\{0}.pdf".format(piname)

    with open(filename,"wb") as new:
        writer.write(new)

