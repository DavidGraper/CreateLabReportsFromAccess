import pyodbc
import psycopg2
import datetime


# Routines specific to the original Access database
# (explicit translation tables, etc.)

def setup_Building_Code_Translations():
    returndict = {}

    returndict["BI B12-13"] = 27
    returndict["BI B20"] = 42
    returndict["BI B23"] = 47
    returndict["BI B23 Orokos"] = 47
    returndict["BI B37"] = 61
    returndict["BI 108"] = 100
    returndict["BI 109"] = 101
    returndict["BI 110"] = 102
    returndict["BI 111"] = 103
    returndict["BI 112"] = 104
    returndict["BI 113"] = 105
    returndict["BI 119"] = 116
    returndict["BI 119E"] = 116
    returndict["119A"] = 117
    returndict["BI 119A"] = 117
    returndict["BI 119D"] = 120
    returndict["119E"] = 121
    returndict["119E"] = 121
    returndict["119E"] = 121
    returndict["BI 126"] = 126
    returndict["BI 127"] = 127
    returndict["BI 143"] = 141
    returndict["BI 147"] = 147
    returndict["BI 209"] = 168
    returndict["BI 211"] = 170
    returndict["BI 212"] = 171
    returndict["Bio 212"] = 171
    returndict["BI 213"] = 173
    returndict["BI 214"] = 174
    returndict["BI  215"] = 175
    returndict["BI 215"] = 175
    returndict["BI 216"] = 176
    returndict["BI 217"] = 177
    returndict["Bio 217"] = 177
    returndict["BI 221 C"] = 180
    returndict["BI 221A"] = 180
    returndict["BI 221C"] = 180
    returndict["BI 222"] = 181
    returndict["Bi 222A"] = 182
    returndict["Bio 222B"] = 183
    returndict["BI 225"] = 186
    returndict["Biology 227"] = 187
    returndict["BI 232"] = 192
    returndict["BI 241"] = 202
    returndict["Bi 244"] = 208
    returndict["Bi 245"] = 209
    returndict["BI 251"] = 216
    returndict["BI 251"] = 216
    returndict["BI 253"] = 218
    returndict["BI 253A"] = 219
    returndict["BI 253B Robinson"] = 220
    returndict["Bio 253 B"] = 220
    returndict["Robinson BI 253B"] = 220
    returndict["BI 254"] = 222
    returndict["Bi 309"] = 230
    returndict["BI 310"] = 232
    returndict["BI 323"] = 246
    returndict["BI 324"] = 247
    returndict["BI 326"] = 249
    returndict["BI 327"] = 251
    returndict["BI 329"] = 255
    returndict["Bi 338"] = 265
    returndict["BI 338 Scimemi"] = 265
    returndict["Bio 338"] = 265
    returndict["BI 338C"] = 268
    returndict["Bi 342"] = 277
    returndict["BI 342 Turner"] = 277
    returndict["Bio 342"] = 277
    returndict["Turner, BI 342"] = 277
    returndict["BI 343"] = 280
    returndict["BI 344"] = 281
    returndict["BI 344 Kleppel"] = 281
    returndict["Bi 345"] = 283
    returndict["Bi 345 Valm"] = 283
    returndict["Bio 345"] = 283
    returndict["BI 349"] = 289
    returndict["BI 353"] = 294
    returndict["BI 353 Forni"] = 294
    returndict["BI 355"] = 298
    returndict["LS 1003K Cunningham"] = 403
    returndict["LS 1003M"] = 403
    returndict["LS 1003N"] = 403
    returndict["LS 1003P"] = 403
    returndict["LS 1033"] = 432
    returndict["LS 1033 Chen"] = 432
    returndict["LS 1037"] = 436
    returndict["LS 1038"] = 437
    returndict["LS 1039"] = 438
    returndict["LS 1042"] = 441
    returndict["LS 1044"] = 443
    returndict["LS 1044 Lnenicka"] = 443
    returndict["LS 1051"] = 450
    returndict["LS 1051 Szaro"] = 450
    returndict["LS 1059"] = 458
    returndict["LS 1060"] = 459
    returndict["LS 1074"] = 470
    returndict["LS 1074 Agris"] = 470
    returndict["LS 1074/1079"] = 470
    returndict["LS 1074/1079 Agris"] = 470
    returndict["LS 1076"] = 472
    returndict["LS 1076"] = 472
    returndict["Larsen LSRB 1086"] = 482
    returndict["LS 1086"] = 482
    returndict["LS1086"] = 482
    returndict["LS 1087A"] = 483
    returndict["LS 1088/LS 1003 Larsen"] = 484
    returndict["LS 1088/LS 1003D"] = 484
    returndict["LS1088"] = 484
    returndict["LS 1103"] = 499
    returndict["LS 1105"] = 501
    returndict["LS 1108"] = 504
    returndict["LS 1116"] = 512
    returndict["LS 1124"] = 520
    returndict["LS 1125"] = 521
    returndict["LS 1126"] = 522
    returndict["LS 1147"] = 540
    returndict["LS 2015A"] = 579
    returndict["LS 2020A"] = 584
    returndict["LS 2027"] = 589
    returndict["LS 2027A"] = 589
    returndict["LS 2027A Fuchs"] = 589
    returndict["LS 2029"] = 590
    returndict["LS 2029 Rangan"] = 590
    returndict["LSRB 2029"] = 590
    returndict["LS 2031 Rangan"] = 592
    returndict["LS 2031A"] = 592
    returndict["LS 2031A Rangan"] = 592
    returndict["LS 2033D"] = 593
    returndict["LS 2033F"] = 593
    returndict["LS 2033I"] = 593
    returndict["LS 2033J"] = 593
    returndict["LSRB 2033D"] = 593
    returndict["LS 2051"] = 594
    returndict["LS 2054"] = 597
    returndict["LS 2054A"] = 597
    returndict["LS 2059"] = 602
    returndict["LS 2060"] = 603
    returndict["LS 2061"] = 604
    returndict["LS 2062"] = 605
    returndict["LS 2062 Osuna"] = 605
    returndict[" LS 2065/2059"] = 608
    returndict[" LS 2065/2059 Belfort"] = 608
    returndict["LS 2065"] = 608
    returndict["LS 2065/2059"] = 608
    returndict["LS 2065/2059 Belfort"] = 608
    returndict["LS 2067"] = 610
    returndict["LS 2072"] = 615
    returndict["LS 2072 Pager"] = 615
    returndict["LSRB 2072"] = 615
    returndict["LS 2075"] = 618
    returndict["LS 2077"] = 620
    returndict["LS 2078"] = 621
    returndict["LS 2082"] = 625
    returndict["LS 2098"] = 641

    return returndict


# Create semester code table in new database on first use
def createsemestertable():
    sqlstatements = [
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2000,'Spring','1/1/2000','6/1/2000');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2000,'Fall','9/1/2000','12/31/2000');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2001,'Spring','1/1/2001','6/1/2001');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2001,'Fall','9/1/2001','12/31/2001');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2002,'Spring','1/1/2002','6/1/2002');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2002,'Fall','9/1/2002','12/31/2002');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2003,'Spring','1/1/2003','6/1/2003');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2003,'Fall','9/1/2003','12/31/2003');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2004,'Spring','1/1/2004','6/1/2004');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2004,'Fall','9/1/2004','12/31/2004');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2005,'Spring','1/1/2005','6/1/2005');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2005,'Fall','9/1/2005','12/31/2005');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2006,'Spring','1/1/2006','6/1/2006');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2006,'Fall','9/1/2006','12/31/2006');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2007,'Spring','1/1/2007','6/1/2007');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2007,'Fall','9/1/2007','12/31/2007');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2008,'Spring','1/1/2008','6/1/2008');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2008,'Fall','9/1/2008','12/31/2008');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2009,'Spring','1/1/2009','6/1/2009');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2009,'Fall','9/1/2009','12/31/2009');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2010,'Spring','1/1/2010','6/1/2010');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2010,'Fall','9/1/2010','12/31/2010');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2011,'Spring','1/1/2011','6/1/2011');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2011,'Fall','9/1/2011','12/31/2011');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2012,'Spring','1/1/2012','6/1/2012');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2012,'Fall','9/1/2012','12/31/2012');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2013,'Spring','1/1/2013','6/1/2013');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2013,'Fall','9/1/2013','12/31/2013');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2014,'Spring','1/1/2014','6/1/2014');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2014,'Fall','9/1/2014','12/31/2014');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2015,'Spring','1/1/2015','6/1/2015');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2015,'Fall','9/1/2015','12/31/2015');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2016,'Spring','1/1/2016','6/1/2016');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2016,'Fall','9/1/2016','12/31/2016');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2017,'Spring','1/1/2017','6/1/2017');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2017,'Fall','9/1/2017','12/31/2017');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2018,'Spring','1/1/2018','6/1/2018');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2018,'Fall','9/1/2018','12/31/2018');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2019,'Spring','1/1/2019','6/1/2019');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2019,'Fall','9/1/2019','12/31/2019');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2020,'Spring','1/1/2020','6/1/2020');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2020,'Fall','9/1/2020','12/31/2020');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2021,'Spring','1/1/2021','6/1/2021');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2021,'Fall','9/1/2021','12/31/2021');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2022,'Spring','1/1/2022','6/1/2022');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2022,'Fall','9/1/2022','12/31/2022');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2023,'Spring','1/1/2023','6/1/2023');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2023,'Fall','9/1/2023','12/31/2023');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2024,'Spring','1/1/2024','6/1/2024');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2024,'Fall','9/1/2024','12/31/2024');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2025,'Spring','1/1/2025','6/1/2025');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2025,'Fall','9/1/2025','12/31/2025');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2026,'Spring','1/1/2026','6/1/2026');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2026,'Fall','9/1/2026','12/31/2026');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2027,'Spring','1/1/2027','6/1/2027');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2027,'Fall','9/1/2027','12/31/2027');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2028,'Spring','1/1/2028','6/1/2028');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2028,'Fall','9/1/2028','12/31/2028');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2029,'Spring','1/1/2029','6/1/2029');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2029,'Fall','9/1/2029','12/31/2029');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2030,'Spring','1/1/2030','6/1/2030');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2030,'Fall','9/1/2030','12/31/2030');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2031,'Spring','1/1/2031','6/1/2031');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2031,'Fall','9/1/2031','12/31/2031');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2032,'Spring','1/1/2032','6/1/2032');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2032,'Fall','9/1/2032','12/31/2032');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2033,'Spring','1/1/2033','6/1/2033');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2033,'Fall','9/1/2033','12/31/2033');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2034,'Spring','1/1/2034','6/1/2034');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2034,'Fall','9/1/2034','12/31/2034');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2035,'Spring','1/1/2035','6/1/2035');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2035,'Fall','9/1/2035','12/31/2035');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2036,'Spring','1/1/2036','6/1/2036');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2036,'Fall','9/1/2036','12/31/2036');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2037,'Spring','1/1/2037','6/1/2037');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2037,'Fall','9/1/2037','12/31/2037');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2038,'Spring','1/1/2038','6/1/2038');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2038,'Fall','9/1/2038','12/31/2038');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2039,'Spring','1/1/2039','6/1/2039');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2039,'Fall','9/1/2039','12/31/2039');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2040,'Spring','1/1/2040','6/1/2040');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2040,'Fall','9/1/2040','12/31/2040');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2041,'Spring','1/1/2041','6/1/2041');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2041,'Fall','9/1/2041','12/31/2041');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2042,'Spring','1/1/2042','6/1/2042');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2042,'Fall','9/1/2042','12/31/2042');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2043,'Spring','1/1/2043','6/1/2043');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2043,'Fall','9/1/2043','12/31/2043');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2044,'Spring','1/1/2044','6/1/2044');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2044,'Fall','9/1/2044','12/31/2044');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2045,'Spring','1/1/2045','6/1/2045');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2045,'Fall','9/1/2045','12/31/2045');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2046,'Spring','1/1/2046','6/1/2046');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2046,'Fall','9/1/2046','12/31/2046');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2047,'Spring','1/1/2047','6/1/2047');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2047,'Fall','9/1/2047','12/31/2047');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2048,'Spring','1/1/2048','6/1/2048');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2048,'Fall','9/1/2048','12/31/2048');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2049,'Spring','1/1/2049','6/1/2049');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2049,'Fall','9/1/2049','12/31/2049');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2050,'Spring','1/1/2050','6/1/2050');",
        "insert into code_semesters (year, semester, firstdate, lastdate) values ( 2050,'Fall','9/1/2050','12/31/2050');"]

    # Clear code_semesters table
    clearaccesstable("code_semesters")

    return sqlstatements


