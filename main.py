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

    pi_personid = 0

    labs = AccessDatabaseLinking.get_labs()

    for lab in labs:
        labmembers = AccessDatabaseLinking.get_labmembers(lab[0])
        rooms = AccessDatabaseLinking.get_labrooms(lab[0])
        labname = lab[1]
        labwebsite = lab[2]

        # Create new PDF form for lab
        CreatePDF.write_PDF(labname, labwebsite, labmembers, rooms)

    CreatePDF.write_PHDPDF()

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
