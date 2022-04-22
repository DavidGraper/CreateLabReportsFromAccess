import pyodbc
import psycopg2
import datetime
import AccessDatabaseLinking
import CreatePDF
import ReadPDF


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # ReadPDF.readPDF("f:\\NameGender.pdf")
    # ReadPDF.readPDF("f:\\PI Form 6_RoomsRemoved.pdf")
    # ReadPDF.readPDF("f:\\PI Form 6_LabMembersShortFieldnames.pdf")
    ReadPDF.readPDF("f:\\Undergraduate Exit Survey.pdf")

    ReadPDF.readPDF("f:\\PhD Requirements.pdf")

    pi_personid = 0

    labs = AccessDatabaseLinking.get_labs()

    for lab in labs:
        labmembers = AccessDatabaseLinking.get_labmembers(lab[0])
        rooms = AccessDatabaseLinking.get_labrooms(lab[0])
        labname = lab[1]
        labwebsite = lab[2]

        # Create new PDF form for lab
        CreatePDF.write_PDF(labname, labwebsite, labmembers, rooms)


    phdreqs = AccessDatabaseLinking.get_currentactivephdstudents()

    for phdreq in phdreqs:

        # 0     ID
        # 1     PersonID
        # 2     Last
        # 3     Bdate
        # 4     First
        # 5     Gen
        # 6     Code
        # 7     Core
        # 8     Current
        # 9     Status
        # 10    Title
        # 11    strpartime
        # 12    EMPLID
        # 13    Need 24 Access LS
        # 14    Curr Semester Teaching
        # 15    BIO Ungrad Advisor
        # 16    EntryDT
        # 17    Field16
        # 18    Residency
        # 19    EntryDeg
        # 20    CurDeg
        # 21    DTAdvDeg
        # 22    Advisor
        # 23    Toefl
        # 24    Speaks
        # 25    CountryOr
        # 26    GREV
        # 27    U/Inst
        # 28    UDeg
        # 29    Statute End
        # 30    Extension to
        # 31    Filler
        # 32    mailbox
        # 33    Funding Max
        # 34    # Sem State Fund-Sprg 10
        # 35    Ethnicity
        # 36    Field36
        # 37    InitialAssmt
        # 38    Exam1 Results
        # 39    Teaching1
        # 40    Teaching2
        # 41    Exam1 Semester
        # 42    Approval of Topic
        # 43    Select Advisor
        # 44    Select Committee
        # 45    Tool
        # 46    Exam II Result
        # 47    Exam II Semester
        # 48    Advance to Candidacy
        # 49    MS/PHD Adv Lecture 1
        # 50    PHD/ Adv Lecture 2
        # 51    PHD/ Adv Lecture 3
        # 52    Sem 6 02-04
        # 53    Sem 7 04-05
        # 54    SEM 10 07-08
        # 55    Sem 8 05-06
        # 56    sEM 9 06-07
        # 57    SEM 11 08-09
        # 58    Sem 12 09-10
        # 59    Sem 13 10-11
        # 60    Sem 14 11-12
        # 61    Sem 15 12-13
        # 62    Sem 16 13-14
        # 63    Sem 17 14-15
        # 64    Sem 18 15-16
        # 65    Sem 19 16-17
        # 66    Sem 20 17-18
        # 67    Sem 21 18-19
        # 68    Sem 22 19-20
        # 69    EEB/PHD Course 1
        # 70    Sem 23 20-22
        # 71    Sem 24 21-22
        # 72    EEB/PHD Course 2
        # 73    COMMENT
        # 74    681 Seminar COmplete
        # 75    CollapsedName
        
        # 1     CurDeg
        # 2     Core
        # 3     PersonID
        # 4     Last
        # 5     First
        # 6     EntryDT
        # 7     Teaching1
        # 8     Exam1 Semester
        # 9     Teaching2
        # 10    Tool
        # 11    Exam II Semester
        # 12    Exam I Results
        # 13    Select Committee
        # 14    Exam II Result
        # 15    Advance to Candidacy
        # 16    Advisor
        # 17    CollapsedName

        # Updated 042222 when I loaded the entire table into the new database, including all fields in their original
        # order

        studentname = "{0}, {1}".format(phdreq[2], phdreq[4])
        advisorname = phdreq[22]
        entrydate = phdreq[16]
        dateofadvanceddegree = ""
        teaching1_2 = "{0} / {1}".format(phdreq[39], phdreq[40])
        corearea = phdreq[7]
        coreexam = "{0} / {1}".format(phdreq[41], phdreq[38])
        tool = phdreq[45]
        selectcommittee = phdreq[44]
        qe2semesterresult = "{0} / {1}".format(phdreq[47], phdreq[46])
        advancedtocandidacy = phdreq[48]

        CreatePDF.write_PHDPDF(studentname, advisorname, entrydate, dateofadvanceddegree, teaching1_2, corearea,
                               coreexam, tool, selectcommittee, qe2semesterresult, advancedtocandidacy)

        CreatePDF.write_ConferralOfDegreePDF(studentname, )
    # ReadPDF.readPDF("f:\\PhD Requirements.pdf")
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