# Add keypad codes (11/17/21)
def addkeypadcodes():
    sqlstatements = [
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (12, 20, 1,88,'426884*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (11, 25, 1,88,'426884*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (12, 20, 1,86,'869150*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (12, 25, 1,86,'869150*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (13, 20, 1,82,'237216*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (13, 25, 1,82,'237216*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (135, 20, 1,67,'407114*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (135, 25, 1,67,'407114*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (154, 20, 1,29,'466190*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (154, 25, 1,29,'466190*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (158, 20, 1,68,'538498*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (158, 25, 1,68,'538498*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (160, 20, 1,44,'541556*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (160, 24, 1,44,'541556*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (160, 25, 1,44,'541556*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (164, 218, 1,4,'212121*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (164, 220, 1,5,'212121*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (18, 20, 1,63,'612836*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (18, 25, 1,63,'612836*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (197, 20, 1,84,'441545*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (197, 25, 1,84,'441545*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (198, 20, 1,25,'300596*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (198, 25, 1,25,'300596*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (201, 202, 1,4,'45358*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (209, 20, 1,51,'602146*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (209, 25, 1,51,'602146*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (211, 20, 1,62,'995218*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (211, 25, 1,62,'995218*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (215, 20, 1,66,'989436*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (215, 25, 1,66,'989436*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (216, 20, 1,26,'433692*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (216, 25, 1,26,'433692*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (218, 20, 1,32,'150363*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (218, 20, 1,55,'505032*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (218, 25, 1,32,'150363*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (218, 25, 1,55,'505032*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (225, 20, 1,43,'620885*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (225, 25, 1,43,'620885*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (227, 220, 1,9,'479438*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (24, 20, 1,42,'917225*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (24, 25, 1,42,'917225*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (240, 20, 1,33,'132700*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (240, 25, 1,33,'132700*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (242, 20, 1,41,'109959*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (242, 25, 1,41,'109959*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (243, 20, 1,70,'600338*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (243, 25, 1,70,'600338*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (247, 216, 1,4,'45095*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (259, 20, 1,56,'362961*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (259, 25, 1,56,'362961*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (261, 20, 1,46,'319974*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (261, 25, 1,46,'319974*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (261, 265, 1,4,'1967*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (283, 20, 1,34,'805156*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (283, 25, 1,34,'805156*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (284, 20, 1,30,'975383*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (284, 25, 1,30,'975383*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (291, 20, 1,58,'183303*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (291, 25, 1,58,'183303*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (299, 20, 1,53,'852303*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (299, 25, 1,53,'852303*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (3, 20, 1,80,'357591*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (3, 25, 1,80,'357591*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (30, 20, 1,24,'315054*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (30, 25, 1,24,'315054*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (300, 218, 1,5,'960165*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (300, 220, 1,4,'081486*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (319, 20, 1,71,'830128*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (319, 25, 1,71,'830128*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (333, 20, 1,91,'907268*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (333, 25, 1,91,'907268*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (334, 20, 1,81,'275581*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (334, 25, 1,81,'275581*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (335, 20, 1,77,'974374*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (335, 216, 1,5,'99685*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (335, 25, 1,77,'974374*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (336, 20, 1,64,'345074*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (336, 25, 1,64,'345074*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (338, 20, 1,90,'400082*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (338, 25, 1,90,'400082*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (339, 20, 1,83,'483271*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (339, 25, 1,83,'483271*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (340, 20, 1,60,'605564*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (340, 25, 1,60,'605564*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (341, 20, 1,75,'763190*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (341, 25, 1,75,'763190*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (342, 20, 1,61,'894028*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (342, 25, 1,61,'894028*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (343, 20, 1,76,'509121*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (343, 25, 1,76,'509121*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (344, 20, 1,78,'102805*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (344, 25, 1,78,'102805*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (345, 20, 1,48,'220383*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (345, 25, 1,48,'220383*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (346, 20, 1,72,'783814*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (346, 25, 1,72,'783814*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (347, 20, 1,47,'681924*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (347, 25, 1,47,'681924*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (348, 20, 1,27,'554801*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (348, 25, 1,27,'554801*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (349, 20, 1,85,'554354*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (349, 25, 1,85,'554354*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (350, 20, 1,69,'800045*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (350, 25, 1,69,'800045*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (351, 20, 1,37,'756141*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (351, 25, 1,37,'756141*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (352, 20, 1,87,'378502*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (352, 25, 1,87,'378502*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (36, 20, 1,54,'392687*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (36, 25, 1,54,'392687*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (37, 20, 1,74,'521660*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (37, 25, 1,74,'521660*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (39, 20, 1,65,'741777*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (39, 25, 1,65,'741777*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (43, 20, 1,31,'264229*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (43, 25, 1,31,'264229*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (46, 20, 1,44,'541556*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (46, 24, 1,44,'541556*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (46, 25, 1,44,'541556*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (58, 20, 1,39,'859282*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (58, 25, 1,39,'859282*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (6, 20, 1,89,'752965*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (6, 25, 1,89,'752965*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (60, 20, 1,73,'845248*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (60, 25, 1,73,'845248*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (63, 20, 1,0,'333769*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (63, 25, 1,0,'333769*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (80, 20, 1,35,'604374*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (80, 25, 1,35,'604374*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (81, 20, 1,44,'541556*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (81, 24, 1,44,'541556*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (81, 25, 1,44,'541556*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (89, 20, 1,20,'666008*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (89, 25, 1,20,'666008*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (90, 20, 1,21,'975234*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (90, 25, 1,21,'975234*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (94, 20, 1,49,'321082*');",
        "insert into data_person_keypadcodes (personid, roomid, keypadcodetypeid, keypadusercode, keypadcodevalue) values (94, 25, 1,49,'321082*');"
    ]

    return sqlstatements


def addsemestercodes():
    sqlstatements = ["INSERT INTO CODE_SEMESTERS VALUES (1,2000, 'Winter','12/15/2000','01/15/2000',2001);",
                     "INSERT INTO CODE_SEMESTERS VALUES (2,2000, 'Spring','01/15/2000','05/15/2000',2003);",
                     "INSERT INTO CODE_SEMESTERS VALUES (3,2000, 'Summer','05/15/2000','08/15/2000',2006);",
                     "INSERT INTO CODE_SEMESTERS VALUES (4,2000, 'Fall','08/15/2000','12/15/2000',2009);",
                     "INSERT INTO CODE_SEMESTERS VALUES (5,2001, 'Winter','12/15/2001','01/15/2001',2011);",
                     "INSERT INTO CODE_SEMESTERS VALUES (6,2001, 'Spring','01/15/2001','05/15/2001',2013);",
                     "INSERT INTO CODE_SEMESTERS VALUES (7,2001, 'Summer','05/15/2001','08/15/2001',2016);",
                     "INSERT INTO CODE_SEMESTERS VALUES (8,2001, 'Fall','08/15/2001','12/15/2001',2019);",
                     "INSERT INTO CODE_SEMESTERS VALUES (9,2002, 'Winter','12/15/2002','01/15/2002',2021);",
                     "INSERT INTO CODE_SEMESTERS VALUES (10,2002, 'Spring','01/15/2002','05/15/2002',2023);",
                     "INSERT INTO CODE_SEMESTERS VALUES (11,2002, 'Summer','05/15/2002','08/15/2002',2026);",
                     "INSERT INTO CODE_SEMESTERS VALUES (12,2002, 'Fall','08/15/2002','12/15/2002',2029);",
                     "INSERT INTO CODE_SEMESTERS VALUES (13,2003, 'Winter','12/15/2003','01/15/2003',2031);",
                     "INSERT INTO CODE_SEMESTERS VALUES (14,2003, 'Spring','01/15/2003','05/15/2003',2033);",
                     "INSERT INTO CODE_SEMESTERS VALUES (15,2003, 'Summer','05/15/2003','08/15/2003',2036);",
                     "INSERT INTO CODE_SEMESTERS VALUES (16,2003, 'Fall','08/15/2003','12/15/2003',2039);",
                     "INSERT INTO CODE_SEMESTERS VALUES (17,2004, 'Winter','12/15/2004','01/15/2004',2041);",
                     "INSERT INTO CODE_SEMESTERS VALUES (18,2004, 'Spring','01/15/2004','05/15/2004',2043);",
                     "INSERT INTO CODE_SEMESTERS VALUES (19,2004, 'Summer','05/15/2004','08/15/2004',2046);",
                     "INSERT INTO CODE_SEMESTERS VALUES (20,2004, 'Fall','08/15/2004','12/15/2004',2049);",
                     "INSERT INTO CODE_SEMESTERS VALUES (21,2005, 'Winter','12/15/2005','01/15/2005',2051);",
                     "INSERT INTO CODE_SEMESTERS VALUES (22,2005, 'Spring','01/15/2005','05/15/2005',2053);",
                     "INSERT INTO CODE_SEMESTERS VALUES (23,2005, 'Summer','05/15/2005','08/15/2005',2056);",
                     "INSERT INTO CODE_SEMESTERS VALUES (24,2005, 'Fall','08/15/2005','12/15/2005',2059);",
                     "INSERT INTO CODE_SEMESTERS VALUES (25,2006, 'Winter','12/15/2006','01/15/2006',2061);",
                     "INSERT INTO CODE_SEMESTERS VALUES (26,2006, 'Spring','01/15/2006','05/15/2006',2063);",
                     "INSERT INTO CODE_SEMESTERS VALUES (27,2006, 'Summer','05/15/2006','08/15/2006',2066);",
                     "INSERT INTO CODE_SEMESTERS VALUES (28,2006, 'Fall','08/15/2006','12/15/2006',2069);",
                     "INSERT INTO CODE_SEMESTERS VALUES (29,2007, 'Winter','12/15/2007','01/15/2007',2071);",
                     "INSERT INTO CODE_SEMESTERS VALUES (30,2007, 'Spring','01/15/2007','05/15/2007',2073);",
                     "INSERT INTO CODE_SEMESTERS VALUES (31,2007, 'Summer','05/15/2007','08/15/2007',2076);",
                     "INSERT INTO CODE_SEMESTERS VALUES (32,2007, 'Fall','08/15/2007','12/15/2007',2079);",
                     "INSERT INTO CODE_SEMESTERS VALUES (33,2008, 'Winter','12/15/2008','01/15/2008',2081);",
                     "INSERT INTO CODE_SEMESTERS VALUES (34,2008, 'Spring','01/15/2008','05/15/2008',2083);",
                     "INSERT INTO CODE_SEMESTERS VALUES (35,2008, 'Summer','05/15/2008','08/15/2008',2086);",
                     "INSERT INTO CODE_SEMESTERS VALUES (36,2008, 'Fall','08/15/2008','12/15/2008',2089);",
                     "INSERT INTO CODE_SEMESTERS VALUES (37,2009, 'Winter','12/15/2009','01/15/2009',2091);",
                     "INSERT INTO CODE_SEMESTERS VALUES (38,2009, 'Spring','01/15/2009','05/15/2009',2093);",
                     "INSERT INTO CODE_SEMESTERS VALUES (39,2009, 'Summer','05/15/2009','08/15/2009',2096);",
                     "INSERT INTO CODE_SEMESTERS VALUES (40,2009, 'Fall','08/15/2009','12/15/2009',2099);",
                     "INSERT INTO CODE_SEMESTERS VALUES (41,2010, 'Winter','12/15/2010','01/15/2010',2101);",
                     "INSERT INTO CODE_SEMESTERS VALUES (42,2010, 'Spring','01/15/2010','05/15/2010',2103);",
                     "INSERT INTO CODE_SEMESTERS VALUES (43,2010, 'Summer','05/15/2010','08/15/2010',2106);",
                     "INSERT INTO CODE_SEMESTERS VALUES (44,2010, 'Fall','08/15/2010','12/15/2010',2109);",
                     "INSERT INTO CODE_SEMESTERS VALUES (45,2011, 'Winter','12/15/2011','01/15/2011',2111);",
                     "INSERT INTO CODE_SEMESTERS VALUES (46,2011, 'Spring','01/15/2011','05/15/2011',2113);",
                     "INSERT INTO CODE_SEMESTERS VALUES (47,2011, 'Summer','05/15/2011','08/15/2011',2116);",
                     "INSERT INTO CODE_SEMESTERS VALUES (48,2011, 'Fall','08/15/2011','12/15/2011',2119);",
                     "INSERT INTO CODE_SEMESTERS VALUES (49,2012, 'Winter','12/15/2012','01/15/2012',2121);",
                     "INSERT INTO CODE_SEMESTERS VALUES (50,2012, 'Spring','01/15/2012','05/15/2012',2123);",
                     "INSERT INTO CODE_SEMESTERS VALUES (51,2012, 'Summer','05/15/2012','08/15/2012',2126);",
                     "INSERT INTO CODE_SEMESTERS VALUES (52,2012, 'Fall','08/15/2012','12/15/2012',2129);",
                     "INSERT INTO CODE_SEMESTERS VALUES (53,2013, 'Winter','12/15/2013','01/15/2013',2131);",
                     "INSERT INTO CODE_SEMESTERS VALUES (54,2013, 'Spring','01/15/2013','05/15/2013',2133);",
                     "INSERT INTO CODE_SEMESTERS VALUES (55,2013, 'Summer','05/15/2013','08/15/2013',2136);",
                     "INSERT INTO CODE_SEMESTERS VALUES (56,2013, 'Fall','08/15/2013','12/15/2013',2139);",
                     "INSERT INTO CODE_SEMESTERS VALUES (57,2014, 'Winter','12/15/2014','01/15/2014',2141);",
                     "INSERT INTO CODE_SEMESTERS VALUES (58,2014, 'Spring','01/15/2014','05/15/2014',2143);",
                     "INSERT INTO CODE_SEMESTERS VALUES (59,2014, 'Summer','05/15/2014','08/15/2014',2146);",
                     "INSERT INTO CODE_SEMESTERS VALUES (60,2014, 'Fall','08/15/2014','12/15/2014',2149);",
                     "INSERT INTO CODE_SEMESTERS VALUES (61,2015, 'Winter','12/15/2015','01/15/2015',2151);",
                     "INSERT INTO CODE_SEMESTERS VALUES (62,2015, 'Spring','01/15/2015','05/15/2015',2153);",
                     "INSERT INTO CODE_SEMESTERS VALUES (63,2015, 'Summer','05/15/2015','08/15/2015',2156);",
                     "INSERT INTO CODE_SEMESTERS VALUES (64,2015, 'Fall','08/15/2015','12/15/2015',2159);",
                     "INSERT INTO CODE_SEMESTERS VALUES (65,2016, 'Winter','12/15/2016','01/15/2016',2161);",
                     "INSERT INTO CODE_SEMESTERS VALUES (66,2016, 'Spring','01/15/2016','05/15/2016',2163);",
                     "INSERT INTO CODE_SEMESTERS VALUES (67,2016, 'Summer','05/15/2016','08/15/2016',2166);",
                     "INSERT INTO CODE_SEMESTERS VALUES (68,2016, 'Fall','08/15/2016','12/15/2016',2169);",
                     "INSERT INTO CODE_SEMESTERS VALUES (69,2017, 'Winter','12/15/2017','01/15/2017',2171);",
                     "INSERT INTO CODE_SEMESTERS VALUES (70,2017, 'Spring','01/15/2017','05/15/2017',2173);",
                     "INSERT INTO CODE_SEMESTERS VALUES (71,2017, 'Summer','05/15/2017','08/15/2017',2176);",
                     "INSERT INTO CODE_SEMESTERS VALUES (72,2017, 'Fall','08/15/2017','12/15/2017',2179);",
                     "INSERT INTO CODE_SEMESTERS VALUES (73,2018, 'Winter','12/15/2018','01/15/2018',2181);",
                     "INSERT INTO CODE_SEMESTERS VALUES (74,2018, 'Spring','01/15/2018','05/15/2018',2183);",
                     "INSERT INTO CODE_SEMESTERS VALUES (75,2018, 'Summer','05/15/2018','08/15/2018',2186);",
                     "INSERT INTO CODE_SEMESTERS VALUES (76,2018, 'Fall','08/15/2018','12/15/2018',2189);",
                     "INSERT INTO CODE_SEMESTERS VALUES (77,2019, 'Winter','12/15/2019','01/15/2019',2191);",
                     "INSERT INTO CODE_SEMESTERS VALUES (78,2019, 'Spring','01/15/2019','05/15/2019',2193);",
                     "INSERT INTO CODE_SEMESTERS VALUES (79,2019, 'Summer','05/15/2019','08/15/2019',2196);",
                     "INSERT INTO CODE_SEMESTERS VALUES (80,2019, 'Fall','08/15/2019','12/15/2019',2199);",
                     "INSERT INTO CODE_SEMESTERS VALUES (81,2020, 'Winter','12/15/2020','01/15/2020',2201);",
                     "INSERT INTO CODE_SEMESTERS VALUES (82,2020, 'Spring','01/15/2020','05/15/2020',2203);",
                     "INSERT INTO CODE_SEMESTERS VALUES (83,2020, 'Summer','05/15/2020','08/15/2020',2206);",
                     "INSERT INTO CODE_SEMESTERS VALUES (84,2020, 'Fall','08/15/2020','12/15/2020',2209);",
                     "INSERT INTO CODE_SEMESTERS VALUES (85,2021, 'Winter','12/15/2021','01/15/2021',2211);",
                     "INSERT INTO CODE_SEMESTERS VALUES (86,2021, 'Spring','01/15/2021','05/15/2021',2213);",
                     "INSERT INTO CODE_SEMESTERS VALUES (87,2021, 'Summer','05/15/2021','08/15/2021',2216);",
                     "INSERT INTO CODE_SEMESTERS VALUES (88,2021, 'Fall','08/15/2021','12/15/2021',2219);",
                     "INSERT INTO CODE_SEMESTERS VALUES (89,2022, 'Winter','12/15/2022','01/15/2022',2221);",
                     "INSERT INTO CODE_SEMESTERS VALUES (90,2022, 'Spring','01/15/2022','05/15/2022',2223);",
                     "INSERT INTO CODE_SEMESTERS VALUES (91,2022, 'Summer','05/15/2022','08/15/2022',2226);",
                     "INSERT INTO CODE_SEMESTERS VALUES (92,2022, 'Fall','08/15/2022','12/15/2022',2229);",
                     "INSERT INTO CODE_SEMESTERS VALUES (93,2023, 'Winter','12/15/2023','01/15/2023',2231);",
                     "INSERT INTO CODE_SEMESTERS VALUES (94,2023, 'Spring','01/15/2023','05/15/2023',2233);",
                     "INSERT INTO CODE_SEMESTERS VALUES (95,2023, 'Summer','05/15/2023','08/15/2023',2236);",
                     "INSERT INTO CODE_SEMESTERS VALUES (96,2023, 'Fall','08/15/2023','12/15/2023',2239);",
                     "INSERT INTO CODE_SEMESTERS VALUES (97,2024, 'Winter','12/15/2024','01/15/2024',2241);",
                     "INSERT INTO CODE_SEMESTERS VALUES (98,2024, 'Spring','01/15/2024','05/15/2024',2243);",
                     "INSERT INTO CODE_SEMESTERS VALUES (99,2024, 'Summer','05/15/2024','08/15/2024',2246);",
                     "INSERT INTO CODE_SEMESTERS VALUES (100,2024, 'Fall','08/15/2024','12/15/2024',2249);",
                     "INSERT INTO CODE_SEMESTERS VALUES (101,2025, 'Winter','12/15/2025','01/15/2025',2251);",
                     "INSERT INTO CODE_SEMESTERS VALUES (102,2025, 'Spring','01/15/2025','05/15/2025',2253);",
                     "INSERT INTO CODE_SEMESTERS VALUES (103,2025, 'Summer','05/15/2025','08/15/2025',2256);",
                     "INSERT INTO CODE_SEMESTERS VALUES (104,2025, 'Fall','08/15/2025','12/15/2025',2259);",
                     "INSERT INTO CODE_SEMESTERS VALUES (105,2026, 'Winter','12/15/2026','01/15/2026',2261);",
                     "INSERT INTO CODE_SEMESTERS VALUES (106,2026, 'Spring','01/15/2026','05/15/2026',2263);",
                     "INSERT INTO CODE_SEMESTERS VALUES (107,2026, 'Summer','05/15/2026','08/15/2026',2266);",
                     "INSERT INTO CODE_SEMESTERS VALUES (108,2026, 'Fall','08/15/2026','12/15/2026',2269);",
                     "INSERT INTO CODE_SEMESTERS VALUES (109,2027, 'Winter','12/15/2027','01/15/2027',2271);",
                     "INSERT INTO CODE_SEMESTERS VALUES (110,2027, 'Spring','01/15/2027','05/15/2027',2273);",
                     "INSERT INTO CODE_SEMESTERS VALUES (111,2027, 'Summer','05/15/2027','08/15/2027',2276);",
                     "INSERT INTO CODE_SEMESTERS VALUES (112,2027, 'Fall','08/15/2027','12/15/2027',2279);",
                     "INSERT INTO CODE_SEMESTERS VALUES (113,2028, 'Winter','12/15/2028','01/15/2028',2281);",
                     "INSERT INTO CODE_SEMESTERS VALUES (114,2028, 'Spring','01/15/2028','05/15/2028',2283);",
                     "INSERT INTO CODE_SEMESTERS VALUES (115,2028, 'Summer','05/15/2028','08/15/2028',2286);",
                     "INSERT INTO CODE_SEMESTERS VALUES (116,2028, 'Fall','08/15/2028','12/15/2028',2289);",
                     "INSERT INTO CODE_SEMESTERS VALUES (117,2029, 'Winter','12/15/2029','01/15/2029',2291);",
                     "INSERT INTO CODE_SEMESTERS VALUES (118,2029, 'Spring','01/15/2029','05/15/2029',2293);",
                     "INSERT INTO CODE_SEMESTERS VALUES (119,2029, 'Summer','05/15/2029','08/15/2029',2296);",
                     "INSERT INTO CODE_SEMESTERS VALUES (120,2029, 'Fall','08/15/2029','12/15/2029',2299);",
                     "INSERT INTO CODE_SEMESTERS VALUES (121,2030, 'Winter','12/15/2030','01/15/2030',2301);",
                     "INSERT INTO CODE_SEMESTERS VALUES (122,2030, 'Spring','01/15/2030','05/15/2030',2303);",
                     "INSERT INTO CODE_SEMESTERS VALUES (123,2030, 'Summer','05/15/2030','08/15/2030',2306);",
                     "INSERT INTO CODE_SEMESTERS VALUES (124,2030, 'Fall','08/15/2030','12/15/2030',2309);",
                     "INSERT INTO CODE_SEMESTERS VALUES (125,2031, 'Winter','12/15/2031','01/15/2031',2311);",
                     "INSERT INTO CODE_SEMESTERS VALUES (126,2031, 'Spring','01/15/2031','05/15/2031',2313);",
                     "INSERT INTO CODE_SEMESTERS VALUES (127,2031, 'Summer','05/15/2031','08/15/2031',2316);",
                     "INSERT INTO CODE_SEMESTERS VALUES (128,2031, 'Fall','08/15/2031','12/15/2031',2319);",
                     "INSERT INTO CODE_SEMESTERS VALUES (129,2032, 'Winter','12/15/2032','01/15/2032',2321);",
                     "INSERT INTO CODE_SEMESTERS VALUES (130,2032, 'Spring','01/15/2032','05/15/2032',2323);",
                     "INSERT INTO CODE_SEMESTERS VALUES (131,2032, 'Summer','05/15/2032','08/15/2032',2326);",
                     "INSERT INTO CODE_SEMESTERS VALUES (132,2032, 'Fall','08/15/2032','12/15/2032',2329);",
                     "INSERT INTO CODE_SEMESTERS VALUES (133,2033, 'Winter','12/15/2033','01/15/2033',2331);",
                     "INSERT INTO CODE_SEMESTERS VALUES (134,2033, 'Spring','01/15/2033','05/15/2033',2333);",
                     "INSERT INTO CODE_SEMESTERS VALUES (135,2033, 'Summer','05/15/2033','08/15/2033',2336);",
                     "INSERT INTO CODE_SEMESTERS VALUES (136,2033, 'Fall','08/15/2033','12/15/2033',2339);",
                     "INSERT INTO CODE_SEMESTERS VALUES (137,2034, 'Winter','12/15/2034','01/15/2034',2341);",
                     "INSERT INTO CODE_SEMESTERS VALUES (138,2034, 'Spring','01/15/2034','05/15/2034',2343);",
                     "INSERT INTO CODE_SEMESTERS VALUES (139,2034, 'Summer','05/15/2034','08/15/2034',2346);",
                     "INSERT INTO CODE_SEMESTERS VALUES (140,2034, 'Fall','08/15/2034','12/15/2034',2349);",
                     "INSERT INTO CODE_SEMESTERS VALUES (141,2035, 'Winter','12/15/2035','01/15/2035',2351);",
                     "INSERT INTO CODE_SEMESTERS VALUES (142,2035, 'Spring','01/15/2035','05/15/2035',2353);",
                     "INSERT INTO CODE_SEMESTERS VALUES (143,2035, 'Summer','05/15/2035','08/15/2035',2356);",
                     "INSERT INTO CODE_SEMESTERS VALUES (144,2035, 'Fall','08/15/2035','12/15/2035',2359);",
                     "INSERT INTO CODE_SEMESTERS VALUES (145,2036, 'Winter','12/15/2036','01/15/2036',2361);",
                     "INSERT INTO CODE_SEMESTERS VALUES (146,2036, 'Spring','01/15/2036','05/15/2036',2363);",
                     "INSERT INTO CODE_SEMESTERS VALUES (147,2036, 'Summer','05/15/2036','08/15/2036',2366);",
                     "INSERT INTO CODE_SEMESTERS VALUES (148,2036, 'Fall','08/15/2036','12/15/2036',2369);",
                     "INSERT INTO CODE_SEMESTERS VALUES (149,2037, 'Winter','12/15/2037','01/15/2037',2371);",
                     "INSERT INTO CODE_SEMESTERS VALUES (150,2037, 'Spring','01/15/2037','05/15/2037',2373);",
                     "INSERT INTO CODE_SEMESTERS VALUES (151,2037, 'Summer','05/15/2037','08/15/2037',2376);",
                     "INSERT INTO CODE_SEMESTERS VALUES (152,2037, 'Fall','08/15/2037','12/15/2037',2379);",
                     "INSERT INTO CODE_SEMESTERS VALUES (153,2038, 'Winter','12/15/2038','01/15/2038',2381);",
                     "INSERT INTO CODE_SEMESTERS VALUES (154,2038, 'Spring','01/15/2038','05/15/2038',2383);",
                     "INSERT INTO CODE_SEMESTERS VALUES (155,2038, 'Summer','05/15/2038','08/15/2038',2386);",
                     "INSERT INTO CODE_SEMESTERS VALUES (156,2038, 'Fall','08/15/2038','12/15/2038',2389);",
                     "INSERT INTO CODE_SEMESTERS VALUES (157,2039, 'Winter','12/15/2039','01/15/2039',2391);",
                     "INSERT INTO CODE_SEMESTERS VALUES (158,2039, 'Spring','01/15/2039','05/15/2039',2393);",
                     "INSERT INTO CODE_SEMESTERS VALUES (159,2039, 'Summer','05/15/2039','08/15/2039',2396);",
                     "INSERT INTO CODE_SEMESTERS VALUES (160,2039, 'Fall','08/15/2039','12/15/2039',2399);",
                     "INSERT INTO CODE_SEMESTERS VALUES (161,2040, 'Winter','12/15/2040','01/15/2040',2401);",
                     "INSERT INTO CODE_SEMESTERS VALUES (162,2040, 'Spring','01/15/2040','05/15/2040',2403);",
                     "INSERT INTO CODE_SEMESTERS VALUES (163,2040, 'Summer','05/15/2040','08/15/2040',2406);",
                     "INSERT INTO CODE_SEMESTERS VALUES (164,2040, 'Fall','08/15/2040','12/15/2040',2409);",
                     "INSERT INTO CODE_SEMESTERS VALUES (165,2041, 'Winter','12/15/2041','01/15/2041',2411);",
                     "INSERT INTO CODE_SEMESTERS VALUES (166,2041, 'Spring','01/15/2041','05/15/2041',2413);",
                     "INSERT INTO CODE_SEMESTERS VALUES (167,2041, 'Summer','05/15/2041','08/15/2041',2416);",
                     "INSERT INTO CODE_SEMESTERS VALUES (168,2041, 'Fall','08/15/2041','12/15/2041',2419);",
                     "INSERT INTO CODE_SEMESTERS VALUES (169,2042, 'Winter','12/15/2042','01/15/2042',2421);",
                     "INSERT INTO CODE_SEMESTERS VALUES (170,2042, 'Spring','01/15/2042','05/15/2042',2423);",
                     "INSERT INTO CODE_SEMESTERS VALUES (171,2042, 'Summer','05/15/2042','08/15/2042',2426);",
                     "INSERT INTO CODE_SEMESTERS VALUES (172,2042, 'Fall','08/15/2042','12/15/2042',2429);",
                     "INSERT INTO CODE_SEMESTERS VALUES (173,2043, 'Winter','12/15/2043','01/15/2043',2431);",
                     "INSERT INTO CODE_SEMESTERS VALUES (174,2043, 'Spring','01/15/2043','05/15/2043',2433);",
                     "INSERT INTO CODE_SEMESTERS VALUES (175,2043, 'Summer','05/15/2043','08/15/2043',2436);",
                     "INSERT INTO CODE_SEMESTERS VALUES (176,2043, 'Fall','08/15/2043','12/15/2043',2439);",
                     "INSERT INTO CODE_SEMESTERS VALUES (177,2044, 'Winter','12/15/2044','01/15/2044',2441);",
                     "INSERT INTO CODE_SEMESTERS VALUES (178,2044, 'Spring','01/15/2044','05/15/2044',2443);",
                     "INSERT INTO CODE_SEMESTERS VALUES (179,2044, 'Summer','05/15/2044','08/15/2044',2446);",
                     "INSERT INTO CODE_SEMESTERS VALUES (180,2044, 'Fall','08/15/2044','12/15/2044',2449);",
                     "INSERT INTO CODE_SEMESTERS VALUES (181,2045, 'Winter','12/15/2045','01/15/2045',2451);",
                     "INSERT INTO CODE_SEMESTERS VALUES (182,2045, 'Spring','01/15/2045','05/15/2045',2453);",
                     "INSERT INTO CODE_SEMESTERS VALUES (183,2045, 'Summer','05/15/2045','08/15/2045',2456);",
                     "INSERT INTO CODE_SEMESTERS VALUES (184,2045, 'Fall','08/15/2045','12/15/2045',2459);",
                     "INSERT INTO CODE_SEMESTERS VALUES (185,2046, 'Winter','12/15/2046','01/15/2046',2461);",
                     "INSERT INTO CODE_SEMESTERS VALUES (186,2046, 'Spring','01/15/2046','05/15/2046',2463);",
                     "INSERT INTO CODE_SEMESTERS VALUES (187,2046, 'Summer','05/15/2046','08/15/2046',2466);",
                     "INSERT INTO CODE_SEMESTERS VALUES (188,2046, 'Fall','08/15/2046','12/15/2046',2469);",
                     "INSERT INTO CODE_SEMESTERS VALUES (189,2047, 'Winter','12/15/2047','01/15/2047',2471);",
                     "INSERT INTO CODE_SEMESTERS VALUES (190,2047, 'Spring','01/15/2047','05/15/2047',2473);",
                     "INSERT INTO CODE_SEMESTERS VALUES (191,2047, 'Summer','05/15/2047','08/15/2047',2476);",
                     "INSERT INTO CODE_SEMESTERS VALUES (192,2047, 'Fall','08/15/2047','12/15/2047',2479);",
                     "INSERT INTO CODE_SEMESTERS VALUES (193,2048, 'Winter','12/15/2048','01/15/2048',2481);",
                     "INSERT INTO CODE_SEMESTERS VALUES (194,2048, 'Spring','01/15/2048','05/15/2048',2483);",
                     "INSERT INTO CODE_SEMESTERS VALUES (195,2048, 'Summer','05/15/2048','08/15/2048',2486);",
                     "INSERT INTO CODE_SEMESTERS VALUES (196,2048, 'Fall','08/15/2048','12/15/2048',2489);",
                     "INSERT INTO CODE_SEMESTERS VALUES (197,2049, 'Winter','12/15/2049','01/15/2049',2491);",
                     "INSERT INTO CODE_SEMESTERS VALUES (198,2049, 'Spring','01/15/2049','05/15/2049',2493);",
                     "INSERT INTO CODE_SEMESTERS VALUES (199,2049, 'Summer','05/15/2049','08/15/2049',2496);",
                     "INSERT INTO CODE_SEMESTERS VALUES (200,2049, 'Fall','08/15/2049','12/15/2049',2499);",
                     "INSERT INTO CODE_SEMESTERS VALUES (201,2050, 'Winter','12/15/2050','01/15/2050',2501);",
                     "INSERT INTO CODE_SEMESTERS VALUES (202,2050, 'Spring','01/15/2050','05/15/2050',2503);",
                     "INSERT INTO CODE_SEMESTERS VALUES (203,2050, 'Summer','05/15/2050','08/15/2050',2506);",
                     "INSERT INTO CODE_SEMESTERS VALUES (204,2050, 'Fall','08/15/2050','12/15/2050',2509);",
                     "INSERT INTO CODE_SEMESTERS VALUES (205,2051, 'Winter','12/15/2051','01/15/2051',2511);",
                     "INSERT INTO CODE_SEMESTERS VALUES (206,2051, 'Spring','01/15/2051','05/15/2051',2513);",
                     "INSERT INTO CODE_SEMESTERS VALUES (207,2051, 'Summer','05/15/2051','08/15/2051',2516);",
                     "INSERT INTO CODE_SEMESTERS VALUES (208,2051, 'Fall','08/15/2051','12/15/2051',2519);",
                     "INSERT INTO CODE_SEMESTERS VALUES (209,2052, 'Winter','12/15/2052','01/15/2052',2521);",
                     "INSERT INTO CODE_SEMESTERS VALUES (210,2052, 'Spring','01/15/2052','05/15/2052',2523);",
                     "INSERT INTO CODE_SEMESTERS VALUES (211,2052, 'Summer','05/15/2052','08/15/2052',2526);",
                     "INSERT INTO CODE_SEMESTERS VALUES (212,2052, 'Fall','08/15/2052','12/15/2052',2529);",
                     "INSERT INTO CODE_SEMESTERS VALUES (213,2053, 'Winter','12/15/2053','01/15/2053',2531);",
                     "INSERT INTO CODE_SEMESTERS VALUES (214,2053, 'Spring','01/15/2053','05/15/2053',2533);",
                     "INSERT INTO CODE_SEMESTERS VALUES (215,2053, 'Summer','05/15/2053','08/15/2053',2536);",
                     "INSERT INTO CODE_SEMESTERS VALUES (216,2053, 'Fall','08/15/2053','12/15/2053',2539);",
                     "INSERT INTO CODE_SEMESTERS VALUES (217,2054, 'Winter','12/15/2054','01/15/2054',2541);",
                     "INSERT INTO CODE_SEMESTERS VALUES (218,2054, 'Spring','01/15/2054','05/15/2054',2543);",
                     "INSERT INTO CODE_SEMESTERS VALUES (219,2054, 'Summer','05/15/2054','08/15/2054',2546);",
                     "INSERT INTO CODE_SEMESTERS VALUES (220,2054, 'Fall','08/15/2054','12/15/2054',2549);",
                     "INSERT INTO CODE_SEMESTERS VALUES (221,2055, 'Winter','12/15/2055','01/15/2055',2551);",
                     "INSERT INTO CODE_SEMESTERS VALUES (222,2055, 'Spring','01/15/2055','05/15/2055',2553);",
                     "INSERT INTO CODE_SEMESTERS VALUES (223,2055, 'Summer','05/15/2055','08/15/2055',2556);",
                     "INSERT INTO CODE_SEMESTERS VALUES (224,2055, 'Fall','08/15/2055','12/15/2055',2559);",
                     "INSERT INTO CODE_SEMESTERS VALUES (225,2056, 'Winter','12/15/2056','01/15/2056',2561);",
                     "INSERT INTO CODE_SEMESTERS VALUES (226,2056, 'Spring','01/15/2056','05/15/2056',2563);",
                     "INSERT INTO CODE_SEMESTERS VALUES (227,2056, 'Summer','05/15/2056','08/15/2056',2566);",
                     "INSERT INTO CODE_SEMESTERS VALUES (228,2056, 'Fall','08/15/2056','12/15/2056',2569);",
                     "INSERT INTO CODE_SEMESTERS VALUES (229,2057, 'Winter','12/15/2057','01/15/2057',2571);",
                     "INSERT INTO CODE_SEMESTERS VALUES (230,2057, 'Spring','01/15/2057','05/15/2057',2573);",
                     "INSERT INTO CODE_SEMESTERS VALUES (231,2057, 'Summer','05/15/2057','08/15/2057',2576);",
                     "INSERT INTO CODE_SEMESTERS VALUES (232,2057, 'Fall','08/15/2057','12/15/2057',2579);",
                     "INSERT INTO CODE_SEMESTERS VALUES (233,2058, 'Winter','12/15/2058','01/15/2058',2581);",
                     "INSERT INTO CODE_SEMESTERS VALUES (234,2058, 'Spring','01/15/2058','05/15/2058',2583);",
                     "INSERT INTO CODE_SEMESTERS VALUES (235,2058, 'Summer','05/15/2058','08/15/2058',2586);",
                     "INSERT INTO CODE_SEMESTERS VALUES (236,2058, 'Fall','08/15/2058','12/15/2058',2589);",
                     "INSERT INTO CODE_SEMESTERS VALUES (237,2059, 'Winter','12/15/2059','01/15/2059',2591);",
                     "INSERT INTO CODE_SEMESTERS VALUES (238,2059, 'Spring','01/15/2059','05/15/2059',2593);",
                     "INSERT INTO CODE_SEMESTERS VALUES (239,2059, 'Summer','05/15/2059','08/15/2059',2596);",
                     "INSERT INTO CODE_SEMESTERS VALUES (240,2059, 'Fall','08/15/2059','12/15/2059',2599);",
                     "INSERT INTO CODE_SEMESTERS VALUES (241,2060, 'Winter','12/15/2060','01/15/2060',2601);",
                     "INSERT INTO CODE_SEMESTERS VALUES (242,2060, 'Spring','01/15/2060','05/15/2060',2603);",
                     "INSERT INTO CODE_SEMESTERS VALUES (243,2060, 'Summer','05/15/2060','08/15/2060',2606);",
                     "INSERT INTO CODE_SEMESTERS VALUES (244,2060, 'Fall','08/15/2060','12/15/2060',2609);",
                     "INSERT INTO CODE_SEMESTERS VALUES (245,2061, 'Winter','12/15/2061','01/15/2061',2611);",
                     "INSERT INTO CODE_SEMESTERS VALUES (246,2061, 'Spring','01/15/2061','05/15/2061',2613);",
                     "INSERT INTO CODE_SEMESTERS VALUES (247,2061, 'Summer','05/15/2061','08/15/2061',2616);",
                     "INSERT INTO CODE_SEMESTERS VALUES (248,2061, 'Fall','08/15/2061','12/15/2061',2619);",
                     "INSERT INTO CODE_SEMESTERS VALUES (249,2062, 'Winter','12/15/2062','01/15/2062',2621);",
                     "INSERT INTO CODE_SEMESTERS VALUES (250,2062, 'Spring','01/15/2062','05/15/2062',2623);",
                     "INSERT INTO CODE_SEMESTERS VALUES (251,2062, 'Summer','05/15/2062','08/15/2062',2626);",
                     "INSERT INTO CODE_SEMESTERS VALUES (252,2062, 'Fall','08/15/2062','12/15/2062',2629);",
                     "INSERT INTO CODE_SEMESTERS VALUES (253,2063, 'Winter','12/15/2063','01/15/2063',2631);",
                     "INSERT INTO CODE_SEMESTERS VALUES (254,2063, 'Spring','01/15/2063','05/15/2063',2633);",
                     "INSERT INTO CODE_SEMESTERS VALUES (255,2063, 'Summer','05/15/2063','08/15/2063',2636);",
                     "INSERT INTO CODE_SEMESTERS VALUES (256,2063, 'Fall','08/15/2063','12/15/2063',2639);",
                     "INSERT INTO CODE_SEMESTERS VALUES (257,2064, 'Winter','12/15/2064','01/15/2064',2641);",
                     "INSERT INTO CODE_SEMESTERS VALUES (258,2064, 'Spring','01/15/2064','05/15/2064',2643);",
                     "INSERT INTO CODE_SEMESTERS VALUES (259,2064, 'Summer','05/15/2064','08/15/2064',2646);",
                     "INSERT INTO CODE_SEMESTERS VALUES (260,2064, 'Fall','08/15/2064','12/15/2064',2649);"]

    return sqlstatements


# Set specific persons to "Inactive" (11/17/21)
def inactivatepeople():
    sqlstatements = ["update data_persons set active=false where lastname='Kramer' and firstname = 'Laura';",
                     "update data_persons set active=false where lastname='Cao' and firstname = 'Zhengzhong';",
                     "update data_persons set active=false where lastname='Birkland' and firstname = 'Thomas';",
                     "update data_persons set active=false where lastname='Calef' and firstname = 'Monika';",
                     "update data_persons set active=false where lastname='Carpenter' and firstname = 'David';",
                     "update data_persons set active=false where lastname='Castracane' and firstname = 'James';",
                     "update data_persons set active=false where lastname='Ciota' and firstname = 'Alex';",
                     "update data_persons set active=false where lastname='Conn' and firstname = 'Jan';",
                     "update data_persons set active=false where lastname='Cryan' and firstname = 'Jason';",
                     "update data_persons set active=false where lastname='Daniels' and firstname = 'Robert';",
                     "update data_persons set active=false where lastname='Davis' and firstname = 'April';",
                     "update data_persons set active=false where lastname='Dudek' and firstname = 'Bruce';",
                     "update data_persons set active=false where lastname='Fraser' and firstname = 'Douglas';",
                     "update data_persons set active=false where lastname='Frye' and firstname = 'Cheryl';",
                     "update data_persons set active=false where lastname='Groffman' and firstname = 'Peter';",
                     "update data_persons set active=false where lastname='Guda' and firstname = 'Chittibabu';",
                     "update data_persons set active=false where lastname='Kays' and firstname = 'Roland';",
                     "update data_persons set active=false where lastname='Kimelberg' and firstname = 'Harold';",
                     "update data_persons set active=false where lastname='Kolozsvary' and firstname = 'Mary';",
                     "update data_persons set active=false where lastname='Likens' and firstname = 'Gene';",
                     "update data_persons set active=false where lastname='Lovett' and firstname = 'Gary';",
                     "update data_persons set active=false where lastname='Mannella' and firstname = 'Carmen';",
                     "update data_persons set active=false where lastname='Martin' and firstname = 'David';",
                     "update data_persons set active=false where lastname='McKeown-Longo' and firstname = 'Paula';",
                     "update data_persons set active=false where lastname='Miller' and firstname = 'Norton';",
                     "update data_persons set active=false where lastname='Molloy' and firstname = 'Daniel';",
                     "update data_persons set active=false where lastname='Newman' and firstname = 'Jonathan';",
                     "update data_persons set active=false where lastname='O'Neal' and firstname = 'Dawn';",
                     "update data_persons set active=false where lastname='Rieder' and firstname = 'Conly';",
                     "update data_persons set active=false where lastname='Sell' and firstname = 'Stewart';",
                     "update data_persons set active=false where lastname='Siegfried' and firstname = 'Clifford';",
                     "update data_persons set active=false where lastname='Smith' and firstname = 'Charles R.';",
                     "update data_persons set active=false where lastname='Strayer' and firstname = 'David';",
                     "update data_persons set active=false where lastname='Tine' and firstname = 'John';",
                     "update data_persons set active=false where lastname='Wright' and firstname = 'Jeremy';",
                     "update data_persons set active=false where lastname='Wyman' and firstname = 'Richard';",
                     "update data_persons set active=false where lastname='Belostotsky' and firstname = 'Dmitry';",
                     "update data_persons set active=false where lastname='Breen' and firstname = 'Riobart (Rob)';",
                     "update data_persons set active=false where lastname='Brown' and firstname = 'Stephen';",
                     "update data_persons set active=false where lastname='Brown' and firstname = 'William';",
                     "update data_persons set active=false where lastname='Chen' and firstname = 'Yu';",
                     "update data_persons set active=false where lastname='Fabris' and firstname = 'Daniele';",
                     "update data_persons set active=false where lastname='Izzard' and firstname = 'Colin';",
                     "update data_persons set active=false where lastname='Love' and firstname = 'Rebecca';",
                     "update data_persons set active=false where lastname='Mascarenhas' and firstname = 'Joseph';",
                     "update data_persons set active=false where lastname='Millis' and firstname = 'Albert';",
                     "update data_persons set active=false where lastname='Murphy' and firstname = 'Patrick Shawn';",
                     "update data_persons set active=false where lastname='Pidgeon' and firstname = 'Jessica';",
                     "update data_persons set active=false where lastname='Rusconi' and firstname = 'Jamie';",
                     "update data_persons set active=false where lastname='Stewart' and firstname = 'Caro-Beth';",
                     "update data_persons set active=false where lastname='Tedeshi' and firstname = 'Henry';",
                     "update data_persons set active=false where lastname='Zhu' and firstname = 'Lin';",
                     "update data_persons set active=false where lastname='Al Lakhen' and firstname = 'Khalid';",
                     "update data_persons set active=false where lastname='Allen' and firstname = 'Erin';",
                     "update data_persons set active=false where lastname='Antonucci' and firstname = 'Brittany';",
                     "update data_persons set active=false where lastname='Bell' and firstname = 'Adam';",
                     "update data_persons set active=false where lastname='Blatt' and firstname = 'Patrick';",
                     "update data_persons set active=false where lastname='Bonenfant' and firstname = 'Gaston';",
                     "update data_persons set active=false where lastname='Bonitatibus' and firstname = 'Jillian';",
                     "update data_persons set active=false where lastname='Bradley' and firstname = 'Joseph';",
                     "update data_persons set active=false where lastname='Caboot' and firstname = 'Emily';",
                     "update data_persons set active=false where lastname='Cassidy' and firstname = 'Lisa';",
                     "update data_persons set active=false where lastname='Champagne' and firstname = 'Julia';",
                     "update data_persons set active=false where lastname='Cooper' and firstname = 'Izaac';",
                     "update data_persons set active=false where lastname='Dagley' and firstname = 'Brian';",
                     "update data_persons set active=false where lastname='Drasser' and firstname = 'Cassidy';",
                     "update data_persons set active=false where lastname='Fleming' and firstname = 'Kelsey';",
                     "update data_persons set active=false where lastname='Gasperi' and firstname = 'William';",
                     "update data_persons set active=false where lastname='Giorgio' and firstname = 'Angelina';",
                     "update data_persons set active=false where lastname='Greagan' and firstname = 'Mary';",
                     "update data_persons set active=false where lastname='Hagedorn' and firstname = 'Zachary';",
                     "update data_persons set active=false where lastname='Sehta' and firstname = 'Priyanka';",
                     "update data_persons set active=false where lastname='Soyer' and firstname = 'Miles';",
                     "update data_persons set active=false where lastname='Tomaszek' and firstname = 'Lindsay';",
                     "update data_persons set active=false where lastname='Agris' and firstname = 'Paul';",
                     "update data_persons set active=false where lastname='Araldi-Brondolo' and firstname = 'Sarah';",
                     "update data_persons set active=false where lastname='Bacot-Davis' and firstname = 'Valjean';",
                     "update data_persons set active=false where lastname='Bailey' and firstname = 'Elgin (Jake)';",
                     "update data_persons set active=false where lastname='Baronner' and firstname = 'Joanne';",
                     "update data_persons set active=false where lastname='Begley' and firstname = 'Ulrike';",
                     "update data_persons set active=false where lastname='Bellini' and firstname = 'Stefania';",
                     "update data_persons set active=false where lastname='Biegel' and firstname = 'Jason';",
                     "update data_persons set active=false where lastname='Chandrasekaran' and firstname = 'Arun Richard';",
                     "update data_persons set active=false where lastname='Chen' and firstname = 'Kuihao';",
                     "update data_persons set active=false where lastname='Chertoff' and firstname = 'Lori';",
                     "update data_persons set active=false where lastname='Collura' and firstname = 'Randall';",
                     "update data_persons set active=false where lastname='Eruysal' and firstname = 'Emily';",
                     "update data_persons set active=false where lastname='Jacklet' and firstname = 'Alice';",
                     "update data_persons set active=false where lastname='Jayachandran' and firstname = 'Pradeepa';",
                     "update data_persons set active=false where lastname='Kahn' and firstname = 'Samantha';",
                     "update data_persons set active=false where lastname='Karsli Uzunbas' and firstname = 'Gizem';",
                     "update data_persons set active=false where lastname='Koslow' and firstname = 'Matthew';",
                     "update data_persons set active=false where lastname='Lennon' and firstname = 'Christopher';",
                     "update data_persons set active=false where lastname='Mallik' and firstname = 'Prabhat';",
                     "update data_persons set active=false where lastname='McCarthy' and firstname = 'Rebecca';",
                     "update data_persons set active=false where lastname='Mock' and firstname = 'Vanessa';",
                     "update data_persons set active=false where lastname='Narendran' and firstname = 'Amithi';",
                     "update data_persons set active=false where lastname='Nye' and firstname = 'Peter';",
                     "update data_persons set active=false where lastname='Pocchiari' and firstname = 'Tyler';",
                     "update data_persons set active=false where lastname='Prasad' and firstname = 'Aparna';",
                     "update data_persons set active=false where lastname='Qu' and firstname = 'Guosheng';",
                     "update data_persons set active=false where lastname='Saha' and firstname = 'Subhrakanti';",
                     "update data_persons set active=false where lastname='Singh' and firstname = 'Tatyana';",
                     "update data_persons set active=false where lastname='Smith' and firstname = 'Dorie';",
                     "update data_persons set active=false where lastname='Tluckova' and firstname = 'Katarina';",
                     "update data_persons set active=false where lastname='Todd' and firstname = 'Gabrielle';",
                     "update data_persons set active=false where lastname='Woods' and firstname = 'Daniel';",
                     "update data_persons set active=false where lastname='Yukilevich' and firstname = 'Roman';",
                     "update data_persons set active=false where lastname='Zappieri' and firstname = 'Jeff';",
                     "update data_persons set active=false where lastname='Zuo' and firstname = 'Dongchuan';",
                     "update data_persons set active=false where lastname='Eastman' and firstname = 'Allison';",
                     "update data_persons set active=false where lastname='Robinson' and firstname = 'Ingrid P.';",
                     "update data_persons set active=false where lastname='Brown' and firstname = 'Jerram';",
                     "update data_persons set active=false where lastname='Caraco' and firstname = 'Tom';",
                     "update data_persons set active=false where lastname='Ghiradella' and firstname = 'Helen';",
                     "update data_persons set active=false where lastname='Gonder' and firstname = 'Mary Katherine';",
                     "update data_persons set active=false where lastname='Hirsch' and firstname = 'Helmut';",
                     "update data_persons set active=false where lastname='Iyengar' and firstname = 'Arati';",
                     "update data_persons set active=false where lastname='Jacklet' and firstname = 'Jon';",
                     "update data_persons set active=false where lastname='Kleppel' and firstname = 'Gary';",
                     "update data_persons set active=false where lastname='Mackiewicz' and firstname = 'John';",
                     "update data_persons set active=false where lastname='Robinson' and firstname = 'George';",
                     "update data_persons set active=false where lastname='Schmidt' and firstname = 'John';",
                     "update data_persons set active=false where lastname='Shub' and firstname = 'David';",
                     "update data_persons set active=false where lastname='Turner' and firstname = 'Wendy';",
                     "update data_persons set active=false where lastname='Wulff' and firstname = 'Daniel';",
                     "update data_persons set active=false where lastname='Zitomer' and firstname = 'Richard';",
                     "update data_persons set active=false where lastname='Barandongo' and firstname = 'Zoe';",
                     "update data_persons set active=false where lastname='Belrose' and firstname = 'Jamie';",
                     "update data_persons set active=false where lastname='Bender' and firstname = 'Philip';",
                     "update data_persons set active=false where lastname='Catizone' and firstname = 'Allison';",
                     "update data_persons set active=false where lastname='Choudhary' and firstname = 'Rupa';",
                     "update data_persons set active=false where lastname='Couttee' and firstname = 'Marie';",
                     "update data_persons set active=false where lastname='De' and firstname = 'Modhurika';",
                     "update data_persons set active=false where lastname='DeSantis' and firstname = 'Kara';",
                     "update data_persons set active=false where lastname='Dolfi' and firstname = 'Amelie';",
                     "update data_persons set active=false where lastname='Dong' and firstname = 'Xiaolong (Eren)';",
                     "update data_persons set active=false where lastname='Duffy' and firstname = 'Connor';",
                     "update data_persons set active=false where lastname='Eapen' and firstname = 'Alan';",
                     "update data_persons set active=false where lastname='Eason' and firstname = 'Kayla';",
                     "update data_persons set active=false where lastname='Farajallah Hosseini' and firstname = 'Zeinab';",
                     "update data_persons set active=false where lastname='FitzGerald' and firstname = 'Alyssa';",
                     "update data_persons set active=false where lastname='Flora' and firstname = 'Pooja';",
                     "update data_persons set active=false where lastname='Fraser' and firstname = 'Antoinette';",
                     "update data_persons set active=false where lastname='Girard-Cartier' and firstname = 'Caroline';",
                     "update data_persons set active=false where lastname='Gore' and firstname = 'Bethany';",
                     "update data_persons set active=false where lastname='Hart' and firstname = 'Thomas';",
                     "update data_persons set active=false where lastname='Henderson' and firstname = 'Eric';",
                     "update data_persons set active=false where lastname='Holbert' and firstname = 'Julianne';",
                     "update data_persons set active=false where lastname='Howlett Lipari' and firstname = 'Lindsey';",
                     "update data_persons set active=false where lastname='Hoyt' and firstname = 'Christopher';",
                     "update data_persons set active=false where lastname='Huang' and firstname = 'Yen-Hua';",
                     "update data_persons set active=false where lastname='Isidoridy' and firstname = 'Andrew';",
                     "update data_persons set active=false where lastname='James' and firstname = 'Tonia-Marie';",
                     "update data_persons set active=false where lastname='Jenkins' and firstname = 'Frank';",
                     "update data_persons set active=false where lastname='Jiang' and firstname = 'Yizhou';",
                     "update data_persons set active=false where lastname='Kelley' and firstname = 'Danielle';",
                     "update data_persons set active=false where lastname='Kelly' and firstname = 'Alyson';",
                     "update data_persons set active=false where lastname='Kenneally' and firstname = 'Jayne';",
                     "update data_persons set active=false where lastname='Kipper' and firstname = 'Laura';",
                     "update data_persons set active=false where lastname='Kuna' and firstname = 'Michael';",
                     "update data_persons set active=false where lastname='LaBarge' and firstname = 'Erin';",
                     "update data_persons set active=false where lastname='LaCreta' and firstname = 'Katherine';",
                     "update data_persons set active=false where lastname='LaFontaine' and firstname = 'Ethan';",
                     "update data_persons set active=false where lastname='Lewis' and firstname = 'Brandi';",
                     "update data_persons set active=false where lastname='Lin' and firstname = 'Jennifer';",
                     "update data_persons set active=false where lastname='Lin' and firstname = 'Mosi';",
                     "update data_persons set active=false where lastname='Loucks' and firstname = 'Samantha';",
                     "update data_persons set active=false where lastname='Louis' and firstname = 'Marissa';",
                     "update data_persons set active=false where lastname='Lutz' and firstname = 'Colleen';",
                     "update data_persons set active=false where lastname='Matthews' and firstname = 'Joseph';",
                     "update data_persons set active=false where lastname='McCarthy' and firstname = 'Alicia';",
                     "update data_persons set active=false where lastname='McCauley' and firstname = 'John';",
                     "update data_persons set active=false where lastname='McNamee' and firstname = 'Loretta';",
                     "update data_persons set active=false where lastname='Miller' and firstname = 'Clare';",
                     "update data_persons set active=false where lastname='Mitchell' and firstname = 'Tyler';",
                     "update data_persons set active=false where lastname='Naik' and firstname = 'Ankana';",
                     "update data_persons set active=false where lastname='Netzband (Cary)' and firstname = 'Rachel';",
                     "update data_persons set active=false where lastname='O'Keefe' and firstname = 'Kevin';",
                     "update data_persons set active=false where lastname='Orton' and firstname = 'Marie';",
                     "update data_persons set active=false where lastname='Pearson' and firstname = 'Seth';",
                     "update data_persons set active=false where lastname='Peterson' and firstname = 'Elizabeth';",
                     "update data_persons set active=false where lastname='Plummer' and firstname = 'Christopher';",
                     "update data_persons set active=false where lastname='Powers' and firstname = 'Andrew';",
                     "update data_persons set active=false where lastname='Rapisarda' and firstname = 'Ian';",
                     "update data_persons set active=false where lastname='Raveendranath' and firstname = 'Sanjay';",
                     "update data_persons set active=false where lastname='Roper' and firstname = 'Ayanna';",
                     "update data_persons set active=false where lastname='Rose' and firstname = 'Rozina';",
                     "update data_persons set active=false where lastname='Sanderson' and firstname = 'Erin';",
                     "update data_persons set active=false where lastname='Santiago' and firstname = 'Rezeily';",
                     "update data_persons set active=false where lastname='Schiraldi (Green)' and firstname = 'Cathleen';",
                     "update data_persons set active=false where lastname='Smith' and firstname = 'Nicole';",
                     "update data_persons set active=false where lastname='Smith (Pease)' and firstname = 'Amanda';",
                     "update data_persons set active=false where lastname='Spano' and firstname = 'Carissa';",
                     "update data_persons set active=false where lastname='Starkloff' and firstname = 'Naima';",
                     "update data_persons set active=false where lastname='Stone' and firstname = 'Kelly';",
                     "update data_persons set active=false where lastname='Stone' and firstname = 'Melissa';",
                     "update data_persons set active=false where lastname='Stroilo' and firstname = 'Viktoriia';",
                     "update data_persons set active=false where lastname='Toro' and firstname = 'Botros';",
                     "update data_persons set active=false where lastname='Trufanoff' and firstname = 'Dustin';",
                     "update data_persons set active=false where lastname='Upadhyay' and firstname = 'Maitreyi';",
                     "update data_persons set active=false where lastname='Uzzo' and firstname = 'Riley';",
                     "update data_persons set active=false where lastname='Valleau' and firstname = 'William';",
                     "update data_persons set active=false where lastname='VanLiew' and firstname = 'Nicholas';",
                     "update data_persons set active=false where lastname='Vare' and firstname = 'Ville';",
                     "update data_persons set active=false where lastname='Vedder-Drew' and firstname = 'Michelle';",
                     "update data_persons set active=false where lastname='Vera' and firstname = 'Kimberlie';",
                     "update data_persons set active=false where lastname='von Schnell' and firstname = 'Ahren';",
                     "update data_persons set active=false where lastname='Waldern' and firstname = 'Justin';",
                     "update data_persons set active=false where lastname='Welch' and firstname = 'Lorianne';",
                     "update data_persons set active=false where lastname='Williams' and firstname = 'Charmaine';",
                     "update data_persons set active=false where lastname='Winters' and firstname = 'Daniel';",
                     "update data_persons set active=false where lastname='Wong' and firstname = 'Jasmine';",
                     "update data_persons set active=false where lastname='Woo' and firstname = 'Ethan';",
                     "update data_persons set active=false where lastname='Zhang' and firstname = 'Hongxue';",
                     "update data_persons set active=false where lastname='Chan' and firstname = 'Hon';",
                     "update data_persons set active=false where lastname='Roberts' and firstname = 'Neketa';",
                     "update data_persons set active=false where lastname='Travis' and firstname = 'Jeffrey';"
                     ]

    return sqlstatements


# Create new code tables in new database on first use

def createroomtable():
    # Created only because Access won't permit multiple SQL statements in a query
    sqlstatements = ["insert into data_rooms values (1,1,'011',NULL,'BIO 011');",
                     "insert into data_rooms values (1,1,'BIO 001',NULL,NULL,'BIO 001 (ADMIN OFC)');",
                     "insert into data_rooms values (2,1,'BIO 001A',NULL,NULL,'BIO 001A (ADMIN)');",
                     "insert into data_rooms values (3,1,'BIO 001B',NULL,NULL,'BIO 001B (ADMIN OFC)');",
                     "insert into data_rooms values (4,1,'BIO 001C',NULL,NULL,'BIO 001C (ADMIN OFC)');",
                     "insert into data_rooms values (5,1,'BIO 001D',NULL,NULL,'BIO 001D (ADMIN OFC)');",
                     "insert into data_rooms values (6,1,'BIO 001E',NULL,NULL,'BIO 001E (ADMIN OFC)');",
                     "insert into data_rooms values (7,1,'BIO 001F',NULL,NULL,'BIO 001F (ADMIN OFC)');",
                     "insert into data_rooms values (8,1,'BIO 002D',NULL,NULL,'BIO 002D (ADMIN OFC)');",
                     "insert into data_rooms values (9,1,'BIO 003',NULL,NULL,'BIO 003 (JANITORS CLOSET)');",
                     "insert into data_rooms values (10,1,'BIO 007',NULL,NULL,'BIO 007 (VESTIBULE)');",
                     "insert into data_rooms values (11,1,'BIO 008',NULL,NULL,'BIO 008 (KEY SHOP STORAGE)');",
                     "insert into data_rooms values (12,1,'BIO 009',NULL,NULL,'BIO 009 (STORAGE)');",
                     "insert into data_rooms values (13,1,'BIO 010',NULL,NULL,'BIO 010 (RESEARCH LAB)');",
                     "insert into data_rooms values (14,1,'BIO 010A',NULL,NULL,'BIO 010A (MECHANICAL RM)');",
                     "insert into data_rooms values (15,1,'BIO 010B',NULL,NULL,'BIO 010B (STORAGE)');",
                     "insert into data_rooms values (16,1,'BIO 010C',NULL,NULL,'BIO 010C (PREP RM)');",
                     "insert into data_rooms values (17,1,'BIO 010D',NULL,NULL,'BIO 010D (ELECTRON MIC)');",
                     "insert into data_rooms values (18,1,'BIO 010E',NULL,NULL,'BIO 010E (RESEARCH LAB)');",
                     "insert into data_rooms values (19,1,'BIO 010F',NULL,NULL,'BIO 010F (CIRCULATION AREA)');",
                     "insert into data_rooms values (20,1,'BIO 011',NULL,NULL,'BIO 011 (RESEARCH LAB)');",
                     "insert into data_rooms values (21,1,'BIO 011A',NULL,NULL,'BIO 011A (RESEARCH LAB)');",
                     "insert into data_rooms values (22,1,'BIO 011B',NULL,NULL,'BIO 011B (RESEARCH LAB)');",
                     "insert into data_rooms values (23,1,'BIO 011C',NULL,NULL,'BIO 011C (DARK RM)');",
                     "insert into data_rooms values (24,1,'BIO 011D',NULL,NULL,'BIO 011D (RESEARCH LAB)');",
                     "insert into data_rooms values (25,1,'BIO 011E',NULL,NULL,'BIO 011E (CONFOCAL MICROSCO)');",
                     "insert into data_rooms values (26,1,'BIO 011F',NULL,NULL,'BIO 011F (LAB SERVICE)');",
                     "insert into data_rooms values (27,1,'BIO 012A',NULL,NULL,'BIO 012A (STORAGE)');",
                     "insert into data_rooms values (28,1,'BIO 012B',NULL,NULL,'BIO 012B (STORAGE)');",
                     "insert into data_rooms values (29,1,'BIO 012C',NULL,NULL,'BIO 012C (STORAGE)');",
                     "insert into data_rooms values (30,1,'BIO 012D',NULL,NULL,'BIO 012D (STORAGE)');",
                     "insert into data_rooms values (31,1,'BIO 013',NULL,NULL,'BIO 013 (RESEARCH LAB)');",
                     "insert into data_rooms values (32,1,'BIO 013A',NULL,NULL,'BIO 013A (DARK ROOM)');",
                     "insert into data_rooms values (33,1,'BIO 013B',NULL,NULL,'BIO 013B (RESEARCH LAB)');",
                     "insert into data_rooms values (34,1,'BIO 014',NULL,NULL,'BIO 014 (CLASS LAB PREP)');",
                     "insert into data_rooms values (35,1,'BIO 014A',NULL,NULL,'BIO 014A (STORAGE)');",
                     "insert into data_rooms values (36,1,'BIO 015',NULL,NULL,'BIO 015 (BIOCHEM CLASS LAB)');",
                     "insert into data_rooms values (37,1,'BIO 015A',NULL,NULL,'BIO 015A (CLASS LAB PREP)');",
                     "insert into data_rooms values (38,1,'BIO 016',NULL,NULL,'BIO 016 (CORRIDOR)');",
                     "insert into data_rooms values (39,1,'BIO 016A',NULL,NULL,'BIO 016A (ENTR VESTIBULE)');",
                     "insert into data_rooms values (40,1,'BIO 018',NULL,NULL,'BIO 018 (VESTIBULE)');",
                     "insert into data_rooms values (41,1,'BIO 019',NULL,NULL,'BIO 019 (PLUMBING)');",
                     "insert into data_rooms values (42,1,'BIO 020',NULL,NULL,'BIO 020 (CLASS LAB)');",
                     "insert into data_rooms values (43,1,'BIO 021A',NULL,NULL,'BIO 021A (CLASS LAB PREP)');",
                     "insert into data_rooms values (44,1,'BIO 021B',NULL,NULL,'BIO 021B (CLASS LAB PREP)');",
                     "insert into data_rooms values (45,1,'BIO 022',NULL,NULL,'BIO 022 (COOLER RM)');",
                     "insert into data_rooms values (46,1,'BIO 022A',NULL,NULL,'BIO 022A (CLASS SUPPORT LAB)');",
                     "insert into data_rooms values (47,1,'BIO 023',NULL,NULL,'BIO 023 (CELL/DEV BIO CLAS)');",
                     "insert into data_rooms values (48,1,'BIO 024',NULL,NULL,'BIO 024 (AQUARIUM LAB)');",
                     "insert into data_rooms values (49,1,'BIO 025',NULL,NULL,'BIO 025 (AQUARIUM LAB)');",
                     "insert into data_rooms values (50,1,'BIO 026',NULL,NULL,'BIO 026 (ELEV MACH RM)');",
                     "insert into data_rooms values (51,1,'BIO 028',NULL,NULL,'BIO 028 (VESTIBULE)');",
                     "insert into data_rooms values (52,1,'BIO 029',NULL,NULL,'BIO 029 (JANITORS CLOSET)');",
                     "insert into data_rooms values (53,1,'BIO 030',NULL,NULL,'BIO 030 (PLUMBING)');",
                     "insert into data_rooms values (54,1,'BIO 031',NULL,NULL,'BIO 031 (RESEARCH LAB)');",
                     "insert into data_rooms values (55,1,'BIO 032',NULL,NULL,'BIO 032 (FIRE SAFETY OFC)');",
                     "insert into data_rooms values (56,1,'BIO 032A',NULL,NULL,'BIO 032A (MEETING AREA)');",
                     "insert into data_rooms values (57,1,'BIO 033',NULL,NULL,'BIO 033 (FAC LAB OFC)');",
                     "insert into data_rooms values (58,1,'BIO 034',NULL,NULL,'BIO 034 (MECHANICAL RM)');",
                     "insert into data_rooms values (59,1,'BIO 035',NULL,NULL,'BIO 035 (RECEIVING AREA)');",
                     "insert into data_rooms values (60,1,'BIO 036',NULL,NULL,'BIO 036 (GEN BLDG SRVC)');",
                     "insert into data_rooms values (61,1,'BIO 037',NULL,NULL,'BIO 037 (RESEARCH LAB)');",
                     "insert into data_rooms values (62,1,'BIO 038',NULL,NULL,'BIO 038 (RESEARCH LAB)');",
                     "insert into data_rooms values (63,1,'BIO 039',NULL,NULL,'BIO 039 (RESEARCH LAB)');",
                     "insert into data_rooms values (64,1,'BIO 040',NULL,NULL,'BIO 040 (AUTOCLAVE RM)');",
                     "insert into data_rooms values (65,1,'BIO 040A',NULL,NULL,'BIO 040A (RESEARCH LAB)');",
                     "insert into data_rooms values (66,1,'BIO 041',NULL,NULL,'BIO 041 (RESEARCH LAB)');",
                     "insert into data_rooms values (67,1,'BIO 041A',NULL,NULL,'BIO 041A (RESEARCH LAB)');",
                     "insert into data_rooms values (68,1,'BIO 042',NULL,NULL,'BIO 042 (EQPT STOR RM)');",
                     "insert into data_rooms values (69,1,'BIO 042A',NULL,NULL,'BIO 042A (FACULTY LAB OFC)');",
                     "insert into data_rooms values (70,1,'BIO 042B',NULL,NULL,'BIO 042B (RESEARCH LAB)');",
                     "insert into data_rooms values (71,1,'BIO 042C',NULL,NULL,'BIO 042C (RESEARCH LAB)');",
                     "insert into data_rooms values (72,1,'BIO 043',NULL,NULL,'BIO 043 (RESEARCH LAB)');",
                     "insert into data_rooms values (73,1,'BIO 043A',NULL,NULL,'BIO 043A (ENTRY)');",
                     "insert into data_rooms values (74,1,'BIO 043B',NULL,NULL,'BIO 043B (LIGHT LOCK)');",
                     "insert into data_rooms values (75,1,'BIO 043C',NULL,NULL,'BIO 043C (DARK RM)');",
                     "insert into data_rooms values (76,1,'BIO 045',NULL,NULL,'BIO 045 (SERVICE DRIVE)');",
                     "insert into data_rooms values (77,1,'BIO 046',NULL,NULL,'BIO 046 (ELEC SWTCHBRD)');",
                     "insert into data_rooms values (78,1,'BIO 046A',NULL,NULL,'BIO 046A (COMMUNICATNS CLST)');",
                     "insert into data_rooms values (79,1,'BIO 048',NULL,NULL,'BIO 048 (RESEARCH LAB)');",
                     "insert into data_rooms values (80,1,'BIO 048A',NULL,NULL,'BIO 048A (RESEARCH LAB)');",
                     "insert into data_rooms values (81,1,'BIO 049',NULL,NULL,'BIO 049 (STORAGE)');",
                     "insert into data_rooms values (82,1,'BIO 049A',NULL,NULL,'BIO 049A (STORAGE)');",
                     "insert into data_rooms values (83,1,'BIO 050',NULL,NULL,'BIO 050 (RESEARCH LAB)');",
                     "insert into data_rooms values (84,1,'BIO 051',NULL,NULL,'BIO 051 (ENTRY)');",
                     "insert into data_rooms values (85,1,'BIO 052A',NULL,NULL,'BIO 052A (ENTRY)');",
                     "insert into data_rooms values (86,1,'BIO 052B',NULL,NULL,'BIO 052B (STORAGE)');",
                     "insert into data_rooms values (87,1,'BIO 053',NULL,NULL,'BIO 053 (FORENSICS GRAD OF)');",
                     "insert into data_rooms values (88,1,'BIO 054',NULL,NULL,'BIO 054 (FORENSICS GRAD OF)');",
                     "insert into data_rooms values (89,1,'BIO 055',NULL,NULL,'BIO 055 (FACULTY OFC)');",
                     "insert into data_rooms values (90,1,'BIO 056',NULL,NULL,'BIO 056 (PLUMBING)');",
                     "insert into data_rooms values (91,1,'BIO 057',NULL,NULL,'BIO 057 (RECEIVING AREA)');",
                     "insert into data_rooms values (92,1,'BIO 057A',NULL,NULL,'BIO 057A (MECHANICAL RM)');",
                     "insert into data_rooms values (93,1,'BIO 058',NULL,NULL,'BIO 058 (MECHANICAL RM)');",
                     "insert into data_rooms values (94,1,'BIO 102',NULL,NULL,'BIO 102 (VESTIBULE)');",
                     "insert into data_rooms values (95,1,'BIO 103',NULL,NULL,'BIO 103 (TOILET)');",
                     "insert into data_rooms values (96,1,'BIO 104',NULL,NULL,'BIO 104 (TOILET)');",
                     "insert into data_rooms values (97,1,'BIO 105',NULL,NULL,'BIO 105 (VESTIBULE)');",
                     "insert into data_rooms values (98,1,'BIO 106',NULL,NULL,'BIO 106 (TOILET)');",
                     "insert into data_rooms values (99,1,'BIO 107',NULL,NULL,'BIO 107 (TOILET)');",
                     "insert into data_rooms values (100,1,'BIO 108',NULL,NULL,'BIO 108 (FACULTY OFC)');",
                     "insert into data_rooms values (101,1,'BIO 109',NULL,NULL,'BIO 109 (INSTRUCTOR OFC)');",
                     "insert into data_rooms values (102,1,'BIO 110',NULL,NULL,'BIO 110 (INSTRUCTOR OFC)');",
                     "insert into data_rooms values (103,1,'BIO 111',NULL,NULL,'BIO 111 (INSTRUCTOR OFC)');",
                     "insert into data_rooms values (104,1,'BIO 112',NULL,NULL,'BIO 112 (INSTRUCTOR OFC)');",
                     "insert into data_rooms values (105,1,'BIO 113',NULL,NULL,'BIO 113 (FACULTY OFC)');",
                     "insert into data_rooms values (106,1,'BIO 114A',NULL,NULL,'BIO 114A (GEN BIO CLASS LAB)');",
                     "insert into data_rooms values (107,1,'BIO 114B',NULL,NULL,'BIO 114B (MED WASTE ROOM)');",
                     "insert into data_rooms values (108,1,'BIO 114C',NULL,NULL,'BIO 114C (DARK RM)');",
                     "insert into data_rooms values (109,1,'BIO 115',NULL,NULL,'BIO 115 (CORRIDOR)');",
                     "insert into data_rooms values (110,1,'BIO 115A',NULL,NULL,'BIO 115A (JANITORS CLOSET)');",
                     "insert into data_rooms values (111,1,'BIO 115B',NULL,NULL,'BIO 115B (COMMUNICATNS CLST)');",
                     "insert into data_rooms values (112,1,'BIO 117',NULL,NULL,'BIO 117 (JANITORS CLOSET)');",
                     "insert into data_rooms values (113,1,'BIO 118',NULL,NULL,'BIO 118 (CORRIDOR)');",
                     "insert into data_rooms values (114,1,'BIO 118A',NULL,NULL,'BIO 118A (JANITORS CLOSET)');",
                     "insert into data_rooms values (115,1,'BIO 118B',NULL,NULL,'BIO 118B (COMMUNICATNS CLST)');",
                     "insert into data_rooms values (116,1,'BIO 119',NULL,NULL,'BIO 119 (TA/GA MAILROOM)');",
                     "insert into data_rooms values (117,1,'BIO 119A',NULL,NULL,'BIO 119A (TA OFFICE)');",
                     "insert into data_rooms values (118,1,'BIO 119B',NULL,NULL,'BIO 119B (FACULTY OFC)');",
                     "insert into data_rooms values (119,1,'BIO 119C',NULL,NULL,'BIO 119C (FACULTY OFC)');",
                     "insert into data_rooms values (120,1,'BIO 119D',NULL,NULL,'BIO 119D (TA OFFICE)');",
                     "insert into data_rooms values (121,1,'BIO 119E',NULL,NULL,'BIO 119E (TA OFFICE)');",
                     "insert into data_rooms values (122,1,'BIO 122',NULL,NULL,'BIO 122 (MAIL RM)');",
                     "insert into data_rooms values (123,1,'BIO 123',NULL,NULL,'BIO 123 (FILE ROOM)');",
                     "insert into data_rooms values (124,1,'BIO 124',NULL,NULL,'BIO 124 (ASST TO CHAIR OFC)');",
                     "insert into data_rooms values (125,1,'BIO 125',NULL,NULL,'BIO 125 (FILE ROOM)');",
                     "insert into data_rooms values (126,1,'BIO 126',NULL,NULL,'BIO 126 (RECEPTION AREA)');",
                     "insert into data_rooms values (127,1,'BIO 127',NULL,NULL,'BIO 127 (SECRETARY OFC)');",
                     "insert into data_rooms values (128,1,'BIO 128',NULL,NULL,'BIO 128 (SUPPLY RM)');",
                     "insert into data_rooms values (129,1,'BIO 129',NULL,NULL,'BIO 129 (SUPPLY RM)');",
                     "insert into data_rooms values (130,1,'BIO 130',NULL,NULL,'BIO 130 (CONFERENCE RM)');",
                     "insert into data_rooms values (131,1,'BIO 131',NULL,NULL,'BIO 131 (CHAIR'S OFC)');",
                     "insert into data_rooms values (132,1,'BIO 132',NULL,NULL,'BIO 132 (VESTIBULE)');",
                     "insert into data_rooms values (133,1,'BIO 133',NULL,NULL,'BIO 133 (TOILET)');",
                     "insert into data_rooms values (134,1,'BIO 134',NULL,NULL,'BIO 134 (TOILET)');",
                     "insert into data_rooms values (135,1,'BIO 135',NULL,NULL,'BIO 135 (VESTIBULE)');",
                     "insert into data_rooms values (136,1,'BIO 136',NULL,NULL,'BIO 136 (TOILET)');",
                     "insert into data_rooms values (137,1,'BIO 137',NULL,NULL,'BIO 137 (TOILET)');",
                     "insert into data_rooms values (138,1,'BIO 140',NULL,NULL,'BIO 140 (VESTIBULE)');",
                     "insert into data_rooms values (139,1,'BIO 141',NULL,NULL,'BIO 141 (GEN BIO CLASS LAB)');",
                     "insert into data_rooms values (140,1,'BIO 142',NULL,NULL,'BIO 142 (CLASS LAB PREP)');",
                     "insert into data_rooms values (141,1,'BIO 143',NULL,NULL,'BIO 143 (RESEARCH LAB)');",
                     "insert into data_rooms values (142,1,'BIO 144',NULL,NULL,'BIO 144 (MOL BIO CLASS LAB)');",
                     "insert into data_rooms values (143,1,'BIO 144A',NULL,NULL,'BIO 144A (PREP RM)');",
                     "insert into data_rooms values (144,1,'BIO 144B',NULL,NULL,'BIO 144B (STORAGE RM)');",
                     "insert into data_rooms values (145,1,'BIO 145',NULL,NULL,'BIO 145 (GEN BIO CLASS LAB)');",
                     "insert into data_rooms values (146,1,'BIO 146',NULL,NULL,'BIO 146 (CLASS PREP RM)');",
                     "insert into data_rooms values (147,1,'BIO 147',NULL,NULL,'BIO 147 (PHOTO AREA)');",
                     "insert into data_rooms values (148,1,'BIO 148',NULL,NULL,'BIO 148 (RESEARCH LAB)');",
                     "insert into data_rooms values (149,1,'BIO 148A',NULL,NULL,'BIO 148A (FAC LAB OFC)');",
                     "insert into data_rooms values (150,1,'BIO 148B',NULL,NULL,'BIO 148B (RESEARCH LAB)');",
                     "insert into data_rooms values (151,1,'BIO 148C',NULL,NULL,'BIO 148C (PASSAGE)');",
                     "insert into data_rooms values (152,1,'BIO 149',NULL,NULL,'BIO 149 (LOBBY)');",
                     "insert into data_rooms values (153,1,'BIO 150',NULL,NULL,'BIO 150 (VESTIBULE)');",
                     "insert into data_rooms values (154,1,'BIO 151',NULL,NULL,'BIO 151 (RESEARCH LAB)');",
                     "insert into data_rooms values (155,1,'BIO 152',NULL,NULL,'BIO 152 (ELECTRONIC CLSSRM)');",
                     "insert into data_rooms values (156,1,'BIO 153',NULL,NULL,'BIO 153 (CLASS PREP RM)');",
                     "insert into data_rooms values (157,1,'BIO 154',NULL,NULL,'BIO 154 (GENERAL BIO CLASS)');",
                     "insert into data_rooms values (158,1,'BIO 155',NULL,NULL,'BIO 155 (GENERAL BIO CLASS)');",
                     "insert into data_rooms values (159,1,'BIO 156',NULL,NULL,'BIO 156 (CLASS PREP & STOR)');",
                     "insert into data_rooms values (160,1,'BIO 157',NULL,NULL,'BIO 157 (CLASS PREP RM)');",
                     "insert into data_rooms values (161,1,'BIO 158',NULL,NULL,'BIO 158 (ECOLOGY CLASS LAB)');",
                     "insert into data_rooms values (162,1,'BIO 160',NULL,NULL,'BIO 160 (VESTIBULE)');",
                     "insert into data_rooms values (163,1,'BIO 201',NULL,NULL,'BIO 201 (CORRIDOR)');",
                     "insert into data_rooms values (164,1,'BIO 201A',NULL,NULL,'BIO 201A (COMMUNICATNS CLST)');",
                     "insert into data_rooms values (165,1,'BIO 202',NULL,NULL,'BIO 202 (JANITORS CLOSET)');",
                     "insert into data_rooms values (166,1,'BIO 203',NULL,NULL,'BIO 203 (FILE ROOM)');",
                     "insert into data_rooms values (167,1,'BIO 206',NULL,NULL,'BIO 206 (PREP RM)');",
                     "insert into data_rooms values (168,1,'BIO 209',NULL,NULL,'BIO 209 (FAC LAB OFC)');",
                     "insert into data_rooms values (169,1,'BIO 210',NULL,NULL,'BIO 210 (FACULTY OFC)');",
                     "insert into data_rooms values (170,1,'BIO 211',NULL,NULL,'BIO 211 (FACULTY OFC)');",
                     "insert into data_rooms values (171,1,'BIO 212',NULL,NULL,'BIO 212 (FACULTY LAB OFC)');",
                     "insert into data_rooms values (172,1,'BIO 212A',NULL,NULL,'BIO 212A (FACULTY LAB OFC)');",
                     "insert into data_rooms values (173,1,'BIO 213',NULL,NULL,'BIO 213 (FACULTY OFC)');",
                     "insert into data_rooms values (174,1,'BIO 214',NULL,NULL,'BIO 214 (TA/GA OFC)');",
                     "insert into data_rooms values (175,1,'BIO 215',NULL,NULL,'BIO 215 (FAC LAB OFC)');",
                     "insert into data_rooms values (176,1,'BIO 216',NULL,NULL,'BIO 216 (FAC LAB OFC)');",
                     "insert into data_rooms values (177,1,'BIO 217',NULL,NULL,'BIO 217 (EEB TA/GA OFC)');",
                     "insert into data_rooms values (178,1,'BIO 218',NULL,NULL,'BIO 218 (CORRIDOR)');",
                     "insert into data_rooms values (179,1,'BIO 220',NULL,NULL,'BIO 220 (JANITORS CLOSET)');",
                     "insert into data_rooms values (180,1,'BIO 221',NULL,NULL,'BIO 221 (CONFERENCE RM)');",
                     "insert into data_rooms values (181,1,'BIO 222',NULL,NULL,'BIO 222 (FORENSICS LAB)');",
                     "insert into data_rooms values (182,1,'BIO 222A',NULL,NULL,'BIO 222A (STORAGE)');",
                     "insert into data_rooms values (183,1,'BIO 222B',NULL,NULL,'BIO 222B (STORAGE)');",
                     "insert into data_rooms values (184,1,'BIO 222C',NULL,NULL,'BIO 222C (ENTRY)');",
                     "insert into data_rooms values (185,1,'BIO 224',NULL,NULL,'BIO 224 (STORAGE)');",
                     "insert into data_rooms values (186,1,'BIO 225',NULL,NULL,'BIO 225 (INSTRUCTOR OFC)');",
                     "insert into data_rooms values (187,1,'BIO 227',NULL,NULL,'BIO 227 (RECEPTION AREA)');",
                     "insert into data_rooms values (188,1,'BIO 228',NULL,NULL,'BIO 228 (TA OFC)');",
                     "insert into data_rooms values (189,1,'BIO 229',NULL,NULL,'BIO 229 (INSTRUCTOR OFC)');",
                     "insert into data_rooms values (190,1,'BIO 230',NULL,NULL,'BIO 230 (FACULTY LAB OFC)');",
                     "insert into data_rooms values (191,1,'BIO 231',NULL,NULL,'BIO 231 (TA OFC)');",
                     "insert into data_rooms values (192,1,'BIO 232',NULL,NULL,'BIO 232 (FORENSICS STUDENT)');",
                     "insert into data_rooms values (193,1,'BIO 233',NULL,NULL,'BIO 233 (VESTIBULE)');",
                     "insert into data_rooms values (194,1,'BIO 234',NULL,NULL,'BIO 234 (TOILET)');",
                     "insert into data_rooms values (195,1,'BIO 235',NULL,NULL,'BIO 235 (TOILET)');",
                     "insert into data_rooms values (196,1,'BIO 236',NULL,NULL,'BIO 236 (VESTIBULE)');",
                     "insert into data_rooms values (197,1,'BIO 237',NULL,NULL,'BIO 237 (TOILET)');",
                     "insert into data_rooms values (198,1,'BIO 238',NULL,NULL,'BIO 238 (TOILET)');",
                     "insert into data_rooms values (199,1,'BIO 239',NULL,NULL,'BIO 239 (JANITORS CLOSET)');",
                     "insert into data_rooms values (200,1,'BIO 240',NULL,NULL,'BIO 240 (CORRIDOR)');",
                     "insert into data_rooms values (201,1,'BIO 240A',NULL,NULL,'BIO 240A (COMMUNICATNS CLST)');",
                     "insert into data_rooms values (202,1,'BIO 241',NULL,NULL,'BIO 241 (MICRO CLASS LAB)');",
                     "insert into data_rooms values (203,1,'BIO 241A',NULL,NULL,'BIO 241A (CLASS SUPPORT LAB)');",
                     "insert into data_rooms values (204,1,'BIO 242',NULL,NULL,'BIO 242 (CLASS SUPPORT LAB)');",
                     "insert into data_rooms values (205,1,'BIO 242A',NULL,NULL,'BIO 242A (COLD RM)');",
                     "insert into data_rooms values (206,1,'BIO 243',NULL,NULL,'BIO 243 (CLASS SUPPORT LAB)');",
                     "insert into data_rooms values (207,1,'BIO 243A',NULL,NULL,'BIO 243A (CLASS SUPPORT LAB)');",
                     "insert into data_rooms values (208,1,'BIO 244',NULL,NULL,'BIO 244 (FORENSIC CLASS LA)');",
                     "insert into data_rooms values (209,1,'BIO 245',NULL,NULL,'BIO 245 (CELL/DEV BIO CLAS)');",
                     "insert into data_rooms values (210,1,'BIO 246',NULL,NULL,'BIO 246 (CLASS SUPPORT LAB)');",
                     "insert into data_rooms values (211,1,'BIO 247',NULL,NULL,'BIO 247 (CLASS SUPPORT LAB)');",
                     "insert into data_rooms values (212,1,'BIO 248A',NULL,NULL,'BIO 248A (SEMINAR RM)');",
                     "insert into data_rooms values (213,1,'BIO 248B',NULL,NULL,'BIO 248B (SEMINAR RM)');",
                     "insert into data_rooms values (214,1,'BIO 249',NULL,NULL,'BIO 249 (KITCHENETTE)');",
                     "insert into data_rooms values (215,1,'BIO 250',NULL,NULL,'BIO 250 (EQP STOR RM)');",
                     "insert into data_rooms values (216,1,'BIO 251',NULL,NULL,'BIO 251 (GRAD ASST)');",
                     "insert into data_rooms values (217,1,'BIO 252',NULL,NULL,'BIO 252 (PHYSIO LAB)');",
                     "insert into data_rooms values (218,1,'BIO 253',NULL,NULL,'BIO 253 (RESEARCH LAB)');",
                     "insert into data_rooms values (219,1,'BIO 253A',NULL,NULL,'BIO 253A (FACULTY LAB OFC)');",
                     "insert into data_rooms values (220,1,'BIO 253B',NULL,NULL,'BIO 253B (RESEARCH LAB)');",
                     "insert into data_rooms values (221,1,'BIO 253C',NULL,NULL,'BIO 253C (FACULTY OFC)');",
                     "insert into data_rooms values (222,1,'BIO 254',NULL,NULL,'BIO 254 (CLASS LAB PREP/ST)');",
                     "insert into data_rooms values (223,1,'BIO 254A',NULL,NULL,'BIO 254A (ANATOMY INSTRUCTO)');",
                     "insert into data_rooms values (224,1,'BIO 254B',NULL,NULL,'BIO 254B (CLASS LAB PREP)');",
                     "insert into data_rooms values (225,1,'BIO 256',NULL,NULL,'BIO 256 (ANATOMY CLASS LAB)');",
                     "insert into data_rooms values (226,1,'BIO 301',NULL,NULL,'BIO 301 (CORRIDOR)');",
                     "insert into data_rooms values (227,1,'BIO 301A',NULL,NULL,'BIO 301A (COMMUNICATNS CLST)');",
                     "insert into data_rooms values (228,1,'BIO 302',NULL,NULL,'BIO 302 (JANITORS CLOSET)');",
                     "insert into data_rooms values (229,1,'BIO 305',NULL,NULL,'BIO 305 (RESEARCH LAB)');",
                     "insert into data_rooms values (230,1,'BIO 309',NULL,NULL,'BIO 309 (GRAD OFC)');",
                     "insert into data_rooms values (231,1,'BIO 309A',NULL,NULL,'BIO 309A (GRAD OFC)');",
                     "insert into data_rooms values (232,1,'BIO 310',NULL,NULL,'BIO 310 (FACULTY OFC)');",
                     "insert into data_rooms values (233,1,'BIO 311',NULL,NULL,'BIO 311 (RESEARCH LAB)');",
                     "insert into data_rooms values (234,1,'BIO 312',NULL,NULL,'BIO 312 (RESEARCH LAB)');",
                     "insert into data_rooms values (235,1,'BIO 313',NULL,NULL,'BIO 313 (COOLER RM)');",
                     "insert into data_rooms values (236,1,'BIO 314',NULL,NULL,'BIO 314 (RESEARCH LAB)');",
                     "insert into data_rooms values (237,1,'BIO 315',NULL,NULL,'BIO 315 (VESTIBULE)');",
                     "insert into data_rooms values (238,1,'BIO 316',NULL,NULL,'BIO 316 (COOLER RM)');",
                     "insert into data_rooms values (239,1,'BIO 317',NULL,NULL,'BIO 317 (RESEARCH LAB)');",
                     "insert into data_rooms values (240,1,'BIO 318',NULL,NULL,'BIO 318 (RESEARCH LAB)');",
                     "insert into data_rooms values (241,1,'BIO 319',NULL,NULL,'BIO 319 (CORRIDOR)');",
                     "insert into data_rooms values (242,1,'BIO 321',NULL,NULL,'BIO 321 (JANITORS CLOSET)');",
                     "insert into data_rooms values (243,1,'BIO 322',NULL,NULL,'BIO 322 (RESEARCH LAB)');",
                     "insert into data_rooms values (244,1,'BIO 322A',NULL,NULL,'BIO 322A (RESEARCH LAB)');",
                     "insert into data_rooms values (245,1,'BIO 322B',NULL,NULL,'BIO 322B (MICROSCOPE RM)');",
                     "insert into data_rooms values (246,1,'BIO 323',NULL,NULL,'BIO 323 (RESEARCH LAB)');",
                     "insert into data_rooms values (247,1,'BIO 324',NULL,NULL,'BIO 324 (GRAD OFC)');",
                     "insert into data_rooms values (248,1,'BIO 325',NULL,NULL,'BIO 325 (FACULTY OFC)');",
                     "insert into data_rooms values (249,1,'BIO 326',NULL,NULL,'BIO 326 (FACULTY OFC)');",
                     "insert into data_rooms values (250,1,'BIO 326A',NULL,NULL,'BIO 326A (FACULTY OFC)');",
                     "insert into data_rooms values (251,1,'BIO 327',NULL,NULL,'BIO 327 (GRAD OFC)');",
                     "insert into data_rooms values (252,1,'BIO 327A',NULL,NULL,'BIO 327A (GRAD OFC)');",
                     "insert into data_rooms values (253,1,'BIO 328',NULL,NULL,'BIO 328 (GRAD OFC)');",
                     "insert into data_rooms values (254,1,'BIO 328A',NULL,NULL,'BIO 328A (GRAD OFC)');",
                     "insert into data_rooms values (255,1,'BIO 329',NULL,NULL,'BIO 329 (FACULTY OFC)');",
                     "insert into data_rooms values (256,1,'BIO 330',NULL,NULL,'BIO 330 (VESTIBULE)');",
                     "insert into data_rooms values (257,1,'BIO 331',NULL,NULL,'BIO 331 (TOILET)');",
                     "insert into data_rooms values (258,1,'BIO 332',NULL,NULL,'BIO 332 (TOILET)');",
                     "insert into data_rooms values (259,1,'BIO 333',NULL,NULL,'BIO 333 (VESTIBULE)');",
                     "insert into data_rooms values (260,1,'BIO 334',NULL,NULL,'BIO 334 (TOILET)');",
                     "insert into data_rooms values (261,1,'BIO 335',NULL,NULL,'BIO 335 (TOILET)');",
                     "insert into data_rooms values (262,1,'BIO 336',NULL,NULL,'BIO 336 (JANITORS CLOSET)');",
                     "insert into data_rooms values (263,1,'BIO 337',NULL,NULL,'BIO 337 (CORRIDOR)');",
                     "insert into data_rooms values (264,1,'BIO 337A',NULL,NULL,'BIO 337A (COMMUNICATNS CLST)');",
                     "insert into data_rooms values (265,1,'BIO 338',NULL,NULL,'BIO 338 (EQUIPMENT RM)');",
                     "insert into data_rooms values (266,1,'BIO 338A',NULL,NULL,'BIO 338A (RESEARCH LAB)');",
                     "insert into data_rooms values (267,1,'BIO 338B',NULL,NULL,'BIO 338B (RESEARCH LAB)');",
                     "insert into data_rooms values (268,1,'BIO 338C',NULL,NULL,'BIO 338C (RESEARCH LAB)');",
                     "insert into data_rooms values (269,1,'BIO 338D',NULL,NULL,'BIO 338D (FACULTY OFC)');",
                     "insert into data_rooms values (270,1,'BIO 339',NULL,NULL,'BIO 339 (COOLER RM)');",
                     "insert into data_rooms values (271,1,'BIO 340A',NULL,NULL,'BIO 340A (RESEARCH LAB)');",
                     "insert into data_rooms values (272,1,'BIO 340B',NULL,NULL,'BIO 340B (RESEARCH LAB)');",
                     "insert into data_rooms values (273,1,'BIO 340C',NULL,NULL,'BIO 340C (RESEARCH LAB)');",
                     "insert into data_rooms values (274,1,'BIO 341',NULL,NULL,'BIO 341 (RESEARCH LAB)');",
                     "insert into data_rooms values (275,1,'BIO 341A',NULL,NULL,'BIO 341A (RESEARCH LAB)');",
                     "insert into data_rooms values (276,1,'BIO 341B',NULL,NULL,'BIO 341B (RESEARCH LAB)');",
                     "insert into data_rooms values (277,1,'BIO 342',NULL,NULL,'BIO 342 (RESEARCH LAB)');",
                     "insert into data_rooms values (278,1,'BIO 342A',NULL,NULL,'BIO 342A (DARK RM)');",
                     "insert into data_rooms values (279,1,'BIO 342B',NULL,NULL,'BIO 342B (INSTRUMENT RM)');",
                     "insert into data_rooms values (280,1,'BIO 343',NULL,NULL,'BIO 343 (RESEARCH LAB)');",
                     "insert into data_rooms values (281,1,'BIO 344',NULL,NULL,'BIO 344 (RESEARCH LAB)');",
                     "insert into data_rooms values (282,1,'BIO 344A',NULL,NULL,'BIO 344A (RESEARCH LAB)');",
                     "insert into data_rooms values (283,1,'BIO 345',NULL,NULL,'BIO 345 (RESEARCH LAB)');",
                     "insert into data_rooms values (284,1,'BIO 346',NULL,NULL,'BIO 346 (RESEARCH LAB)');",
                     "insert into data_rooms values (285,1,'BIO 346A',NULL,NULL,'BIO 346A (EQUIPMENT STOR RM)');",
                     "insert into data_rooms values (286,1,'BIO 346B',NULL,NULL,'BIO 346B (EQUIPMENT STOR RM)');",
                     "insert into data_rooms values (287,1,'BIO 347',NULL,NULL,'BIO 347 (RESEARCH LAB)');",
                     "insert into data_rooms values (288,1,'BIO 348',NULL,NULL,'BIO 348 (RESEARCH LAB)');",
                     "insert into data_rooms values (289,1,'BIO 349',NULL,NULL,'BIO 349 (RESEARCH LAB)');",
                     "insert into data_rooms values (290,1,'BIO 349A',NULL,NULL,'BIO 349A (RESEARCH LAB)');",
                     "insert into data_rooms values (291,1,'BIO 350',NULL,NULL,'BIO 350 (RES FACILITY SRVC)');",
                     "insert into data_rooms values (292,1,'BIO 351',NULL,NULL,'BIO 351 (INCUBATOR)');",
                     "insert into data_rooms values (293,1,'BIO 352',NULL,NULL,'BIO 352 (INCUBATOR)');",
                     "insert into data_rooms values (294,1,'BIO 353',NULL,NULL,'BIO 353 (RESEARCH LAB)');",
                     "insert into data_rooms values (295,1,'BIO 353A',NULL,NULL,'BIO 353A (RESEARCH LAB SRVC)');",
                     "insert into data_rooms values (296,1,'BIO 354A',NULL,NULL,'BIO 354A (FACULTY LAB OFC)');",
                     "insert into data_rooms values (297,1,'BIO 354B',NULL,NULL,'BIO 354B (RESEARCH LAB)');",
                     "insert into data_rooms values (298,1,'BIO 355',NULL,NULL,'BIO 355 (RESEARCH LAB (MULTIPLE PI))');",
                     "insert into data_rooms values (299,1,'BIO 355A',NULL,NULL,'BIO 355A (RESEARCH LAB)');",
                     "insert into data_rooms values (300,1,'BIO 355B',NULL,NULL,'BIO 355B (RESEARCH LAB)');",
                     "insert into data_rooms values (301,1,'BIO 401',NULL,NULL,'BIO 401 (MECHANICAL RM)');",
                     "insert into data_rooms values (400,2,'LSRB 1000',NULL,NULL,'LSRB 1000 (VESTIBULE)');",
                     "insert into data_rooms values (401,2,'LSRB 1001',NULL,NULL,'LSRB 1001 (FLAMSTOR/DISP)');",
                     "insert into data_rooms values (402,2,'LSRB 1002',NULL,NULL,'LSRB 1002 (CHEM STORAGE)');",
                     "insert into data_rooms values (403,2,'LSRB 1003',NULL,NULL,'LSRB 1003 (WARM ROOM)');",
                     "insert into data_rooms values (404,2,'LSRB 1004',NULL,NULL,'LSRB 1004 (BIIOHAZ WASTE STO)');",
                     "insert into data_rooms values (405,2,'LSRB 1005',NULL,NULL,'LSRB 1005 (HAZARDOUS WASTE)');",
                     "insert into data_rooms values (406,2,'LSRB 1006',NULL,NULL,'LSRB 1006 (RADIOACTIVE WASTE)');",
                     "insert into data_rooms values (407,2,'LSRB 1007',NULL,NULL,'LSRB 1007 (GENERAL STORAGE)');",
                     "insert into data_rooms values (408,2,'LSRB 1008',NULL,NULL,'LSRB 1008 (CENT DOCK CTRL)');",
                     "insert into data_rooms values (409,2,'LSRB 1009',NULL,NULL,'LSRB 1009 (COLD RM)');",
                     "insert into data_rooms values (410,2,'LSRB 1010',NULL,NULL,'LSRB 1010 (CONFERENCE RM)');",
                     "insert into data_rooms values (411,2,'LSRB 1011',NULL,NULL,'LSRB 1011 (DECON GLASSWASH)');",
                     "insert into data_rooms values (412,2,'LSRB 1012',NULL,NULL,'LSRB 1012 (WORKSTATION)');",
                     "insert into data_rooms values (413,2,'LSRB 1013',NULL,NULL,'LSRB 1013 (MOLEC BIO CORE)');",
                     "insert into data_rooms values (414,2,'LSRB 1014',NULL,NULL,'LSRB 1014 (DNA LABORATORY)');",
                     "insert into data_rooms values (415,2,'LSRB 1015',NULL,NULL,'LSRB 1015 (EQUIPMENT STORAGE)');",
                     "insert into data_rooms values (416,2,'LSRB 1017',NULL,NULL,'LSRB 1017 (CELL/MICROCHP)');",
                     "insert into data_rooms values (417,2,'LSRB 1018',NULL,NULL,'LSRB 1018 (CELL/MICROCHP)');",
                     "insert into data_rooms values (418,2,'LSRB 1019',NULL,NULL,'LSRB 1019 (WARM ROOM)');",
                     "insert into data_rooms values (419,2,'LSRB 1020',NULL,NULL,'LSRB 1020 (COLD ROOM)');",
                     "insert into data_rooms values (420,2,'LSRB 1021',NULL,NULL,'LSRB 1021 (VENDING AREA)');",
                     "insert into data_rooms values (421,2,'LSRB 1022',NULL,NULL,'LSRB 1022 (DNA SEQUENCING)');",
                     "insert into data_rooms values (422,2,'LSRB 1023',NULL,NULL,'LSRB 1023 (PREP ROOM)');",
                     "insert into data_rooms values (423,2,'LSRB 1024',NULL,NULL,'LSRB 1024 (CENT HSKPG)');",
                     "insert into data_rooms values (424,2,'LSRB 1025',NULL,NULL,'LSRB 1025 (LOADING DOCK)');",
                     "insert into data_rooms values (425,2,'LSRB 1026',NULL,NULL,'LSRB 1026 (GENERATOR)');",
                     "insert into data_rooms values (426,2,'LSRB 1027',NULL,NULL,'LSRB 1027 (TELCOM CLOSET)');",
                     "insert into data_rooms values (427,2,'LSRB 1028',NULL,NULL,'LSRB 1028 (ELECTRIC RM)');",
                     "insert into data_rooms values (428,2,'LSRB 1029',NULL,NULL,'LSRB 1029 (AUTOCLAVE)');",
                     "insert into data_rooms values (429,2,'LSRB 1030',NULL,NULL,'LSRB 1030 (DARK RM)');",
                     "insert into data_rooms values (430,2,'LSRB 1031',NULL,NULL,'LSRB 1031 (SUPPORT LAB A)');",
                     "insert into data_rooms values (431,2,'LSRB 1032',NULL,NULL,'LSRB 1032 (AQUARIUM)');",
                     "insert into data_rooms values (432,2,'LSRB 1033',NULL,NULL,'LSRB 1033 (RESEARCH LAB)');",
                     "insert into data_rooms values (433,2,'LSRB 1034',NULL,NULL,'LSRB 1034 (SUPPORT LAB C)');",
                     "insert into data_rooms values (434,2,'LSRB 1035',NULL,NULL,'LSRB 1035 (SUPPORT LAB D)');",
                     "insert into data_rooms values (435,2,'LSRB 1036',NULL,NULL,'LSRB 1036 (WORKSTATION)');",
                     "insert into data_rooms values (436,2,'LSRB 1037',NULL,NULL,'LSRB 1037 (FACULTY OFC)');",
                     "insert into data_rooms values (437,2,'LSRB 1038',NULL,NULL,'LSRB 1038 (FACULTY OFC)');",
                     "insert into data_rooms values (438,2,'LSRB 1039',NULL,NULL,'LSRB 1039 (FACULTY OFC)');",
                     "insert into data_rooms values (439,2,'LSRB 1040',NULL,NULL,'LSRB 1040 (SUPPORT LAB E)');",
                     "insert into data_rooms values (440,2,'LSRB 1041',NULL,NULL,'LSRB 1041 (SUPPORT LAB A)');",
                     "insert into data_rooms values (441,2,'LSRB 1042',NULL,NULL,'LSRB 1042 (RESEARCH LAB)');",
                     "insert into data_rooms values (442,2,'LSRB 1043',NULL,NULL,'LSRB 1043 (RESEARCH LAB)');",
                     "insert into data_rooms values (443,2,'LSRB 1044',NULL,NULL,'LSRB 1044 (RESEARCH LAB)');",
                     "insert into data_rooms values (444,2,'LSRB 1045',NULL,NULL,'LSRB 1045 (RESEARCH LAB)');",
                     "insert into data_rooms values (445,2,'LSRB 1046',NULL,NULL,'LSRB 1046 (RESEARCH LAB)');",
                     "insert into data_rooms values (446,2,'LSRB 1047',NULL,NULL,'LSRB 1047 (SUPPORT LAB E)');",
                     "insert into data_rooms values (447,2,'LSRB 1048',NULL,NULL,'LSRB 1048 (SUPPORT LAB A)');",
                     "insert into data_rooms values (448,2,'LSRB 1049',NULL,NULL,'LSRB 1049 (RESEARCH LAB)');",
                     "insert into data_rooms values (449,2,'LSRB 1050',NULL,NULL,'LSRB 1050 (AQUARIUM)');",
                     "insert into data_rooms values (450,2,'LSRB 1051',NULL,NULL,'LSRB 1051 (RESEARCH LAB)');",
                     "insert into data_rooms values (451,2,'LSRB 1052',NULL,NULL,'LSRB 1052 (SUPPORT LAB C)');",
                     "insert into data_rooms values (452,2,'LSRB 1053',NULL,NULL,'LSRB 1053 (SUPPORT LAB D)');",
                     "insert into data_rooms values (453,2,'LSRB 1054',NULL,NULL,'LSRB 1054 (SUPPORT LAB E)');",
                     "insert into data_rooms values (454,2,'LSRB 1055',NULL,NULL,'LSRB 1055 (SUPPORT LAB A)');",
                     "insert into data_rooms values (455,2,'LSRB 1056',NULL,NULL,'LSRB 1056 (RESEARCH LAB)');",
                     "insert into data_rooms values (456,2,'LSRB 1057',NULL,NULL,'LSRB 1057 (WORKSTATION)');",
                     "insert into data_rooms values (457,2,'LSRB 1058',NULL,NULL,'LSRB 1058 (FACULTY OFC)');",
                     "insert into data_rooms values (458,2,'LSRB 1059',NULL,NULL,'LSRB 1059 (FACULTY OFC)');",
                     "insert into data_rooms values (459,2,'LSRB 1060',NULL,NULL,'LSRB 1060 (FACULTY OFC)');",
                     "insert into data_rooms values (460,2,'LSRB 1061',NULL,NULL,'LSRB 1061 (COLD RM)');",
                     "insert into data_rooms values (461,2,'LSRB 1063',NULL,NULL,'LSRB 1063 (ADMIN OFC)');",
                     "insert into data_rooms values (462,2,'LSRB 1065',NULL,NULL,'LSRB 1065 (FACULTY OFC)');",
                     "insert into data_rooms values (463,2,'LSRB 1067',NULL,NULL,'LSRB 1067 (COLD RM)');",
                     "insert into data_rooms values (464,2,'LSRB 1068',NULL,NULL,'LSRB 1068 (ADMIN SUPT/SEC)');",
                     "insert into data_rooms values (465,2,'LSRB 1069',NULL,NULL,'LSRB 1069 (EQUIPMENT RM)');",
                     "insert into data_rooms values (466,2,'LSRB 1070',NULL,NULL,'LSRB 1070 (RESEARCH LAB)');",
                     "insert into data_rooms values (467,2,'LSRB 1071',NULL,NULL,'LSRB 1071 (RESEARCH LAB)');",
                     "insert into data_rooms values (468,2,'LSRB 1072',NULL,NULL,'LSRB 1072 (TECH ASST)');",
                     "insert into data_rooms values (469,2,'LSRB 1073',NULL,NULL,'LSRB 1073 (SPEC PURP LAB)');",
                     "insert into data_rooms values (470,2,'LSRB 1074',NULL,NULL,'LSRB 1074 (RESEARCH LAB)');",
                     "insert into data_rooms values (471,2,'LSRB 1075',NULL,NULL,'LSRB 1075 (SUPPORT LAB A)');",
                     "insert into data_rooms values (472,2,'LSRB 1076',NULL,NULL,'LSRB 1076 (FACULTY OFC)');",
                     "insert into data_rooms values (473,2,'LSRB 1077',NULL,NULL,'LSRB 1077 (SUPPORT AREA)');",
                     "insert into data_rooms values (474,2,'LSRB 1078',NULL,NULL,'LSRB 1078 (SUPPORT LAB A)');",
                     "insert into data_rooms values (475,2,'LSRB 1079',NULL,NULL,'LSRB 1079 (RESEARCH LAB)');",
                     "insert into data_rooms values (476,2,'LSRB 1080',NULL,NULL,'LSRB 1080 (TEA ROOM)');",
                     "insert into data_rooms values (477,2,'LSRB 1081',NULL,NULL,'LSRB 1081 (BIOINFORMATICS)');",
                     "insert into data_rooms values (478,2,'LSRB 1082',NULL,NULL,'LSRB 1082 (TEA ROOM)');",
                     "insert into data_rooms values (479,2,'LSRB 1083',NULL,NULL,'LSRB 1083 (SUPPORT LAB A)');",
                     "insert into data_rooms values (480,2,'LSRB 1084',NULL,NULL,'LSRB 1084 (STORAGE)');",
                     "insert into data_rooms values (481,2,'LSRB 1085',NULL,NULL,'LSRB 1085 (ADMIN OFC)');",
                     "insert into data_rooms values (482,2,'LSRB 1086',NULL,NULL,'LSRB 1086 (FACULTY OFC)');",
                     "insert into data_rooms values (483,2,'LSRB 1087',NULL,NULL,'LSRB 1087 (SPEC PURP LAB)');",
                     "insert into data_rooms values (484,2,'LSRB 1088',NULL,NULL,'LSRB 1088 (LABORATORY)');",
                     "insert into data_rooms values (485,2,'LSRB 1089',NULL,NULL,'LSRB 1089 (SPEC PURP LAB)');",
                     "insert into data_rooms values (486,2,'LSRB 1090',NULL,NULL,'LSRB 1090 (JANITORS CLOSET)');",
                     "insert into data_rooms values (487,2,'LSRB 1091',NULL,NULL,'LSRB 1091 (SUPPORT LAB 3)');",
                     "insert into data_rooms values (488,2,'LSRB 1092',NULL,NULL,'LSRB 1092 (SUPPORT LAB E)');",
                     "insert into data_rooms values (489,2,'LSRB 1093',NULL,NULL,'LSRB 1093 (EQUIPMENT RM)');",
                     "insert into data_rooms values (490,2,'LSRB 1094',NULL,NULL,'LSRB 1094 (TISSUE CULTURE)');",
                     "insert into data_rooms values (491,2,'LSRB 1095',NULL,NULL,'LSRB 1095 (TISSUE CULTURE)');",
                     "insert into data_rooms values (492,2,'LSRB 1096',NULL,NULL,'LSRB 1096 (TISSUE CULTURE)');",
                     "insert into data_rooms values (493,2,'LSRB 1097',NULL,NULL,'LSRB 1097 (TISSUE CULTURE)');",
                     "insert into data_rooms values (494,2,'LSRB 1098',NULL,NULL,'LSRB 1098 (WARM ROOM)');",
                     "insert into data_rooms values (495,2,'LSRB 1099',NULL,NULL,'LSRB 1099 (WARM ROOM)');",
                     "insert into data_rooms values (496,2,'LSRB 1100',NULL,NULL,'LSRB 1100 (COLD ROOM)');",
                     "insert into data_rooms values (497,2,'LSRB 1101',NULL,NULL,'LSRB 1101 (AUTOCLAVE)');",
                     "insert into data_rooms values (498,2,'LSRB 1102',NULL,NULL,'LSRB 1102 (RESEARCH LAB)');",
                     "insert into data_rooms values (499,2,'LSRB 1103',NULL,NULL,'LSRB 1103 (RESEARCH LAB)');",
                     "insert into data_rooms values (500,2,'LSRB 1104',NULL,NULL,'LSRB 1104 (RESEARCH LAB)');",
                     "insert into data_rooms values (501,2,'LSRB 1105',NULL,NULL,'LSRB 1105 (WORKSTATION)');",
                     "insert into data_rooms values (502,2,'LSRB 1106',NULL,NULL,'LSRB 1106 (WORKSTATION)');",
                     "insert into data_rooms values (503,2,'LSRB 1107',NULL,NULL,'LSRB 1107 (OFFICE)');",
                     "insert into data_rooms values (504,2,'LSRB 1108',NULL,NULL,'LSRB 1108 (FACULTY OFC)');",
                     "insert into data_rooms values (505,2,'LSRB 1109',NULL,NULL,'LSRB 1109 (FACULTY OFC)');",
                     "insert into data_rooms values (506,2,'LSRB 1110',NULL,NULL,'LSRB 1110 (INSTRUMENT RM)');",
                     "insert into data_rooms values (507,2,'LSRB 1111',NULL,NULL,'LSRB 1111 (RESEARCH LAB)');",
                     "insert into data_rooms values (508,2,'LSRB 1112',NULL,NULL,'LSRB 1112 (LASER INSTRUMENT)');",
                     "insert into data_rooms values (509,2,'LSRB 1113',NULL,NULL,'LSRB 1113 (RESEARCH OFC)');",
                     "insert into data_rooms values (510,2,'LSRB 1114',NULL,NULL,'LSRB 1114 (RESEARCH LAB)');",
                     "insert into data_rooms values (511,2,'LSRB 1115',NULL,NULL,'LSRB 1115 (RESEARCH LAB)');",
                     "insert into data_rooms values (512,2,'LSRB 1116',NULL,NULL,'LSRB 1116 (RESEARCH LAB)');",
                     "insert into data_rooms values (513,2,'LSRB 1117',NULL,NULL,'LSRB 1117 (RESEARCH OFC)');",
                     "insert into data_rooms values (514,2,'LSRB 1118',NULL,NULL,'LSRB 1118 (WRITE UP)');",
                     "insert into data_rooms values (515,2,'LSRB 1119',NULL,NULL,'LSRB 1119 (RESEARCH LAB)');",
                     "insert into data_rooms values (516,2,'LSRB 1120',NULL,NULL,'LSRB 1120 (RESEARCH LAB)');",
                     "insert into data_rooms values (517,2,'LSRB 1121',NULL,NULL,'LSRB 1121 (RESEARCH LAB)');",
                     "insert into data_rooms values (518,2,'LSRB 1122',NULL,NULL,'LSRB 1122 (SPEC PURP LAB)');",
                     "insert into data_rooms values (519,2,'LSRB 1123',NULL,NULL,'LSRB 1123 (RESEARCH OFC)');",
                     "insert into data_rooms values (520,2,'LSRB 1124',NULL,NULL,'LSRB 1124 (WORKSTATION)');",
                     "insert into data_rooms values (521,2,'LSRB 1125',NULL,NULL,'LSRB 1125 (ADMIN OFC)');",
                     "insert into data_rooms values (522,2,'LSRB 1126',NULL,NULL,'LSRB 1126 (ADMIN OFC)');",
                     "insert into data_rooms values (523,2,'LSRB 1127',NULL,NULL,'LSRB 1127 (ADMIN OFC)');",
                     "insert into data_rooms values (524,2,'LSRB 1128',NULL,NULL,'LSRB 1128 (RESEARCH LAB)');",
                     "insert into data_rooms values (525,2,'LSRB 1129',NULL,NULL,'LSRB 1129 (RESEARCH LAB)');",
                     "insert into data_rooms values (526,2,'LSRB 1130',NULL,NULL,'LSRB 1130 (COLD RM)');",
                     "insert into data_rooms values (527,2,'LSRB 1131',NULL,NULL,'LSRB 1131 (WRITE UP)');",
                     "insert into data_rooms values (528,2,'LSRB 1132',NULL,NULL,'LSRB 1132 (ADMIN SUPT/SEC)');",
                     "insert into data_rooms values (529,2,'LSRB 1134',NULL,NULL,'LSRB 1134 (TECH OFC)');",
                     "insert into data_rooms values (530,2,'LSRB 1136',NULL,NULL,'LSRB 1136 (FACULTY OFC)');",
                     "insert into data_rooms values (531,2,'LSRB 1138',NULL,NULL,'LSRB 1138 (HEADHOUSE)');",
                     "insert into data_rooms values (532,2,'LSRB 1139',NULL,NULL,'LSRB 1139 (GROWING ROOM 2)');",
                     "insert into data_rooms values (533,2,'LSRB 1140',NULL,NULL,'LSRB 1140 (GROWING ROOM 1)');",
                     "insert into data_rooms values (534,2,'LSRB 1141',NULL,NULL,'LSRB 1141 (XRAY CRYST.)');",
                     "insert into data_rooms values (535,2,'LSRB 1142',NULL,NULL,'LSRB 1142 (RES GRAD ASST)');",
                     "insert into data_rooms values (536,2,'LSRB 1143',NULL,NULL,'LSRB 1143 (LARGE CONFERENCE)');",
                     "insert into data_rooms values (537,2,'LSRB 1144',NULL,NULL,'LSRB 1144 (CONFERENCE RM)');",
                     "insert into data_rooms values (538,2,'LSRB 1145',NULL,NULL,'LSRB 1145 (OFFICE)');",
                     "insert into data_rooms values (539,2,'LSRB 1146',NULL,NULL,'LSRB 1146 (VESTIBULE)');",
                     "insert into data_rooms values (540,2,'LSRB 1147',NULL,NULL,'LSRB 1147 (FACULTY OFC)');",
                     "insert into data_rooms values (541,2,'LSRB 1148',NULL,NULL,'LSRB 1148 (CONTROL RM)');",
                     "insert into data_rooms values (542,2,'LSRB 1149',NULL,NULL,'LSRB 1149 (FACULTY OFC)');",
                     "insert into data_rooms values (543,2,'LSRB 1150',NULL,NULL,'LSRB 1150 (VESTIBULE)');",
                     "insert into data_rooms values (544,2,'LSRB 1151',NULL,NULL,'LSRB 1151 (ADV INSTR)');",
                     "insert into data_rooms values (545,2,'LSRB 1152',NULL,NULL,'LSRB 1152 (SMALL EQUIP)');",
                     "insert into data_rooms values (546,2,'LSRB 1153',NULL,NULL,'LSRB 1153 (LABORATORY)');",
                     "insert into data_rooms values (547,2,'LSRB 1154',NULL,NULL,'LSRB 1154 (LABORATORY)');",
                     "insert into data_rooms values (548,2,'LSRB 1155',NULL,NULL,'LSRB 1155 (DARK RM)');",
                     "insert into data_rooms values (549,2,'LSRB 1156',NULL,NULL,'LSRB 1156 (RESEARCH LAB)');",
                     "insert into data_rooms values (550,2,'LSRB 1157',NULL,NULL,'LSRB 1157 (SMALL EQUIP)');",
                     "insert into data_rooms values (551,2,'LSRB 1158',NULL,NULL,'LSRB 1158 (RESEARCH LAB)');",
                     "insert into data_rooms values (552,2,'LSRB 1159',NULL,NULL,'LSRB 1159 (RESEARCH LAB)');",
                     "insert into data_rooms values (553,2,'LSRB 1160',NULL,NULL,'LSRB 1160 (DATA ANALYSIS)');",
                     "insert into data_rooms values (554,2,'LSRB 1161',NULL,NULL,'LSRB 1161 (NMR CONTROL)');",
                     "insert into data_rooms values (555,2,'LSRB 1162',NULL,NULL,'LSRB 1162 (RESEARCH LAB)');",
                     "insert into data_rooms values (556,2,'LSRB 1163',NULL,NULL,'LSRB 1163 (RESEARCH LAB)');",
                     "insert into data_rooms values (557,2,'LSRB 1164',NULL,NULL,'LSRB 1164 (RESEARCH LAB)');",
                     "insert into data_rooms values (558,2,'LSRB 1165',NULL,NULL,'LSRB 1165 (RESEARCH LAB)');",
                     "insert into data_rooms values (559,2,'LSRB 1166',NULL,NULL,'LSRB 1166 (NMR)');",
                     "insert into data_rooms values (560,2,'LSRB 1167',NULL,NULL,'LSRB 1167 (RESEARCH LAB)');",
                     "insert into data_rooms values (561,2,'LSRB 1168',NULL,NULL,'LSRB 1168 (RESEARCH LAB)');",
                     "insert into data_rooms values (562,2,'LSRB 1169',NULL,NULL,'LSRB 1169 (RESEARCH LAB)');",
                     "insert into data_rooms values (563,2,'LSRB 1170',NULL,NULL,'LSRB 1170 (COLD ROOM)');",
                     "insert into data_rooms values (564,2,'LSRB 1171',NULL,NULL,'LSRB 1171 (COLD ROOM)');",
                     "insert into data_rooms values (565,2,'LSRB 2001',NULL,NULL,'LSRB 2001 (WARM LAB)');",
                     "insert into data_rooms values (566,2,'LSRB 2002',NULL,NULL,'LSRB 2002 (MECHANICAL RM)');",
                     "insert into data_rooms values (567,2,'LSRB 2003',NULL,NULL,'LSRB 2003 (RESEARCH LAB)');",
                     "insert into data_rooms values (568,2,'LSRB 2004',NULL,NULL,'LSRB 2004 (RESEARCH LAB)');",
                     "insert into data_rooms values (569,2,'LSRB 2005',NULL,NULL,'LSRB 2005 (RESEARCH LAB)');",
                     "insert into data_rooms values (570,2,'LSRB 2006',NULL,NULL,'LSRB 2006 (RESEARCH LAB)');",
                     "insert into data_rooms values (571,2,'LSRB 2007',NULL,NULL,'LSRB 2007 (RESEARCH LAB)');",
                     "insert into data_rooms values (572,2,'LSRB 2008',NULL,NULL,'LSRB 2008 (RESEARCH LAB)');",
                     "insert into data_rooms values (573,2,'LSRB 2009',NULL,NULL,'LSRB 2009 (COLD RM)');",
                     "insert into data_rooms values (574,2,'LSRB 2010',NULL,NULL,'LSRB 2010 (CORRIDOR)');",
                     "insert into data_rooms values (575,2,'LSRB 2011',NULL,NULL,'LSRB 2011 (ELECTRONICS SHOP)');",
                     "insert into data_rooms values (576,2,'LSRB 2012',NULL,NULL,'LSRB 2012 (TELECOM CLOSET)');",
                     "insert into data_rooms values (577,2,'LSRB 2013',NULL,NULL,'LSRB 2013 (ELECTRIC RM)');",
                     "insert into data_rooms values (578,2,'LSRB 2014',NULL,NULL,'LSRB 2014 (MECHANICAL)');",
                     "insert into data_rooms values (579,2,'LSRB 2015',NULL,NULL,'LSRB 2015 (EQUIPMENT RM)');",
                     "insert into data_rooms values (580,2,'LSRB 2016',NULL,NULL,'LSRB 2016 (ADVANCED COMPUTA)');",
                     "insert into data_rooms values (581,2,'LSRB 2017',NULL,NULL,'LSRB 2017 (WRITE UP)');",
                     "insert into data_rooms values (582,2,'LSRB 2018',NULL,NULL,'LSRB 2018 (LASER ROOM)');",
                     "insert into data_rooms values (583,2,'LSRB 2019',NULL,NULL,'LSRB 2019 (WRITE UP)');",
                     "insert into data_rooms values (584,2,'LSRB 2020',NULL,NULL,'LSRB 2020 (ADVANCED CORE INS)');",
                     "insert into data_rooms values (585,2,'LSRB 2021',NULL,NULL,'LSRB 2021 (GLSSWASH/AUTOCLAV)');",
                     "insert into data_rooms values (586,2,'LSRB 2023',NULL,NULL,'LSRB 2023 (EQUIPMENT RM)');",
                     "insert into data_rooms values (587,2,'LSRB 2024',NULL,NULL,'LSRB 2024 (CORRIDOR)');",
                     "insert into data_rooms values (588,2,'LSRB 2025',NULL,NULL,'LSRB 2025 (COLD RM)');",
                     "insert into data_rooms values (589,2,'LSRB 2027',NULL,NULL,'LSRB 2027 (WRITE UP)');",
                     "insert into data_rooms values (590,2,'LSRB 2029',NULL,NULL,'LSRB 2029 (WRITE UP)');",
                     "insert into data_rooms values (591,2,'LSRB 2030',NULL,NULL,'LSRB 2030 (RADIOACTIVE)');",
                     "insert into data_rooms values (592,2,'LSRB 2031',NULL,NULL,'LSRB 2031 (EQUIPMENT RM)');",
                     "insert into data_rooms values (593,2,'LSRB 2033',NULL,NULL,'LSRB 2033 (CORRIDOR)');",
                     "insert into data_rooms values (594,2,'LSRB 2051',NULL,NULL,'LSRB 2051 (FACULTY OFC)');",
                     "insert into data_rooms values (595,2,'LSRB 2052',NULL,NULL,'LSRB 2052 (MEETING AREA)');",
                     "insert into data_rooms values (596,2,'LSRB 2053',NULL,NULL,'LSRB 2053 (SPEC PURP LAB)');",
                     "insert into data_rooms values (597,2,'LSRB 2054',NULL,NULL,'LSRB 2054 (LABORATORY)');",
                     "insert into data_rooms values (598,2,'LSRB 2055',NULL,NULL,'LSRB 2055 (SPEC PURP LAB)');",
                     "insert into data_rooms values (599,2,'LSRB 2056',NULL,NULL,'LSRB 2056 (COLD LAB)');",
                     "insert into data_rooms values (600,2,'LSRB 2057',NULL,NULL,'LSRB 2057 (COLD LAB)');",
                     "insert into data_rooms values (601,2,'LSRB 2058',NULL,NULL,'LSRB 2058 (RESEARCH LAB)');",
                     "insert into data_rooms values (602,2,'LSRB 2059',NULL,NULL,'LSRB 2059 (LABORATORY)');",
                     "insert into data_rooms values (603,2,'LSRB 2060',NULL,NULL,'LSRB 2060 (FACULTY OFC)');",
                     "insert into data_rooms values (604,2,'LSRB 2061',NULL,NULL,'LSRB 2061 (FACULTY OFC)');",
                     "insert into data_rooms values (605,2,'LSRB 2062',NULL,NULL,'LSRB 2062 (FACULTY OFC)');",
                     "insert into data_rooms values (606,2,'LSRB 2063',NULL,NULL,'LSRB 2063 (TCL/SPECIAL)');",
                     "insert into data_rooms values (607,2,'LSRB 2064',NULL,NULL,'LSRB 2064 (SPEC PURP LAB)');",
                     "insert into data_rooms values (608,2,'LSRB 2065',NULL,NULL,'LSRB 2065 (LABORATORY)');",
                     "insert into data_rooms values (609,2,'LSRB 2066',NULL,NULL,'LSRB 2066 (SPEC PURP LAB)');",
                     "insert into data_rooms values (610,2,'LSRB 2067',NULL,NULL,'LSRB 2067 (LABORATORY)');",
                     "insert into data_rooms values (611,2,'LSRB 2068',NULL,NULL,'LSRB 2068 (SMALL EQUIP)');",
                     "insert into data_rooms values (612,2,'LSRB 2069',NULL,NULL,'LSRB 2069 (RESEARCH LAB)');",
                     "insert into data_rooms values (613,2,'LSRB 2070',NULL,NULL,'LSRB 2070 (RESEARCH LAB)');",
                     "insert into data_rooms values (614,2,'LSRB 2071',NULL,NULL,'LSRB 2071 (RESEARCH LAB)');",
                     "insert into data_rooms values (615,2,'LSRB 2072',NULL,NULL,'LSRB 2072 (LABORATORY)');",
                     "insert into data_rooms values (616,2,'LSRB 2073',NULL,NULL,'LSRB 2073 (TCL/SPECIAL)');",
                     "insert into data_rooms values (617,2,'LSRB 2074',NULL,NULL,'LSRB 2074 (TCL/SPECIAL)');",
                     "insert into data_rooms values (618,2,'LSRB 2075',NULL,NULL,'LSRB 2075 (LABORATORY)');",
                     "insert into data_rooms values (619,2,'LSRB 2076',NULL,NULL,'LSRB 2076 (FACULTY OFC)');",
                     "insert into data_rooms values (620,2,'LSRB 2077',NULL,NULL,'LSRB 2077 (FACULTY OFC)');",
                     "insert into data_rooms values (621,2,'LSRB 2078',NULL,NULL,'LSRB 2078 (FACULTY OFC)');",
                     "insert into data_rooms values (622,2,'LSRB 2079',NULL,NULL,'LSRB 2079 (RESEARCH LAB)');",
                     "insert into data_rooms values (623,2,'LSRB 2080',NULL,NULL,'LSRB 2080 (AUTOCLAVE)');",
                     "insert into data_rooms values (624,2,'LSRB 2081',NULL,NULL,'LSRB 2081 (SPEC PURP LAB)');",
                     "insert into data_rooms values (625,2,'LSRB 2082',NULL,NULL,'LSRB 2082 (LABORATORY)');",
                     "insert into data_rooms values (626,2,'LSRB 2083',NULL,NULL,'LSRB 2083 (SPEC PURP LAB)');",
                     "insert into data_rooms values (627,2,'LSRB 2084',NULL,NULL,'LSRB 2084 (ELECTRIC RM)');",
                     "insert into data_rooms values (628,2,'LSRB 2085',NULL,NULL,'LSRB 2085 (TELCOM CLOSET)');",
                     "insert into data_rooms values (629,2,'LSRB 2086',NULL,NULL,'LSRB 2086 (SPEC PURP LAB)');",
                     "insert into data_rooms values (630,2,'LSRB 2087',NULL,NULL,'LSRB 2087 (MECHANICAL RM)');",
                     "insert into data_rooms values (631,2,'LSRB 2088',NULL,NULL,'LSRB 2088 (WARM LAB)');",
                     "insert into data_rooms values (632,2,'LSRB 2089',NULL,NULL,'LSRB 2089 (LABORATORY)');",
                     "insert into data_rooms values (633,2,'LSRB 2090',NULL,NULL,'LSRB 2090 (SMALL EQUIP)');",
                     "insert into data_rooms values (634,2,'LSRB 2091',NULL,NULL,'LSRB 2091 (DECON GLASSWASH)');",
                     "insert into data_rooms values (635,2,'LSRB 2092',NULL,NULL,'LSRB 2092 (STORAGE)');",
                     "insert into data_rooms values (636,2,'LSRB 2093',NULL,NULL,'LSRB 2093 (FACULTY OFC)');",
                     "insert into data_rooms values (637,2,'LSRB 2094',NULL,NULL,'LSRB 2094 (CONFERENCE)');",
                     "insert into data_rooms values (638,2,'LSRB 2095',NULL,NULL,'LSRB 2095 (AUDITORIUM)');",
                     "insert into data_rooms values (639,2,'LSRB 2096',NULL,NULL,'LSRB 2096 (TEA ROOM)');",
                     "insert into data_rooms values (640,2,'LSRB 2097',NULL,NULL,'LSRB 2097 (COMPUTER ANALYSIS)');",
                     "insert into data_rooms values (641,2,'LSRB 2098',NULL,NULL,'LSRB 2098 (OFFICE)');",
                     "insert into data_rooms values (642,2,'LSRB 2099',NULL,NULL,'LSRB 2099 (FACULTY OFC)');",
                     "insert into data_rooms values (643,2,'LSRB 2100',NULL,NULL,'LSRB 2100 (TEA ROOM)');",
                     "insert into data_rooms values (644,2,'LSRB 2101',NULL,NULL,'LSRB 2101 (CONFERENCE RM)');",
                     "insert into data_rooms values (645,2,'LSRB 2102',NULL,NULL,'LSRB 2102 (OFFICE)');",
                     "insert into data_rooms values (646,2,'LSRB 1000A',NULL,NULL,'LSRB 1000A (LOBBY)');",
                     "insert into data_rooms values (647,2,'LSRB 1001A',NULL,NULL,'LSRB 1001A (STORAGE)');",
                     "insert into data_rooms values (648,2,'LSRB 1003A',NULL,NULL,'LSRB 1003A (COLD ROOM)');",
                     "insert into data_rooms values (649,2,'LSRB 1003B',NULL,NULL,'LSRB 1003B (EQUIPMENT RM)');",
                     "insert into data_rooms values (650,2,'LSRB 1003C',NULL,NULL,'LSRB 1003C (SUPPORT LAB)');",
                     "insert into data_rooms values (651,2,'LSRB 1003D',NULL,NULL,'LSRB 1003D (RESEARCH LAB)');",
                     "insert into data_rooms values (652,2,'LSRB 1003E',NULL,NULL,'LSRB 1003E (FERMENTOR RM)');",
                     "insert into data_rooms values (653,2,'LSRB 1003F',NULL,NULL,'LSRB 1003F (AUTOCLAVE)');",
                     "insert into data_rooms values (654,2,'LSRB 1003G',NULL,NULL,'LSRB 1003G (MEDIA PREP)');",
                     "insert into data_rooms values (655,2,'LSRB 1003H',NULL,NULL,'LSRB 1003H (SUPPORT LAB)');",
                     "insert into data_rooms values (656,2,'LSRB 1003I',NULL,NULL,'LSRB 1003I (SUPPORT LAB)');",
                     "insert into data_rooms values (657,2,'LSRB 1003J',NULL,NULL,'LSRB 1003J (SUPPORT LAB)');",
                     "insert into data_rooms values (658,2,'LSRB 1003K',NULL,NULL,'LSRB 1003K (EQUIPMENT RM)');",
                     "insert into data_rooms values (659,2,'LSRB 1003L',NULL,NULL,'LSRB 1003L (SUPPORT LAB)');",
                     "insert into data_rooms values (660,2,'LSRB 1003M',NULL,NULL,'LSRB 1003M (RESEARCH LAB)');",
                     "insert into data_rooms values (661,2,'LSRB 1003N',NULL,NULL,'LSRB 1003N (FACULTY OFC)');",
                     "insert into data_rooms values (662,2,'LSRB 1003P',NULL,NULL,'LSRB 1003P (FACULTY OFC)');",
                     "insert into data_rooms values (663,2,'LSRB 1003R',NULL,NULL,'LSRB 1003R (FACULTY OFC)');",
                     "insert into data_rooms values (664,2,'LSRB 1005A',NULL,NULL,'LSRB 1005A (VESTIBULE)');",
                     "insert into data_rooms values (665,2,'LSRB 1007A',NULL,NULL,'LSRB 1007A (CORRIDOR)');",
                     "insert into data_rooms values (666,2,'LSRB 1010A',NULL,NULL,'LSRB 1010A (CLOSET)');",
                     "insert into data_rooms values (667,2,'LSRB 1010B',NULL,NULL,'LSRB 1010B (CLOSET)');",
                     "insert into data_rooms values (668,2,'LSRB 1012A',NULL,NULL,'LSRB 1012A (CORRIDOR)');",
                     "insert into data_rooms values (669,2,'LSRB 1017A',NULL,NULL,'LSRB 1017A (VESTIBULE)');",
                     "insert into data_rooms values (670,2,'LSRB 1025A',NULL,NULL,'LSRB 1025A (CORRIDOR)');",
                     "insert into data_rooms values (671,2,'LSRB 1031A',NULL,NULL,'LSRB 1031A (CORRIDOR)');",
                     "insert into data_rooms values (672,2,'LSRB 1032A',NULL,NULL,'LSRB 1032A (EQUIPMENT RM)');",
                     "insert into data_rooms values (673,2,'LSRB 1043A',NULL,NULL,'LSRB 1043A (EQUIPMENT RM)');",
                     "insert into data_rooms values (674,2,'LSRB 1050A',NULL,NULL,'LSRB 1050A (EQUIPMENT RM)');",
                     "insert into data_rooms values (675,2,'LSRB 1056A',NULL,NULL,'LSRB 1056A (EQUIPMENT RM)');",
                     "insert into data_rooms values (676,2,'LSRB 1064A',NULL,NULL,'LSRB 1064A (CORRIDOR)');",
                     "insert into data_rooms values (677,2,'LSRB 1072A',NULL,NULL,'LSRB 1072A (JANITORS CLOSET)');",
                     "insert into data_rooms values (678,2,'LSRB 1072B',NULL,NULL,'LSRB 1072B (TOILET)');",
                     "insert into data_rooms values (679,2,'LSRB 1073A',NULL,NULL,'LSRB 1073A (EQUIPMENT RM)');",
                     "insert into data_rooms values (680,2,'LSRB 1079A',NULL,NULL,'LSRB 1079A (EQUIPMENT RM)');",
                     "insert into data_rooms values (681,2,'LSRB 1079B',NULL,NULL,'LSRB 1079B (STORAGE)');",
                     "insert into data_rooms values (682,2,'LSRB 1081A',NULL,NULL,'LSRB 1081A (CORRIDOR)');",
                     "insert into data_rooms values (683,2,'LSRB 1087A',NULL,NULL,'LSRB 1087A (SMALL EQUIP)');",
                     "insert into data_rooms values (684,2,'LSRB 1091A',NULL,NULL,'LSRB 1091A (TOILET)');",
                     "insert into data_rooms values (685,2,'LSRB 1100A',NULL,NULL,'LSRB 1100A (TELCOM CLOSET)');",
                     "insert into data_rooms values (686,2,'LSRB 1100B',NULL,NULL,'LSRB 1100B (ELECTRIC RM)');",
                     "insert into data_rooms values (687,2,'LSRB 1100C',NULL,NULL,'LSRB 1100C (CORRIDOR)');",
                     "insert into data_rooms values (688,2,'LSRB 1135A',NULL,NULL,'LSRB 1135A (CORRIDOR)');",
                     "insert into data_rooms values (689,2,'LSRB 1138A',NULL,NULL,'LSRB 1138A (CORRIDOR)');",
                     "insert into data_rooms values (690,2,'LSRB 1138B',NULL,NULL,'LSRB 1138B (VESTIBULE)');",
                     "insert into data_rooms values (691,2,'LSRB 1141C',NULL,NULL,'LSRB 1141C (CORRIDOR)');",
                     "insert into data_rooms values (692,2,'LSRB 1142A',NULL,NULL,'LSRB 1142A (CORRIDOR)');",
                     "insert into data_rooms values (693,2,'LSRB 1143A',NULL,NULL,'LSRB 1143A (CONF SERVICE)');",
                     "insert into data_rooms values (694,2,'LSRB 1143B',NULL,NULL,'LSRB 1143B (CLOSET)');",
                     "insert into data_rooms values (695,2,'LSRB 1144A',NULL,NULL,'LSRB 1144A (CLOSET)');",
                     "insert into data_rooms values (696,2,'LSRB 1144B',NULL,NULL,'LSRB 1144B (CLOSET)');",
                     "insert into data_rooms values (697,2,'LSRB 1146A',NULL,NULL,'LSRB 1146A (RADIO LAB)');",
                     "insert into data_rooms values (698,2,'LSRB 1148A',NULL,NULL,'LSRB 1148A (SPEC CHEM LAB)');",
                     "insert into data_rooms values (699,2,'LSRB 1148B',NULL,NULL,'LSRB 1148B (CORRIDOR)');",
                     "insert into data_rooms values (700,2,'LSRB 1150A',NULL,NULL,'LSRB 1150A (TOXIC LAB)');",
                     "insert into data_rooms values (701,2,'LSRB 2001A',NULL,NULL,'LSRB 2001A (CORRIDOR)');",
                     "insert into data_rooms values (702,2,'LSRB 2001B',NULL,NULL,'LSRB 2001B (TECH SERVICES)');",
                     "insert into data_rooms values (703,2,'LSRB 2052A',NULL,NULL,'LSRB 2052A (CORRIDOR)');",
                     "insert into data_rooms values (704,2,'LSRB 2054A',NULL,NULL,'LSRB 2054A (SMALL EQUIP)');",
                     "insert into data_rooms values (705,2,'LSRB 2059A',NULL,NULL,'LSRB 2059A (SMALL EQUIP)');",
                     "insert into data_rooms values (706,2,'LSRB 2060A',NULL,NULL,'LSRB 2060A (WORKSTATION)');",
                     "insert into data_rooms values (707,2,'LSRB 2063A',NULL,NULL,'LSRB 2063A (CORRIDOR)');",
                     "insert into data_rooms values (708,2,'LSRB 2065A',NULL,NULL,'LSRB 2065A (SMALL EQUIP)');",
                     "insert into data_rooms values (709,2,'LSRB 2070A',NULL,NULL,'LSRB 2070A (RESEARCH LAB)');",
                     "insert into data_rooms values (710,2,'LSRB 2075A',NULL,NULL,'LSRB 2075A (SMALL EQUIP)');",
                     "insert into data_rooms values (711,2,'LSRB 2076A',NULL,NULL,'LSRB 2076A (WORKSTATION)');",
                     "insert into data_rooms values (712,2,'LSRB 2082A',NULL,NULL,'LSRB 2082A (SMALL EQUIP)');",
                     "insert into data_rooms values (713,2,'LSRB 2085A',NULL,NULL,'LSRB 2085A (CORRIDOR)');",
                     "insert into data_rooms values (714,2,'LSRB 2085B',NULL,NULL,'LSRB 2085B (CORRIDOR)');",
                     "insert into data_rooms values (715,2,'LSRB 2089B',NULL,NULL,'LSRB 2089B (CORRIDOR)');",
                     "insert into data_rooms values (716,2,'LSRB 2095A',NULL,NULL,'LSRB 2095A (PROJECTION BOOTHS)');",
                     "insert into data_rooms values (717,2,'LSRB 2095B',NULL,NULL,'LSRB 2095B (PROJECTION BOOTHS)');",
                     "insert into data_rooms values (718,2,'LSRB 2095E',NULL,NULL,'LSRB 2095E (CORRIDOR)');",
                     "insert into data_rooms values (719,2,'LSRB 2097A',NULL,NULL,'LSRB 2097A (MECHANICAL)');",
                     "insert into data_rooms values (720,2,'LSRB 2099A',NULL,NULL,'LSRB 2099A (CORRIDOR)');",
                     "insert into data_rooms values (721,2,'LSRB 2099B',NULL,NULL,'LSRB 2099B (CORRIDOR)');",
                     "insert into data_rooms values (722,2,'LSRB 2015A',NULL,NULL,'LSRB 2015A (RESEARCH LAB)');",
                     "insert into data_rooms values (723,2,'LSRB 2015B',NULL,NULL,'LSRB 2015B (STORAGE)');",
                     "insert into data_rooms values (724,2,'LSRB 2016A',NULL,NULL,'LSRB 2016A (FOMP MGR OFC)');",
                     "insert into data_rooms values (725,2,'LSRB 2017A',NULL,NULL,'LSRB 2017A (RESEARCH LAB)');",
                     "insert into data_rooms values (726,2,'LSRB 2020A',NULL,NULL,'LSRB 2020A (INSTRUMNT MGR OFC)');",
                     "insert into data_rooms values (727,2,'LSRB 2021A',NULL,NULL,'LSRB 2021A (GLSSWASH/AUTOCLAV)');",
                     "insert into data_rooms values (728,2,'LSRB 2023A',NULL,NULL,'LSRB 2023A (RESEARCH LAB)');",
                     "insert into data_rooms values (729,2,'LSRB 2027A',NULL,NULL,'LSRB 2027A (RESEARCH LAB)');",
                     "insert into data_rooms values (730,2,'LSRB 2031A',NULL,NULL,'LSRB 2031A (RESEARCH LAB)');",
                     "insert into data_rooms values (731,2,'LSRB 2033A',NULL,NULL,'LSRB 2033A (BREAK ROOM)');",
                     "insert into data_rooms values (732,2,'LSRB 2033B',NULL,NULL,'LSRB 2033B (VISITING INVESTIG)');",
                     "insert into data_rooms values (733,2,'LSRB 2033C',NULL,NULL,'LSRB 2033C (CONFERENCE RM)');",
                     "insert into data_rooms values (734,2,'LSRB 2033D',NULL,NULL,'LSRB 2033D (RESEARCH OFC)');",
                     "insert into data_rooms values (735,2,'LSRB 2033E',NULL,NULL,'LSRB 2033E (RESEARCH OFC)');",
                     "insert into data_rooms values (736,2,'LSRB 2033F',NULL,NULL,'LSRB 2033F (RESEARCH OFC)');",
                     "insert into data_rooms values (737,2,'LSRB 2033G',NULL,NULL,'LSRB 2033G (RESEARCH OFC)');",
                     "insert into data_rooms values (738,2,'LSRB 2033H',NULL,NULL,'LSRB 2033H (ADMIN OFC)');",
                     "insert into data_rooms values (739,2,'LSRB 2033I',NULL,NULL,'LSRB 2033I (DIRECTOR'S OFC)');",
                     "insert into data_rooms values (740,2,'LSRB 2033J',NULL,NULL,'LSRB 2033J (CONFERENCE RM)');",
                     "insert into data_rooms values (741,2,'LSRB B001',NULL,NULL,'LSRB B001 (PREP AREA)');",
                     "insert into data_rooms values (742,2,'LSRB B001A',NULL,NULL,'LSRB B001A (LABORATORY SVC)');",
                     "insert into data_rooms values (743,2,'LSRB B002',NULL,NULL,'LSRB B002 (BEHAV TESTING)');",
                     "insert into data_rooms values (744,2,'LSRB B003',NULL,NULL,'LSRB B003 (BEHAV TESTING)');",
                     "insert into data_rooms values (745,2,'LSRB B004',NULL,NULL,'LSRB B004 (BEHAV TESTING)');",
                     "insert into data_rooms values (746,2,'LSRB B005',NULL,NULL,'LSRB B005 (PREP AREA)');",
                     "insert into data_rooms values (747,2,'LSRB B006',NULL,NULL,'LSRB B006 (LINEN HOLDING)');",
                     "insert into data_rooms values (748,2,'LSRB B007',NULL,NULL,'LSRB B007 (LOCKER RM)');",
                     "insert into data_rooms values (749,2,'LSRB B007A',NULL,NULL,'LSRB B007A (DATA ANALYSIS)');",
                     "insert into data_rooms values (750,2,'LSRB B008',NULL,NULL,'LSRB B008 (PREP AREA)');",
                     "insert into data_rooms values (751,2,'LSRB B009',NULL,NULL,'LSRB B009 (BEHAV TESTING)');",
                     "insert into data_rooms values (752,2,'LSRB B009A',NULL,NULL,'LSRB B009A (LABORATORY SVC)');",
                     "insert into data_rooms values (753,2,'LSRB B010',NULL,NULL,'LSRB B010 (BEHAV TESTING)');",
                     "insert into data_rooms values (754,2,'LSRB B011',NULL,NULL,'LSRB B011 (BEHAV TESTING)');",
                     "insert into data_rooms values (755,2,'LSRB B011A',NULL,NULL,'LSRB B011A (LABORATORY SVC)');",
                     "insert into data_rooms values (756,2,'LSRB B012',NULL,NULL,'LSRB B012 (BEHAV TESTING)');",
                     "insert into data_rooms values (757,2,'LSRB B013',NULL,NULL,'LSRB B013 (BEHAV TESTING)');",
                     "insert into data_rooms values (758,2,'LSRB B014',NULL,NULL,'LSRB B014 (PREP AREA)');",
                     "insert into data_rooms values (759,2,'LSRB B015',NULL,NULL,'LSRB B015 (BEHAV TESTING)');",
                     "insert into data_rooms values (760,2,'LSRB B016',NULL,NULL,'LSRB B016 (BEHAV TESTING)');",
                     "insert into data_rooms values (761,2,'LSRB B016A',NULL,NULL,'LSRB B016A (LABORATORY SVC)');",
                     "insert into data_rooms values (762,2,'LSRB B017',NULL,NULL,'LSRB B017 (BEHAV TESTING)');",
                     "insert into data_rooms values (763,2,'LSRB B018',NULL,NULL,'LSRB B018 (BEHAV TESTING)');",
                     "insert into data_rooms values (764,2,'LSRB B019',NULL,NULL,'LSRB B019 (BEHAV TESTING)');",
                     "insert into data_rooms values (765,2,'LSRB B020',NULL,NULL,'LSRB B020 (BEHAV TESTING)');",
                     "insert into data_rooms values (766,2,'LSRB B021',NULL,NULL,'LSRB B021 (BEHAV TESTING)');",
                     "insert into data_rooms values (767,2,'LSRB B022',NULL,NULL,'LSRB B022 (BEHAV TESTING)');",
                     "insert into data_rooms values (768,2,'LSRB B022A',NULL,NULL,'LSRB B022A (LABORATORY SVC)');",
                     "insert into data_rooms values (769,2,'LSRB B023',NULL,NULL,'LSRB B023 (BEHAV TESTING)');",
                     "insert into data_rooms values (770,2,'LSRB B024',NULL,NULL,'LSRB B024 (BEHAV TESTING)');",
                     "insert into data_rooms values (771,2,'LSRB B025',NULL,NULL,'LSRB B025 (BEHAV TESTING)');",
                     "insert into data_rooms values (772,2,'LSRB B026',NULL,NULL,'LSRB B026 (BEHAV TESTING)');",
                     "insert into data_rooms values (773,2,'LSRB B026A',NULL,NULL,'LSRB B026A (LABORATORY SVC)');",
                     "insert into data_rooms values (774,2,'LSRB B027',NULL,NULL,'LSRB B027 (TESTING RM)');",
                     "insert into data_rooms values (775,2,'LSRB B028',NULL,NULL,'LSRB B028 (TESTING RM)');",
                     "insert into data_rooms values (776,2,'LSRB B029',NULL,NULL,'LSRB B029 (BEHAV TESTING)');",
                     "insert into data_rooms values (777,2,'LSRB B030',NULL,NULL,'LSRB B030 (BEHAV TESTING)');",
                     "insert into data_rooms values (778,2,'LSRB B031',NULL,NULL,'LSRB B031 (PREP AREA)');",
                     "insert into data_rooms values (779,2,'LSRB B032',NULL,NULL,'LSRB B032 (BEHAV TESTING)');",
                     "insert into data_rooms values (780,2,'LSRB B032A',NULL,NULL,'LSRB B032A (LABORATORY SVC)');",
                     "insert into data_rooms values (781,2,'LSRB B033',NULL,NULL,'LSRB B033 (BEHAV TESTING)');",
                     "insert into data_rooms values (782,2,'LSRB B034',NULL,NULL,'LSRB B034 (BEHAV TESTING)');",
                     "insert into data_rooms values (783,2,'LSRB B035',NULL,NULL,'LSRB B035 (BEHAV TESTING)');",
                     "insert into data_rooms values (784,2,'LSRB B036',NULL,NULL,'LSRB B036 (CLEAN FOOD/BED)');",
                     "insert into data_rooms values (785,2,'LSRB B036A',NULL,NULL,'LSRB B036A (SOILED HOLDING)');",
                     "insert into data_rooms values (786,2,'LSRB B036B',NULL,NULL,'LSRB B036B (AIR LOCK)');",
                     "insert into data_rooms values (787,2,'LSRB B036C',NULL,NULL,'LSRB B036C (LABORATORY SVC)');",
                     "insert into data_rooms values (788,2,'LSRB B036D',NULL,NULL,'LSRB B036D (TOILET)');",
                     "insert into data_rooms values (789,2,'LSRB B036E',NULL,NULL,'LSRB B036E (SHOWER/CHANGE)');",
                     "insert into data_rooms values (790,2,'LSRB B036F',NULL,NULL,'LSRB B036F (CLEAN LINEN)');",
                     "insert into data_rooms values (791,2,'LSRB B037',NULL,NULL,'LSRB B037 (STAFF OFFICE)');",
                     "insert into data_rooms values (792,2,'LSRB B037A',NULL,NULL,'LSRB B037A (TEL/DATA)');",
                     "insert into data_rooms values (793,2,'LSRB B037B',NULL,NULL,'LSRB B037B (ELECTRICAL CLOSET)');",
                     "insert into data_rooms values (794,2,'LSRB B037F',NULL,NULL,'LSRB B037F (CLEAN LINEN)');",
                     "insert into data_rooms values (795,2,'LSRB B038',NULL,NULL,'LSRB B038 (CONTROL SUBST)');",
                     "insert into data_rooms values (796,2,'LSRB B039',NULL,NULL,'LSRB B039 (SURGICAL PREP)');",
                     "insert into data_rooms values (797,2,'LSRB B039A',NULL,NULL,'LSRB B039A (SURGICAL DECON)');",
                     "insert into data_rooms values (798,2,'LSRB B040',NULL,NULL,'LSRB B040 (EUTHANASIA)');",
                     "insert into data_rooms values (799,2,'LSRB B041',NULL,NULL,'LSRB B041 (BREAK ROOM)');",
                     "insert into data_rooms values (800,2,'LSRB B041A',NULL,NULL,'LSRB B041A (BREAK RM SVC)');",
                     "insert into data_rooms values (801,2,'LSRB B042',NULL,NULL,'LSRB B042 (CLEAN CAGEWASH)');",
                     "insert into data_rooms values (802,2,'LSRB B042A',NULL,NULL,'LSRB B042A (JANITORS CLOSET)');",
                     "insert into data_rooms values (803,2,'LSRB B043',NULL,NULL,'LSRB B043 (DECON CAGEWASH)');",
                     "insert into data_rooms values (804,2,'LSRB B044',NULL,NULL,'LSRB B044 (QUARANTINE)');",
                     "insert into data_rooms values (805,2,'LSRB B044A',NULL,NULL,'LSRB B044A (LABORATORY SVC)');",
                     "insert into data_rooms values (806,2,'LSRB B045',NULL,NULL,'LSRB B045 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (807,2,'LSRB B046',NULL,NULL,'LSRB B046 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (808,2,'LSRB B047',NULL,NULL,'LSRB B047 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (809,2,'LSRB B047A',NULL,NULL,'LSRB B047A (CIRCULATION AREA)');",
                     "insert into data_rooms values (810,2,'LSRB B048',NULL,NULL,'LSRB B048 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (811,2,'LSRB B049',NULL,NULL,'LSRB B049 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (812,2,'LSRB B050',NULL,NULL,'LSRB B050 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (813,2,'LSRB B051',NULL,NULL,'LSRB B051 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (814,2,'LSRB B052',NULL,NULL,'LSRB B052 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (815,2,'LSRB B053',NULL,NULL,'LSRB B053 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (816,2,'LSRB B054',NULL,NULL,'LSRB B054 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (817,2,'LSRB B055',NULL,NULL,'LSRB B055 (UNFINISHED)');",
                     "insert into data_rooms values (818,2,'LSRB B055A',NULL,NULL,'LSRB B055A (ANIMAL HOLDING)');",
                     "insert into data_rooms values (819,2,'LSRB B055B',NULL,NULL,'LSRB B055B (LABORATORY SVC)');",
                     "insert into data_rooms values (820,2,'LSRB B056',NULL,NULL,'LSRB B056 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (821,2,'LSRB B057',NULL,NULL,'LSRB B057 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (822,2,'LSRB B058',NULL,NULL,'LSRB B058 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (823,2,'LSRB B059',NULL,NULL,'LSRB B059 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (824,2,'LSRB B060',NULL,NULL,'LSRB B060 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (825,2,'LSRB B061',NULL,NULL,'LSRB B061 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (826,2,'LSRB B061A',NULL,NULL,'LSRB B061A (LABORATORY SVC)');",
                     "insert into data_rooms values (827,2,'LSRB B062',NULL,NULL,'LSRB B062 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (828,2,'LSRB B063',NULL,NULL,'LSRB B063 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (829,2,'LSRB B064',NULL,NULL,'LSRB B064 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (830,2,'LSRB B065',NULL,NULL,'LSRB B065 (HOLDING AREA)');",
                     "insert into data_rooms values (831,2,'LSRB B066',NULL,NULL,'LSRB B066 (ANIMAL HOLDING)');",
                     "insert into data_rooms values (832,2,'LSRB B067',NULL,NULL,'LSRB B067 (RECOVERY ROOM)');",
                     "insert into data_rooms values (833,2,'LSRB B068',NULL,NULL,'LSRB B068 (ELEVATOR MACH.)');",
                     "insert into data_rooms values (834,2,'LSRB B068A',NULL,NULL,'LSRB B068A (EQUIPMENT STORAGE)');",
                     "insert into data_rooms values (835,2,'LSRB B069',NULL,NULL,'LSRB B069 (TOILET)');",
                     "insert into data_rooms values (836,2,'LSRB B070',NULL,NULL,'LSRB B070 (CORRIDOR)');",
                     "insert into data_rooms values (837,2,'LSRB B071',NULL,NULL,'LSRB B071 (JANITORIAL)');",
                     "insert into data_rooms values (838,2,'LSRB B072',NULL,NULL,'LSRB B072 (EQUIPMENT STORAGE)');",
                     "insert into data_rooms values (839,2,'LSRB B073',NULL,NULL,'LSRB B073 (TOILET)');",
                     "insert into data_rooms values (840,2,'LSRB B0M01',NULL,NULL,'LSRB B0M01 (MECHANICAL RM)');",
                     "insert into data_rooms values (841,2,'LSRB B0M01A',NULL,NULL,'LSRB B0M01A (MECHANICAL)');",
                     "insert into data_rooms values (842,2,'LSRB B0M02',NULL,NULL,'LSRB B0M02 (BOILER RM)');",
                     "insert into data_rooms values (843,2,'LSRB B0M02A',NULL,NULL,'LSRB B0M02A (VESTIBULE)');",
                     "insert into data_rooms values (844,2,'LSRB B0M03',NULL,NULL,'LSRB B0M03 (ELECTRICAL RM)');",
                     "insert into data_rooms values (845,2,'LSRB B0M04',NULL,NULL,'LSRB B0M04 (TEL/DATA)');",
                     "insert into data_rooms values (846,2,'LSRB B0M05',NULL,NULL,'LSRB B0M05 (ELEVATOR MACHINE)');",
                     "insert into data_rooms values (847,2,'LSRB B0M06',NULL,NULL,'LSRB B0M06 (CONTROL RM)');",
                     "insert into data_rooms values (848,2,'LSRB B0M07',NULL,NULL,'LSRB B0M07 (EM POWER)');"]

    # Clear data_rooms table
    clearaccesstable("data_rooms")

    return sqlstatements


def createbiologyjobtitletable():
    sqlstatements = ["insert into code_biology_jobtitles (jobtypeid, jobtitle) values (1, 7, 'Academic Advisement Assistant');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (2, 3, 'Adjunct - Miscellaneous Title');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (3, 3, 'Adjunct Assistant Professor');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (4, 3, 'Adjunct Associate Professor');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (5, 3, 'Adjunct Professor');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (6, 3, 'Adjunct Research Associate Professor');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (7, 3, 'Adjunct Research Assistant Professor');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (8, 3, 'Adjunct Research Professor');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (9, 1, 'Assistant Professor');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (10, 1, 'Associate Professor');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (11, 6, 'Clerk');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (12, 6, 'Computer Analyst');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (13, 1, 'Department Chair');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (14, 4, 'Distinguished Teaching Professor');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (15, 12, 'Emeritus Faculty');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (16, 5, 'Graduate Student');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (17, 8, 'Instructional Support Assistant');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (18, 8, 'Instructional Support Associate');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (19, 8, 'Instructional Support Specialist');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (20, 8, 'Instructional Support Technician');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (21, 8, 'Lab Assistant');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (22, 2, 'Lecturer');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (23, 9, 'NERFI Personnel');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (24, 1, 'O'Leary Professor');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (25, 10, 'Postdoctoral Fellow');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (26, 1, 'Professor');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (27, 9, 'Research Assistant');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (28, 9, 'Research Associate');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (29, 9, 'Research Professor');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (30, 9, 'Research Scientist');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (31, 9, 'Research Support Specialist');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (32, 9, 'Research Technician');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (33, 13, 'RNA Institute - Administration');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (34, 13, 'RNA Institute - Scientific');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (35, 6, 'Secretary');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (36, 9, 'Senior Research Associate');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (37, 6, 'Senior Staff Assistant');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (38, 9, 'Visiting Scientist');",
                     "insert into code_biology_jobtitles (jobtypeid, jobtitle) values (39, 15, 'Visiting Student');"]

    # Clear data_rooms table
    clearaccesstable("code_biology_jobtitles")

    return sqlstatements


def update_documentfilepaths():
    sqlstatements = [
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Aberdale, Kayla_S20' where lastname='Aberdale' and firstname='Kayla';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Abrenica, Alleah_S20' where lastname='Abrenica' and firstname='Alleah';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Andrews, Jack_F20' where lastname='Andrews' and firstname='Jack';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Antonucci, Ryan_F20' where lastname='Antonucci' and firstname='Ryan';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Callanan, Melissa_S19' where lastname='Callanan' and firstname='Melissa';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Chenier, Mabel_F21' where lastname='Chenier' and firstname='Mabel';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_DeStefano, Kayla_F20' where lastname='DeStefano' and firstname='Kayla';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Frederick, Analysa_F19' where lastname='Frederick' and firstname='Analysa';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Hoyt, Christopher_F19' where lastname='Hoyt' and firstname='Christopher';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Lester, Sara_F20' where lastname='Lester' and firstname='Sara';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Loder, Morgan_S19' where lastname='Loder' and firstname='Morgan';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Monaghan, Brenna_F19' where lastname='Monaghan' and firstname='Brenna';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Montague, Samantha_F20' where lastname='Montague' and firstname='Samantha';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Rophael, Andrew_F21' where lastname='Rophael' and firstname='Andrew';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Rossetti, Erica_F21' where lastname='Rossetti' and firstname='Erica';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Shufelt, Cayleigh_F20' where lastname='Shufelt' and firstname='Cayleigh';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Tong, Danielle_F20' where lastname='Tong' and firstname='Danielle';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Uzzo, Riley_f18' where lastname='Uzzo' and firstname='Riley';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_VanLiew, Nicholas_F19' where lastname='VanLiew' and firstname='Nicholas';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Williams, Morgan_F18' where lastname='Williams' and firstname='Morgan';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\FOR_MS_Winston, Eric_F21' where lastname='Winston' and firstname='Eric';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Begum, Shelina_F20' where lastname='Begum' and firstname='Shelina';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Chery, Gaietchyne_F21' where lastname='Chery' and firstname='Gaietchyne';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_DeVeer, Theodora_F20' where lastname='DeVeer' and firstname='Theodora';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Dion, Tyler_F20' where lastname='Dion' and firstname='Tyler';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Fischer, Stephanie_S22' where lastname='Fischer' and firstname='Stephanie';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_George, Jenessa_F20' where lastname='George' and firstname='Jenessa';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Gonzalez, Bianca_F20' where lastname='Gonzalez' and firstname='Bianca';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Infantado, Danielle_S21' where lastname='Infantado' and firstname='Danielle';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Norkvests, Eduards_F20' where lastname='Norkvests' and firstname='Eduards';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Pendergast, Casey' where lastname='Pendergast' and firstname='Casey';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Pfister, Milan_F_F22' where lastname='Pfister' and firstname='Milan_F';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Rodriguez, Monica_F20' where lastname='Rodriguez' and firstname='Monica';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Sehta, Priyanka_F17' where lastname='Sehta' and firstname='Priyanka';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Shippas, Hanah_F20' where lastname='Shippas' and firstname='Hanah';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Teimouri, Melika_S22' where lastname='Teimouri' and firstname='Melika';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Torrens, Arthur_F20' where lastname='Torrens' and firstname='Arthur';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Tucotte, Madison_F20' where lastname='Tucotte' and firstname='Madison';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Wallace, Katina_F21' where lastname='Wallace' and firstname='Katina';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\MS_Wehrle, Patrick_F20' where lastname='Wehrle' and firstname='Patrick';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Adade, Emmanuel_S20' where lastname='Adade' and firstname='Emmanuel';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Affinnih, Nurat_F20' where lastname='Affinnih' and firstname='Nurat';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Aliyeva, Asmer_F21' where lastname='Aliyeva' and firstname='Asmer';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Altrieth, Amber_F16' where lastname='Altrieth' and firstname='Amber';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Amato, Rico_F20' where lastname='Amato' and firstname='Rico';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Assili, Sanam_S21' where lastname='Assili' and firstname='Sanam';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Badu, Pheonah_F18' where lastname='Badu' and firstname='Pheonah';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Bennink, Benjamin_S21' where lastname='Bennink' and firstname='Benjamin';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Bialousknia, Sean_F19' where lastname='Bialousknia' and firstname='Sean';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Breznak, Shane_F16' where lastname='Breznak' and firstname='Shane';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Brokowski, Carolyn_S21' where lastname='Brokowski' and firstname='Carolyn';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Brown, Deniece_S18' where lastname='Brown' and firstname='Deniece';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Dolphin, Nikki_F21' where lastname='Dolphin' and firstname='Nikki';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Dufflart, Jhos_F20' where lastname='Dufflart' and firstname='Jhos';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Durham, Serene_F17' where lastname='Durham' and firstname='Serene';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Ehrbar, Dylan_F21' where lastname='Ehrbar' and firstname='Dylan';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Frias, Jesus_F18' where lastname='Frias' and firstname='Jesus';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Gellatly, Victoria_F21' where lastname='Gellatly' and firstname='Victoria';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Gianola, Shawn_F19' where lastname='Gianola' and firstname='Shawn';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Golestanian, Afrooz_F20' where lastname='Golestanian' and firstname='Afrooz';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Hicks, Sawyer_S20' where lastname='Hicks' and firstname='Sawyer';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Hnin, Thet_F21' where lastname='Hnin' and firstname='Thet';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Hoff, Samantha_F17' where lastname='Hoff' and firstname='Samantha';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_John, Nimmy_F19' where lastname='John' and firstname='Nimmy';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Katreddi, Raghu_F18' where lastname='Katreddi' and firstname='Raghu';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Kaytes, Kristen_F21' where lastname='Kaytes' and firstname='Kristen';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Lemus, Alex_F19' where lastname='Lemus' and firstname='Alex';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Lin, Shu Jiu_F20' where lastname='Lin' and firstname='Shu Jiu';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_MacNeil, Haley_S22' where lastname='MacNeil' and firstname='Haley';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Martin, Elliot_F15' where lastname='Martin' and firstname='Elliot';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Mathias, Nicholas_F15' where lastname='Mathias' and firstname='Nicholas';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Mathur, Chetna_S21' where lastname='Mathur' and firstname='Chetna';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Matthews, JR_F19' where lastname='Matthews' and firstname='JR';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_McCann, Abby_F20' where lastname='McCann' and firstname='Abby';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Montoya Giraldo, Manuela_F22' where lastname='Montoya Giraldo' and firstname='Manuela';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Morrissey, Jennifer_S18' where lastname='Morrissey' and firstname='Jennifer';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Moskwa, Nicholas_F15' where lastname='Moskwa' and firstname='Nicholas';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Omeoga, Humphrey_S20' where lastname='Omeoga' and firstname='Humphrey';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Pena, Rafael_F20' where lastname='Pena' and firstname='Rafael';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Petroccione, Maurice_F17' where lastname='Petroccione' and firstname='Maurice';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Piper_Kathryn, Piper_F21' where lastname='Kathryn' and firstname='Piper';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Rosas, Esperanza_F21' where lastname='Rosas' and firstname='Esperanza';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Sarkar, Anwesha_F17' where lastname='Sarkar' and firstname='Anwesha';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Sarkar, Kahini_F17' where lastname='Sarkar' and firstname='Kahini';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Schroader, Jacob_F20' where lastname='Schroader' and firstname='Jacob';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Stella, Rosemary_F19' where lastname='Stella' and firstname='Rosemary';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Taroc, Ed Zandro_F18' where lastname='Taroc' and firstname='Ed Zandro';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Tavarez, Joey_F21' where lastname='Tavarez' and firstname='Joey';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Traver, Nicole_F20' where lastname='Traver' and firstname='Nicole';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Urman, Michelle_F20' where lastname='Urman' and firstname='Michelle';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Weston, Kennedi_F21' where lastname='Weston' and firstname='Kennedi';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Woodstock, Dana_F18' where lastname='Woodstock' and firstname='Dana';",
        "update data_persons set documentfilepath='O:\\Graduate\\Graduate Programs\\STUDENTS\\PhD_Zhang, Jing_S22' where lastname='Zhang' and firstname='Jing';",
        ]

    return sqlstatements


def create_university_jobtitles():

    sqlstatements = ["insert into code_university_jobtitles (jobtypeid, jobtitle) values (7, 'Academic Advisor');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Assistant Professor 10 Months');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Asso Prof 10');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Associate Professor   10 Month');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Associate Professor (10 Mo)');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Asst Prof 10');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (9, 'Bioinformatics Assistant');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Dist Prof & Dir Lf Sci Rch Bld');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Dstg Prof 10');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Instr Supp Spec & Dir Forensic');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Instrcl Support Tech');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Instrucl Supprt Assnt');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Instrucl Supprt Assoc');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Instrucl Supprt Spec');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Instructional Support Spec.');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Instructional Support Speclst');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Instructional Support Tech');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (3, 'Lect 10');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (3, 'Lect 12');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (3, 'Lecturer (10 Month)');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (9, 'Medicinal Chemistry Scientist');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (6, 'Office Assistant 1 (Keyboarding)');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (6, 'Office Assistant 1 (Keybrd)');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (9, 'Postdoctoral Associate');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (9, 'Postdrl Assoc');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Prof & Chair, Biological Sci');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Prof &Dir Ctr NeuroscnceResrch');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Professor  10 Months');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Professor 10 Month');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (1, 'Professor 10 Months');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (6, 'Programmer-Analyst');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (9, 'Research Assistant 08');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (9, 'Research Associate');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (9, 'Senior Staff Scientist');",
                     "insert into code_university_jobtitles (jobtypeid, jobtitle) values (6, 'Senr Staff Assnt');"]

    # Clear data_rooms table
    clearaccesstable("code_university_jobtitles")

    return sqlstatements


# Pull rows from tables of old database

def get_labs():
    mdb = r'c:\temp\BIO DEPT.mdb'
    drv = '{Microsoft Access Driver (*.mdb)}'
    pwd = 'pw'

    # connect to access db
    # con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(drv, mdb, pwd))
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = 'SELECT * FROM data_labs;'  # your query goes here
    rows = cur.execute(sql).fetchall()

    for row in rows:
        print("{0} - {1} - {2}".format(row[0],row[1],row[2]))

    cur.close()
    con.close()

    return rows


def get_labmembers(labkey):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT data_persons.id, data_persons.lastname, data_persons.firstname, code_labrole.role, data_lab_persons.labid "
    sql += "FROM (data_lab_persons INNER JOIN data_persons ON data_lab_persons.personid = data_persons.id) "
    sql += "INNER JOIN code_labrole ON data_lab_persons.labroleid = code_labrole.id "
    sql += "WHERE (((data_lab_persons.labid)={0})) ORDER BY data_persons.lastname;".format(str(labkey))

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    return rows


def get_requirements():
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT data_persons.id, data_persons.lastname, data_persons.firstname, code_labrole.role, data_lab_persons.labid "
    sql += "FROM (data_lab_persons INNER JOIN data_persons ON data_lab_persons.personid = data_persons.id) "
    sql += "INNER JOIN code_labrole ON data_lab_persons.labroleid = code_labrole.id "
    sql += "WHERE (((data_lab_persons.labid)={0})) ORDER BY data_persons.lastname;".format(str(labkey))

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    return rows


def get_labrooms(labkey):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT data_rooms.roomnumber "
    sql += "FROM data_lab_rooms INNER JOIN data_rooms ON data_lab_rooms.roomid = data_rooms.id "
    sql += "WHERE (((data_lab_rooms.labid)={0})) ORDER BY data_rooms.roomnumber;".format(str(labkey))

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    return rows


def get_labphones(labkey):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT data_lab_phones.phonenumber FROM data_lab_phones where data_lab_phones.labid = {0};".format(str(labkey))

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    return rows


def get_currentactivephdstudents():
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT data_person_olddb_requirements.*, data_person_olddb_requirements.CurDeg, "
    sql += "data_persons.active, data_persons.lastname FROM data_person_olddb_requirements INNER JOIN "
    sql += "data_persons ON data_person_olddb_requirements.PersonID = data_persons.id "
    sql += "WHERE (((data_person_olddb_requirements.CurDeg)='PhD') "
    sql += "AND ((data_persons.active)=True)) ORDER BY data_persons.lastname;"

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    return rows


def get_currentactivemsstudents():
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT data_person_olddb_requirements.*, data_person_olddb_requirements.CurDeg, "
    sql += "data_persons.active, data_persons.lastname FROM data_person_olddb_requirements INNER JOIN "
    sql += "data_persons ON data_person_olddb_requirements.PersonID = data_persons.id "
    sql += "WHERE (((data_person_olddb_requirements.CurDeg)='MS') "
    sql += "AND ((data_persons.active)=True)) ORDER BY data_persons.lastname;"

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    return rows


def get_officeroomnumber_by_personid(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT data_rooms.roomnumber "
    sql += "FROM code_roomtypes INNER JOIN ((data_persons INNER JOIN data_person_rooms "
    sql += "ON data_persons.id = data_person_rooms.personid) "
    sql += "INNER JOIN data_rooms ON data_person_rooms.roomid = data_rooms.id) "
    sql += "ON code_roomtypes.id = data_person_rooms.roomusetype "
    sql += "WHERE (((data_persons.id)={0}) AND ((code_roomtypes.roomtype)='Office'));".format(str(personid))

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return ""


def get_officephone_by_personid(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT data_person_phones.phonenumber "
    sql += "FROM code_phonetypes INNER JOIN data_person_phones ON code_phonetypes.id = data_person_phones.phonetypeid "
    sql += "WHERE (((data_person_phones.personid)={0}) AND ((code_phonetypes.phoneclassname)='Office'));".format(str(personid))

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return ""


def GetAdvisorNameForStudent(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT data_persons.firstname, data_persons.lastname "
    sql += "FROM data_person_academicadvisors INNER JOIN data_persons ON "
    sql += "data_person_academicadvisors.advisorid = data_persons.id "
    sql += "WHERE (((data_person_academicadvisors.adviseeid)={0}));".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return "{0} {1}".format(rows[0][0], rows[0][1])
    else:
        return ""


def GetEntryDateForStudent(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT Format([data_person_olddb_requirements.EntryDT], 'mm/dd/yyyy') as Expr1 " \
          "FROM data_person_olddb_requirements "
    sql += "where personid={0};".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return ""


def GetStatuteEndForStudent(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT [Statute End] " \
          "FROM data_person_olddb_requirements "
    sql += "where personid={0};".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return str(int(rows[0][0]))
    else:
        return ""


def GetCoreAreaForStudent(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT Core " \
          "FROM data_person_olddb_requirements "
    sql += "where personid={0};".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return ""


def GetApprovalOfTopicForStudent(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT [Approval of Topic] " \
          "FROM data_person_olddb_requirements "
    sql += "where personid={0};".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return ""


def GetMCDNAdvancedLectureForStudent(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT [MS/PHD Adv Lecture 1] " \
          "FROM data_person_olddb_requirements "
    sql += "where personid={0};".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return ""


def GetBIO681CompleteForStudent(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT [681 Seminar COmplete] " \
          "FROM data_person_olddb_requirements "
    sql += "where personid={0};".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return ""


def GetTeaching1ForStudent(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT Teaching1 " \
          "FROM data_person_olddb_requirements "
    sql += "where personid={0};".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return ""


def GetTeaching2ForStudent(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT Teaching2 " \
          "FROM data_person_olddb_requirements "
    sql += "where personid={0};".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return ""


def GetSelectCommitteeForStudent(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT [Select Committee] FROM data_person_olddb_requirements "
    sql += "where personid={0};".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return ""


def GetAdvanceToCandidacy(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT [Advance to Candidacy] FROM data_person_olddb_requirements "
    sql += "where personid={0};".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return ""


def GetTool(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT tool FROM data_person_olddb_requirements "
    sql += "where personid={0};".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return ""


def GetCoreExamSemesterResults(personid):
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\biologydatabase.mdb;')
    cur = con.cursor()

    sql = "SELECT data_person_olddb_requirements.[Exam1 Semester], data_person_olddb_requirements.[Exam1 Results], "
    sql += "data_person_olddb_requirements.[Exam II Semester], data_person_olddb_requirements.[Exam II Result] "
    sql += "FROM data_person_olddb_requirements WHERE (((data_person_olddb_requirements.PersonID)={0}));".format(personid)

    print(sql)

    rows = cur.execute(sql).fetchall()

    cur.close()
    con.close()

    returnlist = []

    if len(rows) > 0:
        returnlist.append(rows[0][0])
        returnlist.append(rows[0][1])
        returnlist.append(rows[0][2])
        returnlist.append(rows[0][3])
        return returnlist
    else:
        returnlist.append('')
        returnlist.append('')
        returnlist.append('')
        returnlist.append('')
        return returnlist


def get_old_access_db_address_records():
    mdb = 'c:/temp/BIO DEPT.mdb'
    drv = '{Microsoft Access Driver (*.mdb)}'
    pwd = 'pw'

    # connect to access db
    # con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(drv, mdb, pwd)
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\BIO DEPT.mdb;')
    cur = con.cursor()

    sql = "SELECT * FROM [Mailing List 05];"

    try:
        rows = cur.execute(sql).fetchall()
    except Exception as e:
        print(e)

    cur.close()
    con.close()

    return rows


def get_old_access_db_profile_records():
    mdb = 'c:/temp/BIO DEPT.mdb'
    drv = '{Microsoft Access Driver (*.mdb)}'
    pwd = 'pw'

    # connect to access db
    # con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(drv, mdb, pwd))
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\BIO DEPT.mdb;')
    cur = con.cursor()

    sql = "SELECT * FROM tblgsPROFILE;"

    try:
        rows = cur.execute(sql).fetchall()
    except Exception as e:
        print(e)

    cur.close()
    con.close()

    return rows


#  Utilities for creating/updating code tables

def clearaccesstable(tablename):
    mdb = 'c:/temp/BiologyDatabase.mdb'
    drv = '{Microsoft Access Driver (*.mdb)}'
    pwd = 'pw'

    # connect to access db
    try:
        # con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}'DBQ=c:\Temp\BiologyDatabase.mdb;')
        con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\BiologyDatabase.mdb;')
        cur = con.cursor()
    except Exception as e:
        print(str(e))

    sql = "DELETE * from {0};".format(tablename)

    try:
        cur.execute(sql)
        con.commit()
    except Exception as e:
        print(str(e))


# def executecommandagainstdestinationdatabase(sqlcommandstring):
#     mdb = 'c:/temp/BiologyDatabase.mdb'
#     drv = '{Microsoft Access Driver (*.mdb)}'
#     pwd = 'pw'
#
#     # connect to access db
#     con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(drv, mdb, pwd))
#     cur = con.cursor()
#
#     try:
#         cur.execute(sqlcommandstring)
#         con.commit()
#     except Exception as e:
#         print(str(e))
#
#     cur.close()
#     con.close()


def execute_commands_against_destination_database(sqlcommandstrings):
    mdb = r'c:\temp\BiologyDatabase.mdb'
    drv = '{Microsoft Access Driver (*.mdb)}'
    pwd = 'pw'

    # con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(drv, mdb, pwd))
    con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Temp\BiologyDatabase.mdb;')
    cur = con.cursor()

    for sqlstatement in sqlcommandstrings:
        # print(sqlstatement)
        try:
            cur.execute(sqlstatement)
            con.commit()
        except Exception as e:
            print(e)

    cur.close()
    con.close()


# General Utilities

def return_valid_date(inputvalue):
    print(type(inputvalue))

    if type(inputvalue) != datetime.datetime: return ""

    year = inputvalue.strftime("%Y")
    month = inputvalue.strftime("%m")
    day = inputvalue.strftime("%d")

    return "{1}/{0}/{2}".format(day, month, year)
