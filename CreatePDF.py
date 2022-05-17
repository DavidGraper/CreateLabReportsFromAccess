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


def write_PHDPDF(studentname, advisorname, entrydate, dateofadvanceddegree, teaching1_2, corearea, coreexam, tool, selectcommittee,
                 qe2semesterresult, advancedtocandidacy):

    # Template file
    myfile = PdfFileReader("F:\\PhD Requirements.pdf")
    first_page = myfile.getPage(0)

    writer = PdfFileWriter()
    set_need_appearances_writer(writer)
    data_dict = {
        'txtStudentName': studentname,
        'txtAdvisorName': advisorname,
        'txtEntryDate': entrydate,
        'txtDateOfAdvancedDegree': dateofadvanceddegree,
        'txtTeaching1_2': teaching1_2,
        'txtCoreArea': corearea,
        'txtCoreExam': coreexam,
        'txtTool': tool ,
        'txtSelectCommittee': selectcommittee,
        'txtQE2SemesterResult': qe2semesterresult,
        'txtAdvanceToCandidacy': advancedtocandidacy
                }

    writer.updatePageFormFieldValues(first_page, fields=data_dict)
    writer.addPage(first_page)

    filename = "c:\\temp\\Requirements {0}.pdf".format(studentname)

    with open(filename,"wb") as new:
        writer.write(new)


def write_ConferralOfDegreePDF(studentname, studentid, degree, deptmajor, datestudybegan, admittedtocandidacy,
                               approvaldate, submitdate, satisfactorydefense, transmitted, dissertationtitle):

    # Template file
    myfile = PdfFileReader("F:\\CONFERRAL OF DEGREE.pdf")
    # myfile = PdfFileReader("F:\\Conferral Slug 1.pdf")
    first_page = myfile.getPage(0)

    filename = "c:\\temp\\Conferral Of Degree {0}.pdf".format(studentname)

    writer = PdfFileWriter()
    set_need_appearances_writer(writer)
    data_dict = {
        'txtStudentName': studentname,
        'txtStudentID': studentid,
        'txtDegree': degree,
        'txtDeptMajor': deptmajor,
        'txtDateStudyBegan': datestudybegan,
        'txtAdmittedToCandidacy': admittedtocandidacy,
        'txtApprovalDate': approvaldate,
        'txtSubmitDate': submitdate,
        'txtSatisfactoryDefense': satisfactorydefense,
        'txtTransmitted': transmitted,
        'txtDissertationTitle': dissertationtitle,
        'txtFilename': filename
                }

    writer.updatePageFormFieldValues(first_page, fields=data_dict)

    writer.addPage(first_page)

    with open(filename,"wb") as new:
        writer.write(new)


def write_DoctoralProgressReportPDF(studentname, advisorname, entrydate, corearea, teaching1, teaching2,
                                    coreexamsemesterresult, tool, selectcommittee, qe2semesterresult,
                                    advancetocandidacy, expectedgraddate):

    # Template file
    templatefile = PdfFileReader("F:\\Doctoral Student Progress Report 2022.pdf")
    first_page = templatefile.getPage(0)

    outputfilename = "c:\\temp\\{0} - Doctoral Student Progress Report.pdf".format(studentname)

    writer = PdfFileWriter()
    set_need_appearances_writer(writer)
    data_dict = {
        'txtAdvanceToCandidacy': advancetocandidacy,
        'txtAdvisor': advisorname,
        'txtCoreArea': corearea,
        'txtCoreExamSemesterResult': coreexamsemesterresult,
        'txtEntryDate': entrydate,
        'txtExpectedGraduationDate': expectedgraddate,
        'txtName': studentname,
        'txtQE2SemesterResult': qe2semesterresult,
        'txtSelectCommittee': selectcommittee,
        'txtTeaching1': teaching1,
        'txtTeaching2': teaching2,
        'txtTool': tool
                }

    writer.updatePageFormFieldValues(first_page, fields=data_dict)

    writer.addPage(first_page)

    with open(outputfilename,"wb") as new:
        writer.write(new)


def write_PDF(labname, labwebsite, labmembers, rooms, labphone):
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
                'txtLabWebsite': labwebsite,
                'txtLabPhone': labphone
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

