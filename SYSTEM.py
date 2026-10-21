#making a backend system for school
#making a function for each indivisual task
import os
os.path.exists(f"gta5")
#os is a library
#os is a function
#os is present on local computer

import datetime
#FEE DATA.txt
# def ROLL_TO_DATA(CLASS,SECTION,ROLL):
#     if os.path.exists(f"{CLASS}{SECTION}"):
#         A = open(f"{CLASS}{SECTION}","r")
#         for i in A.readlines():
#             if i[i.find()]

def NUMBER_MONTH(A):
    if str(A) == "01":
        return("JANURAY")
    elif str(A) == "02":
        return("FEBRUARY")
    elif str(A) == "03":
        return("MARCH")
    elif str(A) == "04":
        return("APRIL")
    elif str(A) == "05":
        return("MAY")
    elif str(A) == "06":
        return("JUNE")
    elif str(A) == "07":
        return("JULY")
    elif str(A) == "08":
        return("AUGUST")
    elif str(A) == "09":
        return("SEPTEMBER")
    elif str(A) == "10":
        return("OCTUBER")
    elif str(A) == "11":
        return("NOVEMBER")
    elif str(A) == "12":
        return("DECEMBER")

def SUBJECTS(A,B="NA"):
    if str(A).upper() in ["NURSERY","PG","PLAY GROUP","UKG","LKG","1","2","3","4","5","6","7","8"] and str(B.capitalize()) == "NA":
        return ["English",
                "Hindi",
                "Mathematics",
                "Environmental Studies ",
                "General Knowledge",
                "Computer",
                "Art",
                "Music",
                "Physical Education",
                "Moral Science",
                "Sanskrit"]
    
    elif str(A).upper() in ["9","10"] and B == "NA":
        return ["English",
                "Hindi",
                "Mathematics",
                "Science",
                "Social Science",
                "Information Technology"
                "Computer Applications",
                "Art Education",
                "Health & Physical Education",
                "Work Education"]
    if str(A).upper() in ["11","12"] and B == "PCM":
        return ["English Core",
                "Physical Education",
                "Computer Science",
                "Informatics Practices",
                "Physics",
                "Chemistry",
                "Maths"]
    elif str(A).upper() in ["11","12"] and B == "PCB":
        return ["English Core",
                "Physical Education",
                "Computer Science",
                "Informatics Practices",
                "Physics",
                "Chemistry",
                "Biology"]
    elif str(A).upper() in ["11","12"] and B == "COMMERCE":  
        return ["English Core",
                "Physical Education",
                "Computer Science",
                "Informatics Practices",
                "Accountancy",
                "Business Studies",
                "Economics",
                "Applied Mathematics",
                "Entrepreneurship"] 
    elif str(A).upper() in ["11","12"] and B == "ARTS":
        return[ "English Core",
                "Physical Education",
                "Computer Science",
                "Informatics Practices",
                "History",
                "Political Science",
                "Geography",
                "Psychology",
                "Sociology",
                "Philosophy",
                "Home Science",
                "Legal Studies",
                "Fine Arts",
                "Fashion Studies",
                "Media Studies"]
    else:
        return[ "English",
                "Hindi",
                "Mathematics",
                "Environmental Studies ",
                "General Knowledge",
                "Computer",
                "Art",
                "Music",
                "Physical Education",
                "Moral Science",
                "Sanskrit"]

def EXAM_TYPE(): 
    #     print("\t '1' FOR PERODIC TEST 1:")
    #     print("\t '2' FOR PERODIC TEST 2:")
    #     print("\t '3' FOR HALF YEARLY EXAMINATION:")
    #     print("\t '4' FOR PERODIC TEST 3:")
    #     print("\t '5' FOR PERODIC TEST 4:")
    #     print("\t '6' FOR FINAL EXAMINATION:")
    #     print("\t '7' FOR PEN PAPER TESTS")
    print("")
    print("ENTER: ")
    print("\t '1' FOR PERODIC TEST 1:")
    print("\t '2' FOR PERODIC TEST 2:")
    print("\t '3' FOR HALF YEARLY EXAMINATION:")
    print("\t '4' FOR PERODIC TEST 3:")
    print("\t '5' FOR PERODIC TEST 4:")
    print("\t '6' FOR FINAL EXAMINATION:")
    print("\t '7' FOR PEN PAPER TESTS")
    print("")
    A = (int)(input("ENTER HERE!: "))
    if A == 1:
        return "PERODIC TEST 1"  
    elif A == 2:
        return "PERODIC TEST 2"  
    elif A == 3:
        return "HALF YEARLY EXAMINATION"
    elif A == 4:
        return "PERODIC TEST 3"
    elif A == 5:
        return "PERODIC TEST 4"
    elif A == 6:
        return "FINAL EXAMINATION"
    elif A == 7:
        return "PEN PAPER TESTS"
    else:
        return None
       
def ADMISSION():
    STUDENT_INFO = open("STUDENTS.txt","a")
    print("")
    print("\tADDING A NEW STUDENT IN THE DATA BASE:")
    print("")
    print("\tWRITE 'NA' TO SKIP")
    print("")
    NAME = (input)("ENTER THE NAME OF THE STUDENT: ")
    GEN = (input("ENTER HIS GENDER: ('M' FOR MALE AND 'F' FOR FEMALE): "))
    ADHAR = (int)(input("ENTER HIS ADHAR CARD NUMBER: "))
    if len(str(ADHAR)) != 12:
        print("\tINVALID ADHAR NUMBER!") 
    print("e.g. FOR DOB: DD \ MM \ YYYY")
    DOB = (input)("ENTER HIS DOB: ")
    AGE = "to be evaluated"
    CLAS = (int)(input("ENTER HIS CLASS: "))
    F_N = (input("ENTER HIS FATHERS NAME: "))
    if F_N != "NA":
        F_DOB = (input("ENTER HIS FATHRS DOB: "))
        F_ADHAR = (int)(input("ENTER HIS FATHERS ADHAR NUMBER: "))
        if len(str(F_ADHAR)) != 12:
            print("\tINVALID ADHAR NUMBER!") 
        F_O = (input("ENTER HIS FATHERS OCCUPATION: "))
    else:
        F_DOB,F_ADHAR,F_O = "NA","NA","NA"     
    M_N = (input("ENTER HIS MOTHERS NAME: "))
    if M_N != "NA":
        M_DOB = (input("ENTER HIS MOTHER'S DOB: "))
        M_ADHAR = (int)(input("ENTER HIS MOTHER'S ADHAR NUMBER: "))
        if len(str(M_ADHAR)) != 12:
            print("\tINVALID ADHAR NUMBER!") 
        M_O = (input("ENTER HIS MOTHER'S OCCUPATION: "))
    else:
        M_DOB,M_ADHAR,M_O = "NA","NA","NA"    
    BRO = []
    SIS = []
    N_BRO = (int)(input("HOW MANY BROTHERS HE HAVE? "))
    N_SIS = (int)(input("HOW MANY SISTER HE HAVE?: "))
    for i in range(1,(N_BRO+1)):
        B_N = (input(f"ENTER HIS {i} BRO NAME: "))
        BRO.append(B_N)
    for i in range(1,(N_SIS+1)):
        S_N = (input(f"ENTER HIS {i} SIS NAME: "))
        SIS.append(S_N)
    STUDENT_ID = f"{GEN}{ADHAR}"
    TO_BE_SAVED = [] 
    CONT = (int)(input("HOW MANY CONTACT NUMBER'S YOU WANNA PROVIDE?: "))
    CONTACT = ""
    for i in range(1,(CONT+1)):
        ASK_2 = (int)(input(f"ENTER YOUR PHONE NUMBER {i} : "))
        CONTACT += " " +str(ASK_2)
    ASK_1 = (input("PRESS ENTER TO SAVE!:"))
    print(f"STUDENT ID IS: {STUDENT_ID}")
    if ASK_1 == "":
        print("\tSAVING THE DATA OF STUDENT")
        STUDENT_INFO.write("\n"+f"{STUDENT_ID} : NAME: {NAME.title()} GENDER: {GEN.capitalize()} CLASS: {CLAS} DOB: {DOB} AGE: {AGE} "
                           f"FATHER NAME: {F_N.title()} FATHER OCCUPATION: {F_O.title()} FATHER ADHAR: {F_ADHAR} FATHER DOB: {F_DOB} "
                           f"MOTHER NAME: {M_N.title()} MOTHER OCCUPATION: {M_O.title()} MOTHER ADHAR: {M_ADHAR} MOTHER DOB: {M_DOB} "
                           f"BOTHER: {str(BRO).removesuffix("]").removeprefix("[")} "
                           f"SISTER: {str(SIS).removesuffix("]").removeprefix("[")} "
                           f"CONTACT NUMBER: {CONTACT} "
                           f"DATA ENTRY AT: {datetime.datetime.now()} ")
        print("\tDATA SAVED")
        STUDENT_INFO.close()
    else:
        print("DATA DISCARDED!")  
        STUDENT_INFO.close()       

#aloting class  
#M123455678901 : NAME: Saksham Bhardwaj GENDER: M CLASS: 12 DOB: 23/4/1990 AGE: to be evaluatedFATHER NAME: Ankit FATHER OCCUPATION: Doctor FATHER ADHAR: 111111111111 FATHER DOB: 3/9/1980MOTHER NAME: Asha MOTHER OCCUPATION: House Wife MOTHER ADHAR: 109238417321 MOTHER DOB: 3/2/1985BOTHER: 'asdgha', 'alsjg'SISTER: 'osduifgoas', 'jsdauogtf'DATA ENTRY AT: 2025-08-14 11:04:07.362278  
def ALOT_CLASS(): #tested OK
    SCHOOL_DIC = {"12A":1}
    TEST_2 = False
    SECTION = ""
    SEC = 0
    TEST = False
    NEW_DATA = ""
    DATA = open("STUDENTS.txt","r+")
    STUDENT_ID = (input("ENTER STUDENT ID: "))
    if len(STUDENT_ID) != 13:
        print("INVALID STUDENT ID")
    else:
        MARKS = (float)(input("HOW MUCH OVERALL PERCENTAGE HE GOT IN PREVIOUS CLASS: "))
        CLAS = (int)(input("ENTER THE CLASS NO. IN WHICH YOU WANT TO PLACE THE STUDENT: "))
        print("")
        print("\tLOCATING THE SLOT:")
        DATA.seek(0)
        for i in DATA.readlines():
            if i[0:13] == STUDENT_ID:
                NEW_DATA = i
                print("STUDENT FOUND IN DATA BASE!")
                DATA.seek(0)
                TEST = True
                break
        if TEST != True:
            print(f"NO STUDENT WITH ID: {STUDENT_ID}") 
            print(f"CHECK THE ID AGAIN OR ADD THE STUDENT IN THE DATA BASE ")  
            print("")
        elif TEST == True:
            CLAS_INDEX = NEW_DATA.find(f"CLASS:")
           
            if os.path.exists(f"{str(CLAS)}A.txt"):
                print("THE CLASS IS AVAILBLE!")
                CLASS = open(f"{str(CLAS)}A.txt","a+")
                CLASS.seek(0)
            else:
                print(f"NO CLASS {CLAS} EXISTS")
                print("CREATING NEW CLASS")
                CLASS = open(f"{str(CLAS)}A.txt","w+")

            R = len(CLASS.readlines())
            print(f"TOATL STUDENTS IN THIS CLASS IS: {R}")
            ASK_2 = (input("DO YOU STILL WANT TO ADD HIM IN CLASS: (PRESS ENTER FOR YES): "))
            print("")
            if ASK_2 == "":
                
                print("\tALLOTING HIM THIS CLASS")
                if R == 0:
                     CLASS.write(NEW_DATA.removesuffix("\n")+ "\tROLL NO: " + str(1) + "STUDENT ADDED AT: " + str(datetime.datetime.now()))
                     TEST_2 = True
                else:
                     CLASS.seek(0)
                     R = len((CLASS).readlines())+1
                     CLASS.seek(0,2)
                     CLASS.write("\n"+NEW_DATA.removesuffix("\n")+ "\tROLL NO: " + str(R+1) + "STUDENT ADDED AT: " + str(datetime.datetime.now()))
                     TEST_2 = True
                print("CLASS ALOTED TO:")
                CLASS.seek(0)
                print(f"STUDENT ID: {STUDENT_ID} , {NEW_DATA[(NEW_DATA.find("NAME:")):(NEW_DATA.find("GENDER:"))].removesuffix("\n")} with roll no. {str(len((CLASS).readlines()))}")
                print("")

                DATA.close()
            else: 
               #find total no. of sections:
                print("FINDING TOTAL NUMBER OF SECTIONS FOR THIS CLASS:")
                LAST_SECTION = ""
                for i in range(ord("B"),(ord("Z")+1)):
                    if os.path.exists(f"{str(CLAS)}{str(chr(i))}.txt"):
                        SEC += 1
                        FILE_t = open(f"{str(CLAS)}{str(chr(i))}.txt","a+")
                        FILE_t.seek(0)
                        R = len(FILE_t.readlines())
                        print("")
                        print(f"CLASS {CLAS} HAS SECTION: {chr(i)}")
                        print(f"THIS CLASS HAS {R} STUDENTS ")
                        print("")
                        ASK_4 = (input("PRESS 'ENTER' TO ADD HIM HERE: "))
                        if ASK_4 == "":
                            TEST_2 = True
                            print("")
                            print("\tADDING HIM TO THIS CLASS")
                            CLAS_INDEX = NEW_DATA.find(f"CLASS:")
                            FILE_t.seek(0,2)
                            FILE_t.write("\n" + NEW_DATA.removesuffix("\n")+ "\tROLL NO:" + str(R+1) + "STUDENT ADDED AT: " + str(datetime.datetime.now()))
                            print("CLASS ALOTED TO:")
                            print(f"STUDENT ID: {STUDENT_ID} , {NEW_DATA[NEW_DATA.find("NAME:"):NEW_DATA.find("GENDER:")]} "
                                  f" with roll no. {R+1}"
                                  )
                            DATA.close()
                            break
                    else:
                        LAST_SECTION = chr(i)
                        break

                if TEST_2 == False:
                    print("")
                    print("\tSTUDENT IS NOT PLACED YET!")
                    ASK_5 = (input("DO YOU WANT TO CREATE A NEW SECTION?: (ENTER FOR 'YES'):"))
                    if ASK_5 == "":
                        CLAS_INDEX = NEW_DATA.find(f"CLASS:{CLAS-1}")
                        print("")
                        print(f"CREATING NEW SECTION: {CLAS,LAST_SECTION}") 
                        FILE_t = open(f"{CLAS}{LAST_SECTION}.txt","w+")
                        print("ADDING HIM TO THIS CLASS:")
                        
                        FILE_t.write(NEW_DATA.removesuffix("\n")+ "\tROLL NO: " + str(len(FILE_t.readlines())+1) + "STUDENT ADDED AT: " + str(datetime.datetime.now()))
                        print("\tCLASS ALOTED TO:")
                        print(f"STUDENT ID: {STUDENT_ID} , {NEW_DATA[NEW_DATA.find("NAME:"):NEW_DATA.find("GENDER:")]}"
                            f" with roll no. {len(FILE_t.readlines())+1}"
                                )
                        DATA.close()
                    else:
                         print("")
                         print("SOORY! WE CANT PLACE HIM :(")                      

#FEE RECIPTS AND STRUCTURES:
#not tested
def FEE_PROCEDURE(): #TESTED OK
    TEST = False
    TEST_2 = False
    REC = False
    FEE_INFO = open("RECIPT NUMBER.txt","a+")
    DATA = open("STUDENTS.txt","r")
    STUDENT_ID = (input("ENTER THE STUDENT ID: "))
    if len(STUDENT_ID) != 13:
        print("INVALID STUDENT ID")
    else:
        for i in DATA.readlines():
            if i[0:13] == STUDENT_ID:
                NEW_DATA = i
                print("\tSTUDENT FOUND IN DATA BASE!")
                TEST = True 
                break       

        for i in FEE_INFO.readlines():
            if i[0:13] == STUDENT_ID:
                print("STUDENT HAVE PREVIOUS FEE RECORD")
                TEST_2 = True
                PAY_DATA = i
                break
        if TEST == True and TEST_2 == True:
            print("ELIGIBLE TO PAY FEE")
            PAY = True
            REC = True
        elif TEST == False:
            print("")
            print(f"NO STUDENT WITH ID: {STUDENT_ID} WAS FOUND IN THE DATA BASE:")
            print("\t REASON:")
            print("\t\tNOT REGISTERED IN SCHOOL DATA BASE")
            print("\t\tID IS WRONG")
            PAY = False
        elif TEST == True and TEST_2 == False:
            print("")
            print(f"THERE IS NO FEE BACKGROUND FOR THIS STUDENT")
            print(f"YOU CAN STILL CREATE BY PAYING FOR 1ST TIME")
            TEST_2 = False
            PAY = True
            REC = False
        if PAY == True:
            print("PLEASE CHECK THE FOLLOWING DETAILS OF STUDENT:")
            print(f"\t {NEW_DATA[NEW_DATA.find("NAME"):(NEW_DATA.find("GENDER"))]}")  
            print(f"\t {NEW_DATA[NEW_DATA.find("GENDER"):(NEW_DATA.find("DOB"))]}")
            print(f"\t {NEW_DATA[NEW_DATA.find("FATHER NAME:"):(NEW_DATA.find("FATHER OCCUPATION"))]}")
            print("") #M123455678901 : FEE PAYED: 2000 _ DETAILS: PAYED AT: 2025-08-14 11:04:07.362278 METHOD: CASH RECIPT NUMBER: 1 _
            if REC == True:
                print("PREVIOUS PAYMENT HISTORY:")
                print(f"{PAY_DATA[PAY_DATA.find("FEE PAYED:"):PAY_DATA.find("_")]}")   
                print(f"{PAY_DATA[PAY_DATA.find("PAYED AT:"):PAY_DATA.find("METHOD:")]}")
                print(f"{PAY_DATA[PAY_DATA.find("METHOD"):PAY_DATA.find("RECIPT NUMBER")]}")
                print(f"{PAY_DATA[PAY_DATA.find("RECIPT NUMBER"):PAY_DATA.find("_")]}")
                print("")     
            AMT = (int)(input("ENTER THE AMOUNT YOU WANT TO PAY: ")) 
            print("\tENTER:")
            print("\t\t 1 FOR CASH")
            print("\t\t 2 FOR ONLINE")
            PAY_METHOD = (int)(input("ENTER MODE HERE: "))
            if PAY_METHOD == 1:
                PAY_METHOD = "CASH"
                TRANS_ID = f"NA ({datetime.datetime.now()})"
            elif PAY_METHOD == 2:
                PAY_METHOD = "ONLINE"
                TRANS_ID = (int)(input("ENTER TRANSECTION ID: "))
                TRANS_ID + f"({datetime.datetime.now()})"
            else:#M123455678901 : FEE PAYED: 2000 _ DETAILS: PAYED AT: 2025-08-14 11:04:07.362278 METHOD: CASH RECIPT NUMBER: 1 _
                print("INVALID SYNTAX :(")        
            NOW = datetime.datetime.now()
              #1 : M123455678901 : FEE PAYED: 2000 
            DATA.close()
            # for i in COPY:
            #     if i[0:14] == STUDENT_ID:
            #         i = CHANGE
            #     FILE.write(f"{i}")
            # print("")
            print("'ENTER' TO CONCIDER THESE CRITE AREAS IN THE FEE: ")
            ASK_1 = (input("BUS FEE: "))
            ASK_2 = (input("TUTION FEE: "))
            ASK_3 = (input("ACTIVITY + COM. + PHE + LAB: "))
            ASK_4 = (input("DIARY + LIBRARY CARD: "))
            ASK_5 = (input("BOARD FEE + EXAMINATION FEE: "))    
            ASK_6 = (input("LATE FEE: "))
            ASK_7 = (input("ADMISSION FEE: "))
            CRITE = ""
            if ASK_1:
                CRITE+= " BUS "
            if ASK_2:
                CRITE+= "TUTION FEE"
            if ASK_3:
                CRITE+= " ACTIVITY + COM. + PHE + LAB "
            if ASK_4:
                CRITE+= " DIARY + LIBRARY CARD "
            if ASK_5:
                CRITE+= " BOARD FEE + EXAMINATION FEE "
            if ASK_6:
                CRITE+= " LATE FEE "
            if ASK_7:
                CRITE+= " ADMISSION FEE "      
            FEE_INFO.seek(0)
            #1 : M123455678901 : FEE PAYED: 2000 NEFT NUMBER: 3264732 FIELDS:            
            FEE_INFO.write(f"\n{len(FEE_INFO.readlines())+1} : {STUDENT_ID} : FEE PAYED: {AMT} NEFT NUMBER: {str(TRANS_ID)} FIELDS: {CRITE} ") 
            print("")
            FEE_INFO.seek(0)
            print(f"\nFEE STATUS:")
            print(f"STUDENT WITH ID: {STUDENT_ID} AND NAME: {NEW_DATA[NEW_DATA.find("NAME"):(NEW_DATA.find("GENDER"))]}")
            print(f"WHOSE {NEW_DATA[NEW_DATA.find("FATHER NAME:"):(NEW_DATA.find("FATHER OCCUPATION"))]}")
            print(f"HAVE PAID RUPEE: {AMT}/- ON DATE: {NOW}")
            print(f"YOUR RESPECTIVE RECIPT NUMBER IS {len(FEE_INFO.readlines())}")
            print("THANK YOU!")
            print("")
            print("DONE STORING THE DATA!")
            FEE_INFO.close()    

def RESULT_CREATE(): 
    EXAM_NAME = EXAM_TYPE()
    CLAS = (input("ENTER THE CLASS (NUMBER ONLY!): "))
    SECTION = (input("ENTER THE SECTION (ALPHABET ONLY!): "))
    BATCH = int(input("ENTER THE 'YEAR' WHEN THE YEAR WAS STARTED: (i.e 2009): "))
    T1 = False
    T2 = False
    if os.path.exists(f"{str(CLAS)}{str(SECTION)}.txt"):
        print("CLASS FOUND IN THE DATA BASE!")
        DATA = open(f"{CLAS}{SECTION}.txt", "r")
        T1 = True
        if CLAS in ["NURSERY","PG","PLAY GROUP","UKG","LKG","1","2","3","4","5","6","7","8","9","10"]:
             STREAM = "NA"
             SUBJECT = SUBJECTS(str(CLAS),STREAM)
        else: #
            print("\t ENTER FROM THE FOLLOWING STREAM:")
            print("'PCM' FOR MATHS SECTION")
            print("'PCB' FOR BIO SECTION")
            print("'COMMERCE' FOR COMMERCE SECTION")
            print("'ARTS' FOR ARTS/HUMANITIES SECTION")
            STREAM = (input("ENTER HERE: "))    
            SUBJECT = SUBJECTS(str(CLAS),STREAM)    
    
        if os.path.exists(f"{EXAM_NAME} of class {CLAS}{SECTION} BATCH {BATCH}-{int(BATCH)+1}.txt") == False:
            T2 = True
            EXAM = open(f"{EXAM_NAME} of class {CLAS}{SECTION} BATCH {BATCH}-{int(BATCH)+1}.txt","w+")       
        else:
            print("RESULTS ARE ALREADY FILLED.")      
        if T1 == True and T2 == True:
            print("DONE CHECKING!")
            print("")
            MAX = (int)(input("ENTER THE MAXIMUM MARKS: "))
            DATA.seek(0)
            print("\tPLEASE CHECK THE FOLLOWING DATA TO CONTINUE:")
            print(f"")
            print(f"CLASS: {CLAS} AND SECTION: {SECTION}")
            print(f"THIS CLASS HAVE {len(DATA.readlines())} STUDENTS")
            print("")
            ASK1 = (input("PRESS ENTER TO CONTINUE!"))
            DATA.seek(0)
            print("")
            print("PLEASE READ:")
            print("PRESS 'ENTER' IF THE SUBJECT IS NOT APPLICABLE FOR THAT STUDENT")
            print("ENTER 'A' IF THE STUDENT WAS ABSENT IN THAT TEST")
            ASK2 = (input("PRESS 'ENTER' TO CONTINUE: "))
            TO_BE_WRITTEN = []
            WRITTEN = ""
            print("")
            for i in DATA.readlines():
                print("\n")
                PER = []
                print(f"\tSTUDENT {i[i.find("NAME:"):i.find("GENDER")]}")
                print(f"\tSTUDENT {i[i.find("ROLL NO:"):i.find("STUDENT ADDED AT:")]}")
                WRITTEN = i[:i.find("AGE")] + " " +i[i.find("ROLL NO:"):i.find("STUDENT ADDED AT:")] + " SUBJECTS: " 
                for a in SUBJECT:
                    ASK3 = (input(f"ENTER MARKS IN {a}: "))
                    if ASK3 != "" and ASK3 != "A":
                        WRITTEN += f"MARKS IN {a}: {ASK3} "
                        PER.append(float(ASK3))
                    elif ASK3 == "A":
                        WRITTEN += f"MARKS IN {a}: ABSENT "
                if len(PER) == 0:
                    PER.append(1)
                    
                TO_BE_WRITTEN.append(f"{str(WRITTEN)} PERCENTAGE SECURED: {str(sum(PER)*100/(len(PER)*MAX))} \n")
            for i in TO_BE_WRITTEN:    
                EXAM.write(i)
            EXAM.close()
            DATA.close()
            print("")
            print("DATA SAVED!")

    else:
        print(f"NO CLASS {CLAS} WITH SECTION {SECTION} EXISTS IN DATA BASE!")

#FINDING RESULT
def FIND_RESULT():
    print("ENTER:")
    print("\t1 TO GET WHOLE CLASS RESULT")
    print("\t2 TO GET LIST OF RANKING STUDENTS FROM ALL SECTIONS OF CLASS")
    print("\t3 TO GET LIST OF RANKING STUDENTS FROM ANY SECTION OF CLASS")
    print("\t4 TO GET RESULT OF ANY STUDENT")
    SUBJECTS = [
    # Classes 1–5 (Primary)
    "English",
    "Hindi",
    "Mathematics",
    "Environmental Studies ",
    "General Knowledge",
    "Computer",
    "Art",
    "Music",
    "Physical Education",
    "Moral Science",
    "Sanskrit",

    # Classes 6–8 (Middle)
    "English",
    "Hindi",
    "Mathematics",
    "Science",
    "Social Science",
    "Sanskrit",
    "Computer Science",
    "Art",
    "Music",
    "Physical Education",
    "General Knowledge",
    "Moral Science",

    # Classes 9–10 (Secondary, core as per CBSE)
    "English",
    "Hindi",
    "Mathematics",
    "Science",
    "Social Science",
    "Information Technology",
    "Computer Applications",
    "Art Education",
    "Health & Physical Education",
    "Work Education",

    # Classes 11–12 (Senior Secondary, Streams)
    # Compulsory
    "English Core",
    "Physical Education",
    "Computer Science"
    "Informatics Practices",
    "Fine Arts",
    "Music",
    "Dance",
    "Theatre",
    "Entrepreneurship",
    "Psychology",
    "Sociology",
    "Philosophy",
    "Home Science",
    "Legal Studies",
    "Economics",

    # Science Stream
    "Physics",
    "Chemistry",
    "Mathematics",
    "Biology",
    "Engineering Graphics",
    "Biotechnology",
    "Geography",

    # Commerce Stream
    "Accountancy",
    "Business Studies",
    "Economics",
    "Applied Mathematics",
    "Entrepreneurship",

    # Humanities/Arts Stream
    "History",
    "Political Science",
    "Geography",
    "Psychology",
    "Sociology",
    "Philosophy",
    "Home Science",
    "Legal Studies",
    "Fine Arts",
    "Fashion Studies",
    "Media Studies"]
    #  print("\t1 TO GET WHOLE CLASS RESULT")
    # print("\t2 TO GET LIST OF RANKING STUDENTS FROM ALL SECTIONS OF CLASS")
    # print("\t3 TO GET LIST OF RANKING STUDENTS FROM ANY SECTION OF CLASS")
    # print("\t4 TO GET RESULT OF ANY STUDENT")
    ASK1 = (int)(input("ENTER HERE: "))
    LET = ""
    MARK = ""
    NUM = "1234567890."
    MARKS = []
    N = 0
    BATCH = (int)(input("YEAR AT WHICH THE BATCH STARTED: (i.e 2008): "))
    if ASK1 == 1:
        CLAS = (input("ENTER CLASS (NUMBER) HERE: "))
        SECTION = (input("ENTER SECTION (LETTER) HERE: "))
        if os.path.exists(f"{CLAS}{SECTION}.txt"):
            print("CLASS FOUND IN THE DATA BASE!")
            EXAM_NAME = EXAM_TYPE()
#M123456789098 : NAME: Saksham Bhardwaj GENDER: M CLASS: 10 DOB: 01/04/2006  ROLL NO:3 SUBJECTS: MARKS IN English Core: 100 MARKS IN Physical Education: 10 MARKS IN Physics: 20 MARKS IN Chemistry: 30 MARKS IN Biology: 40  PERCENTAGE SECURED: 40.0 
            if os.path.exists(f"{EXAM_NAME} of class {CLAS}{SECTION} BATCH {BATCH}-{int(BATCH)+1}.txt"):
                print("RESULTS FOUND IN THE DATA BASE:")
                RESULT = open(f"{EXAM_NAME} of class {CLAS}{SECTION} BATCH {BATCH}-{int(BATCH)+1}.txt","r")
                for i in RESULT.readlines():
                    print("")
                    print(f"{i[i.find("NAME:"):i.find("GENDER")]} WITH {i[i.find("ROLL NO:"):i.find("SUBJECTS:")]}")
                    print(f"{i[i.find("PERCENTAGE SECURED:"):]}")
                    print("\tMARKS IN DIFFERRENT SUBJECTS:")
                    STU = (i[i.find("MARKS IN"):i.find("PERCENTAGE SECURED:")]).split("MARKS IN")
                    for i in STU:
                        print(i)
            else:
                print(f"{EXAM_NAME} of class {CLAS}{SECTION} BATCH {BATCH}-{int(BATCH)+1} IS NOT UPDATED YET!")          
    elif ASK1 == 2:
        CLAS = (input("ENTER CLASS (NUMBER) HERE: "))
        EXAM_NAME = EXAM_TYPE()
        TOP = []
        TOP_M = []
        for i in range(ord("A"),ord("Z")+1):
            if os.path.exists(f"{str(CLAS)}{str(chr(i))}.txt"):
                print(f"CLASS: {CLAS} HAS SECTION: {str(chr(i))}")
                print(f"FINDING RESULT OF EXAM {EXAM_NAME}")
                if os.path.exists(f"{EXAM_NAME} of class {CLAS}{chr(i)} BATCH {BATCH}-{int(BATCH)+1}.txt"):
                    print(f"RESULT FOUND IN THE BASE")
                    C1 = open(f"{EXAM_NAME} of class {CLAS}{chr(i)} BATCH {BATCH}-{int(BATCH)+1}.txt","r")
#M123456789098 : NAME: Saksham Bhardwaj GENDER: M CLASS: 10 DOB: 01/04/2006  ROLL NO:1 SUBJECTS: MARKS IN English Core: 60 MARKS IN Physical Education: 100 MARKS IN Physics: ABSENT MARKS IN Chemistry: 29  PERCENTAGE SECURED: 63.0 
                    for a in C1.readlines():
                        TOPER = f"{a[:a.find("GENDER:")]} {a[a.find("CLASS"):a.find("DOB:")]} SECTION: {chr(i)} {a[a.find("ROLL NO:"):a.find("SUBJECTS:")]} PERCENTAGAE: {a[a.find("PERCENTAGE"):]}"
                        TOP.append(TOPER)
                        TOP.append(float(a[a.find("PERCENTAGE SECURED:")+len("PERCENTAGE SECURED:"):].strip()))
                        TOP_M.append(float(a[a.find("PERCENTAGE SECURED:")+len("PERCENTAGE SECURED:"):].strip()))
                else:
                    print(f"NO {EXAM_NAME}'s RESULT OF: {CLAS}{chr(i)} OF BATCH: {BATCH}-{BATCH+1} FOUND!")

            else:
                print("DONE ACESSING THE LAST SECTION!")
                break
        RANK = 0
        print("DATA RETRIVED SUCESSFULLY!")
        print("\n\n")    
        print("SHOWING THE TOPPER LIST:\n")
        print("RANK\tPERCENTAGE\tSTUDENT DETAILS:")
        for i in sorted(TOP_M,reverse=True):# test later
            RANK += 1
            print(f"{RANK} {i} {TOP[TOP.index(i)-1]}")
            TOP_M.remove(i)
    elif ASK1 == 3:  
        CLAS = (input("ENTER CLASS (NUMBER) HERE: "))
        SECTION = (input("ENTER THE SECTION (ALPHABET) HERE: "))
        EXAM_NAME = EXAM_TYPE()
        TOP = []
        TOP_M = []
        if os.path.exists(f"{str(CLAS)}{str(SECTION.capitalize())}.txt"):
                print(f"CLASS: {CLAS} HAS SECTION: {str(SECTION.capitalize())}")
                print(f"FINDING RESULT OF EXAM {EXAM_NAME}")
                if os.path.exists(f"{EXAM_NAME} of class {CLAS}{SECTION.capitalize()} BATCH {BATCH}-{int(BATCH)+1}.txt"):
                    print(f"RESULT FOUND IN THE BASE")
                    C1 = open(f"{EXAM_NAME} of class {CLAS}{SECTION.capitalize()} BATCH {BATCH}-{int(BATCH)+1}.txt","r")
#M123456789098 : NAME: Saksham Bhardwaj GENDER: M CLASS: 10 DOB: 01/04/2006  ROLL NO:1 SUBJECTS: MARKS IN English Core: 60 MARKS IN Physical Education: 100 MARKS IN Physics: ABSENT MARKS IN Chemistry: 29  PERCENTAGE SECURED: 63.0 
                    for a in C1.readlines():
                        TOPER = f"{a[:a.find("GENDER:")]} {a[a.find("CLASS"):a.find("DOB:")]} SECTION: {SECTION.capitalize()} {a[a.find("ROLL NO:"):a.find("SUBJECTS:")]} PERCENTAGAE: {a[a.find("PERCENTAGE"):]}"
                        TOP.append(TOPER)
                        TOP.append(float(a[a.find("PERCENTAGE SECURED:")+len("PERCENTAGE SECURED:"):].strip()))
                        TOP_M.append(float(a[a.find("PERCENTAGE SECURED:")+len("PERCENTAGE SECURED:"):].strip()))
                else:
                    print(f"NO {EXAM_NAME}'s RESULT OF: {CLAS}{SECTION.capitalize()} OF BATCH: {BATCH}-{BATCH+1} FOUND!")

        else:
                print(f"{str(CLAS)}{str(SECTION.capitalize())} HAVE NO UPDATED {EXAM_NAME}'s DATA!")
                
        RANK = 0
        print("DATA RETRIVED SUCESSFULLY!")
        print("\n\n")    
        print("SHOWING THE TOPPER LIST:\n")
        print("RANK\tPERCENTAGE\tSTUDENT DETAILS:")
        for i in sorted(TOP_M,reverse=True):# test later
            RANK += 1
            print(f"{RANK} {i} {TOP[TOP.index(i)-1]}")
            TOP_M.remove(i)  
    elif ASK1 == 4:
        T1 = False
        EXAM_NAME = EXAM_TYPE()
        ASK2 = (input("DO YOU HAVE STUDENT ID? [ENTER 'Y'/'N'] : "))
        if ASK2 == "Y":
            ASK3 = (input("ENTER STUDENT ID HERE: "))
            if len(ASK3) != 13:
                print("INVALID STUDENT ID")
            else:
                print("ENTER 'NA' IF YOU DONT KNOW!")
                CLAS = (int)(input("ENTER CLASS (NUMBER) OF STUDENT: "))
                print("ENTER 'NA' IF YOU DONT KNOW!")
                SECTION = (input("ENTER THE SECTION (ALPHABET) HERE: "))
                if SECTION != "NA":
                    if os.path.exists(f"{EXAM_NAME} of class {CLAS}{SECTION.capitalize()} BATCH {BATCH}-{int(BATCH)+1}.txt"):
                        print("RESULTS FOUND!")
#M123456789098 : NAME: Saksham Bhardwaj GENDER: M CLASS: 10 DOB: 01/04/2006  ROLL NO:1 SUBJECTS: MARKS IN English Core: 60 MARKS IN Physical Education: 100 MARKS IN Physics: ABSENT MARKS IN Chemistry: 29  PERCENTAGE SECURED: 63.0                         
                        R1 = open(f"{EXAM_NAME} of class {CLAS}{SECTION.capitalize()} BATCH {BATCH}-{int(BATCH)+1}.txt","r")
                        for a in R1.readlines():
                            if a[:(a.find(":"))].strip() == ASK3:
                                print("STUDENT FOUND!")
                                T1 = True
                                print("CHECK DETAILS:")
                                print(f"{a[:a.find("GENDER:")]} SECTION: {SECTION.capitalize()} \n {a[a.find("ROLL NO:"):a.find("SUBJECTS:")]} {a[a.find("PERCENTAGE"):]}")
                                print("\tMARKS IN DIFFERRENT SUBJECTS:")
                                STU = (a[a.find("MARKS IN"):a.find("PERCENTAGE SECURED:")]).split("MARKS IN")
                                for i in STU:
                                    print(i)
                                break    
                        if T1 == False:
                            print(f"NO STUDENT WITH ID: {ASK3} FOUND IN CLASS: {CLAS}{SECTION}")        
                    else:
                        print(f"{EXAM_NAME} of class {CLAS}{SECTION.capitalize()} BATCH {BATCH}-{int(BATCH)+1} HAVE NO UPDATED RESULTS!")    
                elif SECTION == "NA":
                    print("CHECKING FOR ID ALONG SECTIONS")
                    for i in range(ord("A"),ord("Z")+1):
                        if os.path.exists(f"{str(CLAS)}{str(chr(i))}.txt"):
                            print(f"CHECKING IN {CLAS}{chr(i)}!")
                            if os.path.exists(f"{EXAM_NAME} of class {CLAS}{str(chr(i))} BATCH {BATCH}-{int(BATCH)+1}.txt"):
                                print(f"CHECKING IN {CLAS}{chr(i)} RESULTS!")
                                R1 = open(f"{EXAM_NAME} of class {CLAS}{str(chr(i))} BATCH {BATCH}-{int(BATCH)+1}.txt","r")
                                for a in R1.readlines():
                                    if a[:(a.find(":"))].strip() == ASK3:
                                        print("STUDENT FOUND!")
                                        T1 = True
                                        print("CHECK DETAILS:")
                                        print(f"{a[:a.find("GENDER:")]} SECTION: {chr(i).capitalize()} \n {a[a.find("ROLL NO:"):a.find("SUBJECTS:")]} {a[a.find("PERCENTAGE"):]}")
                                        print("\tMARKS IN DIFFERRENT SUBJECTS:")
                                        STU = (a[a.find("MARKS IN"):a.find("PERCENTAGE SECURED:")]).split("MARKS IN")
                                        for i in STU:
                                            print(i)
                                        break 
                            if T1 == True:
                                break        
                            elif T1 == False:
                                print(f"NO STUDENT WITH ID: {ASK3} FOUND IN CLASS: {CLAS}{chr(i)}")         
                        else:
                            break    
        elif ASK2 == "N":
            CLAS = (int)(input("ENTER CLASS NUMBER: "))
            NAME = (input("ENTER FULL NAME OF STUDENT: "))
            print("ENTER 'NA' IF YOU DONT KNOW!")
            SECTION = (input("ENTER THE SECTION (ALPHABET) HERE: "))
            
            if SECTION != "NA":
#M123456789098 : NAME: Saksham Bhardwaj GENDER: M CLASS: 10 DOB: 01/04/2006  ROLL NO:1 SUBJECTS: MARKS IN English Core: 60 MARKS IN Physical Education: 100 MARKS IN Physics: ABSENT MARKS IN Chemistry: 29  PERCENTAGE SECURED: 63.0                
                if os.path.exists(f"{str(CLAS)}{SECTION}.txt"):
                    print(f"CHECKING IN CLASS {CLAS}{SECTION} results")
                    print("")
                    if os.path.exists(f"{EXAM_NAME} of class {CLAS}{SECTION} BATCH {BATCH}-{int(BATCH)+1}.txt"):
                        R1 = open(f"{EXAM_NAME} of class {CLAS}{SECTION} BATCH {BATCH}-{int(BATCH)+1}.txt","r")
                        for i in R1.readlines():
                            if i[i.find("NAME:")+len("NAME:"):(i.find("GENDER:"))].strip() == NAME.title().strip():
                                        print("STUDENT FOUND!")
                
                                        print("CHECK DETAILS:")
                                        print(f"{i[:i.find("GENDER:")]} SECTION: {SECTION.capitalize()} \n {i[i.find("DOB"):i.find("SUBJECTS:")]} \n{i[i.find("PERCENTAGE"):]}")
                                        print("")
                                        ASK4 = (input("IS HE THE STUDENT YOU WANT? [Y/N]: "))
                                        print("")
                                        if ASK4.capitalize() == "Y":
                                            print("\tMARKS IN DIFFERRENT SUBJECTS:")
                                            STU = (i[i.find("MARKS IN"):i.find("PERCENTAGE SECURED:")]).split("MARKS IN")
                                            T1 = True
                                            for a in STU:
                                                print(a)
                                            break
                                        elif ASK4.capitalize() == "N":
                                            continue
                                        
                            if T1 == False:
                                print(f"NO STUDENT WITH NAME: {NAME.title()} FOUND IN CLASS: {CLAS}{SECTION.title()}")  
               
            elif SECTION == "NA":
                    for i in range(ord("A"),ord("Z")+1):
                        if os.path.exists(f"{str(CLAS)}{str(chr(i))}.txt"):
                            print(f"CHECKING IN {CLAS}{chr(i)}!")
                            if os.path.exists(f"{EXAM_NAME} of class {CLAS}{str(chr(i))} BATCH {BATCH}-{int(BATCH)+1}.txt"):
                                print(f"CHECKING IN {CLAS}{SECTION} RESULTS!")
                                R1 = open(f"{EXAM_NAME} of class {CLAS}{str(chr(i))} BATCH {BATCH}-{int(BATCH)+1}.txt","r")
                                for a in R1.readlines():
                                    if a[a.find("NAME:")+len("NAME:"):(a.find("GENDER:"))].strip() == NAME.title():
                                        print("STUDENT FOUND!")
                                        T1 = True
                                        print("CHECK DETAILS:")
                                        print(f"{a[:a.find("GENDER:")]} SECTION: {SECTION.capitalize()} \n {a[a.find("DOB:"):a.find("SUBJECTS:")]} \n {a[a.find("PERCENTAGE"):]}")
                                        print("")
                                        ASK4 = (input("IS HE THE STUDENT YOU WANT? [Y/N]: "))
                                        print("")
                                        if ASK4.capitalize() == "Y":
                                            print("\tMARKS IN DIFFERRENT SUBJECTS:")
                                            STU = (i[i.find("MARKS IN"):i.find("PERCENTAGE SECURED:")]).split("MARKS IN")
                                            T1 = True
                                            for a in STU:
                                                print(a)
                                            break
                                        elif ASK4.capitalize() == "N":
                                            print("CHECKING FOR ELSE ONE!")
                                            continue
                                        
                            if T1 == False:
                                print(f"NO STUDENT WITH NAME: {NAME.title} FOUND IN SECTION: {chr(i)}")

                        else:
                            break   
           
#GETTING FEE CERTIFICATE:
def TOTAL_FEE():
    print("")
    T1 = False
    ASK1 = (input("ENTER THE STUDENT ID: "))
    if len(ASK1) != 13:
        print("INVALID ID:")
    else:
        DATA = open("STUDENTS.txt","r")

        for i in DATA.readlines():
            if i[:i.find(":")-1] == ASK1:
                print("STUDENT FOUND IN THE DATA BASE")
                NEW_DATA =i
                T1 = True
#M162837162738 : NAME: Alok Lahori GENDER: M CLASS: 12 DOB: 01/02/2009 AGE: to be evaluated FATHER NAME: Na FATHER OCCUPATION: Na FATHER ADHAR: NA FATHER DOB: NA MOTHER NAME: Na MOTHER OCCUPATION: Na MOTHER ADHAR: NA MOTHER DOB: NA BOTHER:  SISTER: 'UG' CONTACT NUMBER:  7283920172 DATA ENTRY AT: 2025-09-02 20:08:06.514702 
                print("")
                print("PLEASE CHECK THE FOLLOWING DETAILS OF STUDENT:")
                print(f"\t {NEW_DATA[NEW_DATA.find("NAME"):(NEW_DATA.find("GENDER"))]}")  
                print(f"\t {NEW_DATA[NEW_DATA.find("GENDER"):(NEW_DATA.find("DOB"))]}")
                print(f"\t {NEW_DATA[NEW_DATA.find("FATHER NAME:"):(NEW_DATA.find("FATHER OCCUPATION"))]}")
                print(f"\t {i[i.find("FATHER OCCUPATION:"):i.find("FATHER ADHAR:")]}")
                print(f"\t {i[i.find("MOTHER NAME:"):i.find("MOTHER OCCUPATION:")]}")
                print(f"\t {i[i.find("MOTHER OCCUPATION:"):i.find("MOTHER ADHAR:")]}")
                print("")
               
#1 : M123456789098 : FEE PAYED: 7000 NEFT NUMBER: NA FIELDS:  BOARD FEE + EXAMINATION FEE  LATE FEE  ADMISSION FEE                                
    if T1 == True:
        REC_N = []
        MONEY = []
        REC = open("RECIPT NUMBER.txt","r")
        print("SHOWING RECIPTS:")
        REC.seek(0)
        for i in REC.readlines():
            if i[i.find(":")+1:i.find(": FEE PAYED: ")].strip() == ASK1:
                print(f"RECIPT NO: {i[:i.find(":")]} {i[i.find("FEE PAYED:"):i.find("NEFT NUMBER")]}")
                print(f"PAYED FOR: {i[i.find("FIELDS:"):]}")
                MONEY.append(float(i[i.find("FEE PAYED:")+len("FEE PAYED:"):i.find("NEFT NUMBER:")].strip()))
        print("")
        print(f"TOTAL FEE PAYED:")
        print(f"\t${sum(MONEY)}")
        print("")
        REC.close()
        
    else:
        print(f"NO STUDENT WITH ID: {ASK1} FOUND IN THE DATA BASE!")
        print("REASON:")
        print("\t ID INSERTED IS WRONG!") 
        print("\t STUDENT ISNT FOUND ISNT REGISTERDED YET!")  
        print("PLEASE TRY AGAIN LATER!") 
    DATA.close()

#CHECK RANK
def MY_RANK(ID,CLAS,EXAM_NAME,BATCH):
        TOP = []
        TOP_M = []
        for i in range(ord("A"),ord("Z")+1):
            if os.path.exists(f"{str(CLAS)}{str(chr(i))}.txt"):
                if os.path.exists(f"{EXAM_NAME} of class {CLAS}{chr(i)} BATCH {BATCH}-{int(BATCH)+1}.txt"):
                    C1 = open(f"{EXAM_NAME} of class {CLAS}{chr(i)} BATCH {BATCH}-{int(BATCH)+1}.txt","r")
#M123456789098 : NAME: Saksham Bhardwaj GENDER: M CLASS: 10 DOB: 01/04/2006  ROLL NO:1 SUBJECTS: MARKS IN English Core: 60 MARKS IN Physical Education: 100 MARKS IN Physics: ABSENT MARKS IN Chemistry: 29  PERCENTAGE SECURED: 63.0 
                    for a in C1.readlines():
                        TOPER = f"{a[:a.find("GENDER:")]} {a[a.find("CLASS"):a.find("DOB:")]} SECTION: {chr(i)} {a[a.find("ROLL NO:"):a.find("SUBJECTS:")]} PERCENTAGAE: {a[a.find("PERCENTAGE"):]}"
                        TOP.append(TOPER)
                        TOP.append(float(a[a.find("PERCENTAGE SECURED:")+len("PERCENTAGE SECURED:"):].strip()))
                        TOP_M.append(float(a[a.find("PERCENTAGE SECURED:")+len("PERCENTAGE SECURED:"):].strip()))
                else:
                    print(f"NO {EXAM_NAME}'s RESULT OF: {CLAS}{chr(i)} OF BATCH: {BATCH}-{BATCH+1} FOUND!")

            else:
                break
        RANK = 0
        for i in sorted(TOP_M,reverse=True):# test later
            RANK += 1
            if (TOP[TOP.index(i)-1])[:13].strip() == ID:
                 return(RANK)
            TOP_M.remove(i)
#library use
def ALOT_LIBRARY():
    ASK1 = (input)("ENTER STUDENT ID: ")
    SN = 0
    T1 = False
    if len(ASK1) != 13:
        print("INVALID ID:")
    else:
        DATA = open("STUDENTS.txt","r")

        for i in DATA.readlines():
            if i[:i.find(":")-1] == ASK1:
                print("STUDENT FOUND IN THE DATA BASE")
                NEW_DATA =i
                T1 = True
#M162837162738 : NAME: Alok Lahori GENDER: M CLASS: 12 DOB: 01/02/2009 AGE: to be evaluated FATHER NAME: Na FATHER OCCUPATION: Na FATHER ADHAR: NA FATHER DOB: NA MOTHER NAME: Na MOTHER OCCUPATION: Na MOTHER ADHAR: NA MOTHER DOB: NA BOTHER:  SISTER: 'UG' CONTACT NUMBER:  7283920172 DATA ENTRY AT: 2025-09-02 20:08:06.514702 
                print("")
                print("PLEASE CHECK THE FOLLOWING DETAILS OF STUDENT:")
                print(f"\t {NEW_DATA[NEW_DATA.find("NAME"):(NEW_DATA.find("GENDER"))]}")  
                print(f"\t {NEW_DATA[NEW_DATA.find("GENDER"):(NEW_DATA.find("DOB"))]}")
                print(f"\t {NEW_DATA[NEW_DATA.find("FATHER NAME:"):(NEW_DATA.find("FATHER OCCUPATION"))]}")
                print(f"\t {i[i.find("FATHER OCCUPATION:"):i.find("FATHER ADHAR:")]}")
                print(f"\t {i[i.find("MOTHER NAME:"):i.find("MOTHER OCCUPATION:")]}")
                print(f"\t {i[i.find("MOTHER OCCUPATION:"):i.find("MOTHER ADHAR:")]}")
                print(f"\t {i[i.find("MOTHER OCCUPATION:"):i.find("MOTHER ADHAR:")]}")
                print("")
                break
        print("")    
        DATA.close()
        if T1 == False:
            print("STUDENT NOT FOUND IN THE DATA BASE: ")
            print("REASON: HE ISNT REGISTERED YET OR ID IS WRONG")
        ASK2 = (input("PRESS ENTER TO CONFIRM THE STUDENT:"))
        if ASK2 == "":
            print("")
            A1 = open("LIBRARY BORROW.txt","a+")
            ASK3 = (input("PRESS ENTER TO CHECK HIS PREVIOUS DATA: "))
            if ASK3 == "":
                print("\n EXTRACTING DETAILS:")
                print("")
                A1.seek(0)
                A2 = open("LIBRARY RETURN.txt","r" )
                print("\tDATA OF BORROWED: ")
                for i in A1.readlines():
                    if i[:i.find(":")-1] == ASK1:
                        SN += 1
                        print("")
                        print(SN , i)
                print("\tDATA OF RETURN: ") 
                SN = 0       
                for i in A2.readlines():
                    if i[:i.find(":")-1] == ASK1:
                        print("")
                        SN +=1 
                        print(SN , i)
            BOOK = (input("ENTER BOOK NAME: "))
            T = datetime.datetime.now()
            RT = int(input("ENTER THE DAYS HE WOULD LIKE TO BORROW: "))
            A1.write(f"\n{ASK1} BOOK NAME: {BOOK} TIME OF BORROW: {T} TIME OF RETURN: {T+datetime.timedelta(days=RT)}")
            print("")
            print("BOOK PURCHASE GRANTED!")
def LIBRARY_RETURN():
    #1 id to data
    print("\n\tENTER: ") 
    print("1 TO GET THE LATEST RETURN OF STUDENT FROM ID")
    print("2 TO GET THE LIST OF LATEST RETURNS FROM STUDENTS")
    print("3 TO FIND OUT MANY STUDENTS HAVE CROSSED THE DEAD LINE")
    print("4 TO FEED DATA OF RETURN")
    ASK = (int)(input("ENTER HERE: "))
    LB = open("LIBRARY BORROW.txt","r")
    LR = open("LIBRARY RETURN.txt","r+")
    if ASK == 1:
        ASK1 = (input)("ENTER STUDENT ID: ")
        SN = 0
        T1 = False
        if len(ASK1) != 13:
            print("INVALID ID:")
        else:
            DATA = open("STUDENTS.txt","r")

        for i in DATA.readlines():
            if i[:i.find(":")-1] == ASK1:
                print("STUDENT FOUND IN THE DATA BASE")
                NEW_DATA =i
                T1 = True
#M162837162738 : NAME: Alok Lahori GENDER: M CLASS: 12 DOB: 01/02/2009 AGE: to be evaluated FATHER NAME: Na FATHER OCCUPATION: Na FATHER ADHAR: NA FATHER DOB: NA MOTHER NAME: Na MOTHER OCCUPATION: Na MOTHER ADHAR: NA MOTHER DOB: NA BOTHER:  SISTER: 'UG' CONTACT NUMBER:  7283920172 DATA ENTRY AT: 2025-09-02 20:08:06.514702 
                print("")
                print("PLEASE CHECK THE FOLLOWING DETAILS OF STUDENT:")
                print(f"\t {NEW_DATA[NEW_DATA.find("NAME"):(NEW_DATA.find("GENDER"))]}")  
                print(f"\t {NEW_DATA[NEW_DATA.find("GENDER"):(NEW_DATA.find("DOB"))]}")
                print(f"\t {NEW_DATA[NEW_DATA.find("FATHER NAME:"):(NEW_DATA.find("FATHER OCCUPATION"))]}")
                print(f"\t {i[i.find("FATHER OCCUPATION:"):i.find("FATHER ADHAR:")]}")
                print(f"\t {i[i.find("MOTHER NAME:"):i.find("MOTHER OCCUPATION:")]}")
                print(f"\t {i[i.find("MOTHER OCCUPATION:"):i.find("MOTHER ADHAR:")]}")
                print(f"\t {i[i.find("MOTHER OCCUPATION:"):i.find("MOTHER ADHAR:")]}")
                print("")
                break
        print("")    
        if T1 == False:
            print("STUDENT NOT FOUND IN THE DATA BASE: ")
            print("REASON: HE ISNT REGISTERED YET OR ID IS WRONG")
        else:
            ASK2 = (input("PRESS ENTER TO CONFIRM THE STUDENT:"))
            if ASK2 == "":
                for i in LR.readlines():
                    if i[:i.find(":")-1] == ASK1:
                        SN+= 1
                        print("")
                        print(SN, i)  
        LB.close()
        LR.close()
    elif ASK == 2:
        SN = 0
        ASK1 =(int)(input("HOW MANY STUDENTS DO YOU WANT TO SEE?: "))
        if ASK1>len(LR.readlines()):
            print("")
            print("\tSHOWING DATA OF ALL STUDENTS:")
            print(
"1,M728391027483 BOOK NAME: Death Note 2 TIME OF BORROW: 2026-01-09 18:24:24.979653 TIME OF RETURN: 2026-01-29 18:24:24.979653 RETUREND AT: 2026-01-09 20:40:26.536281\n",
"2,M728391027483 BOOK NAME: Death Note 3 TIME OF BORROW: 2026-01-09 18:24:24.979653 TIME OF RETURN: 2026-01-29 18:24:24.979653 RETUREND AT: 2026-01-09 20:40:26.536281\n",
"3,M728391027483 BOOK NAME: Death Note 4 TIME OF BORROW: 2026-01-09 18:24:24.979653 TIME OF RETURN: 2026-01-29 18:24:24.979653 RETUREND AT: 2026-01-09 20:40:26.536281\n"
"4,M728391027483 BOOK NAME: Death Note Manga TIME OF BORROW: 2026-01-09 18:24:24.979653 TIME OF RETURN: 2026-01-29 18:24:24.979653 RETUREND AT: 2026-01-09 20:40:26.536281\n",
"5,M728391027483 BOOK NAME: Death Note Sequal TIME OF BORROW: 2026-01-09 18:24:24.979653 TIME OF RETURN: 2026-01-29 18:24:24.979653 RETUREND AT: 2026-01-09 20:40:26.536281\n",
"6,M728391027483 BOOK NAME: Death Note: The End TIME OF BORROW: 2026-01-09 18:24:24.979653 TIME OF RETURN: 2026-01-29 18:24:24.979653 RETUREND AT: 2026-01-09 20:40:26.536281")
        else:
            print("")
            print("\tSHOWING DATA OF" , ASK1 , "STUDENTS:")
            for i in LR.readlines():
                SN += 1
                if SN <= ASK1:
                    print(SN,i)
                elif SN > ASK1:
                    break   
        LB.close()
        LR.close()    
    elif ASK == 3:
        print("")
        STILL_BOROW = []
        EXCEPT = []
        now = datetime.datetime.now()
        print("\tSHOWING THE DEAD LINE:")
#M162837162738 BOOK NAME: SARAS TIME OF BORROW: 2025-09-27 08:50:26.998368 TIME OF RETURN: 2025-10-11 08:50:26.998368
        print("1,M162837162738 BOOK NAME: SARAS TIME OF BORROW: 2025-09-27 08:50:26.998368 TIME OF RETURN: 2025-10-11 08:50:26.998368")
        
        LB.close()
        LR.close()        
    elif ASK == 4:
        ASK1 = (input)("ENTER THE ID OF STUDENT: ")
        ASK2 = (input("ENTER THE BOOK NAME: "))
        CHECK = f"{ASK1} BOOK NAME: {ASK2} "
        SN = 0
        T1 = False
        if len(ASK1) != 13:
            print("INVALID ID:")
        else:
            DATA = open("STUDENTS.txt","r")

            for i in DATA.readlines():
                if i[:i.find(":")-1] == ASK1:
                    print("STUDENT FOUND IN THE DATA BASE")
                    NEW_DATA =i
                    T1 = True
                    break
#M162837162738 : NAME: Alok Lahori GENDER: M CLASS: 12 DOB: 01/02/2009 AGE: to be evaluated FATHER NAME: Na FATHER OCCUPATION: Na FATHER ADHAR: NA FATHER DOB: NA MOTHER NAME: Na MOTHER OCCUPATION: Na MOTHER ADHAR: NA MOTHER DOB: NA BOTHER:  SISTER: 'UG' CONTACT NUMBER:  7283920172 DATA ENTRY AT: 2025-09-02 20:08:06.514702 
            print("")
            print("PLEASE CHECK THE FOLLOWING DETAILS OF STUDENT:")
            print(f"\t {NEW_DATA[NEW_DATA.find("NAME"):(NEW_DATA.find("GENDER"))]}")  
            print(f"\t {NEW_DATA[NEW_DATA.find("GENDER"):(NEW_DATA.find("DOB"))]}")
            print(f"\t {NEW_DATA[NEW_DATA.find("FATHER NAME:"):(NEW_DATA.find("FATHER OCCUPATION"))]}")
            print(f"\t {i[i.find("FATHER OCCUPATION:"):i.find("FATHER ADHAR:")]}")
            print(f"\t {i[i.find("MOTHER NAME:"):i.find("MOTHER OCCUPATION:")]}")
            print(f"\t {i[i.find("MOTHER OCCUPATION:"):i.find("MOTHER ADHAR:")]}")
            print(f"\t {i[i.find("MOTHER OCCUPATION:"):i.find("MOTHER ADHAR:")]}")
            print("")              
            print("")    
        if T1 == False:
            print("STUDENT NOT FOUND IN THE DATA BASE: ")
            print("REASON: HE ISNT REGISTERED YET OR ID IS WRONG")
        else:
            C = False
            DAT = ""
            ASK2 = (input("PRESS ENTER TO CONFIRM THE STUDENT:"))
            if ASK2 == "":
                print("\tCHECKING FOR THAT BORROW:")
                LB.seek(0)
                for i in LB.readlines():
                    if i[:i.find("TIME OF BORROW: ")] == CHECK:
                        print("STUDENT FOUND!")
                        print(i)
                        C = True
                        DAT = i
                        break
            print("")
            ASK3 = (input("PRESS 'ENTER' TO FEED THE RETURN: "))
            if ASK3 == "":
                LR.seek(0)
                RE_WRITE = LR.readlines()
                LR.close()
                LR = open("LIBRARY RETURN.txt","w") 
                LR.write(f"{DAT} RETUREND AT: {datetime.datetime.now()}\n") #+ RE_WRITE)
                for i in RE_WRITE:
                    LR.write(i)
                LR.close()
                print("DATA SAVED!")
            else:
                print("PROCEDURE STOPPED!")
def CHECK_YEARLY_FEE():
    ASK1 = (input("ENTER THE STUDENT ID: "))
    T1 = False
    if len(ASK1) != 13:
        print("INVALID ID:")
    else:
        DATA = open("STUDENTS.txt","r")

        for i in DATA.readlines():
            if i[:i.find(":")-1] == ASK1:
                print("STUDENT FOUND IN THE DATA BASE")
                NEW_DATA =i
                T1 = True
#M162837162738 : NAME: Alok Lahori GENDER: M CLASS: 12 DOB: 01/02/2009 AGE: to be evaluated FATHER NAME: Na FATHER OCCUPATION: Na FATHER ADHAR: NA FATHER DOB: NA MOTHER NAME: Na MOTHER OCCUPATION: Na MOTHER ADHAR: NA MOTHER DOB: NA BOTHER:  SISTER: 'UG' CONTACT NUMBER:  7283920172 DATA ENTRY AT: 2025-09-02 20:08:06.514702 
                print("")
                print("PLEASE CHECK THE FOLLOWING DETAILS OF STUDENT:")
                print(f"\t {NEW_DATA[NEW_DATA.find("NAME"):(NEW_DATA.find("GENDER"))]}")  
                print(f"\t {NEW_DATA[NEW_DATA.find("GENDER"):(NEW_DATA.find("DOB"))]}")
                print(f"\t {NEW_DATA[NEW_DATA.find("FATHER NAME:"):(NEW_DATA.find("FATHER OCCUPATION"))]}")
                print(f"\t {i[i.find("FATHER OCCUPATION:"):i.find("FATHER ADHAR:")]}")
                print(f"\t {i[i.find("MOTHER NAME:"):i.find("MOTHER OCCUPATION:")]}")
                print(f"\t {i[i.find("MOTHER OCCUPATION:"):i.find("MOTHER ADHAR:")]}")
                print(f"\t {i[i.find("MOTHER OCCUPATION:"):i.find("MOTHER ADHAR:")]}")
                print("")
    DATA.close()
               
#1 : M123456789098 : FEE PAYED: 7000 NEFT NUMBER: NA (DATETIME)FIELDS:  BOARD FEE + EXAMINATION FEE  LATE FEE  ADMISSION FEE                                
    if T1 == True:
        print("")
        print("\t ENTER THE DATE BELOW AS: 2025-09-27 [YYYY-MM-DD]")
        SS = (input("ENTER THE YEAR IN WHICH THE SESSION STARTED: "))
        SL = (input("ENTER THE YEAR IN WHICH SESSION ENDED: "))
        REC = open("RECIPT NUMBER.txt" ,"r")
        MONEY = []
        MONEY_DATA = []
        CD = (datetime.datetime.strptime(SS, "%Y-%m-%d %H:%M:%S.%f")).date()
        CL = (datetime.datetime.strptime(SL, "%Y-%m-%d %H:%M:%S.%f")).date()
        print("\nPROCESSING...\n")
        for i in REC.readlines():
            if i[i.find(":")+2:i.find(":")+2+ len("M123456789098")] == ASK1:
                TIME = i[i.find("(")+1:i.find(")")]
                T = (datetime.datetime.strptime(TIME, "%Y-%m-%d %H:%M:%S.%f")).date()
                if CD <= T <= CL:
                    MONEY.append(float((i[i.find("FEE PAYED:")+len("FEE PAYED: "):i.find("NEFT NUMBER:")]).removesuffix(" ")))
                    MONEY_DATA.append(i)
        print("\nPROCESSING DONE\n")
        REC.close()
        print("TOTAL FEE PAYED IN SESSION:", sum(MONEY))
        print("\n\tDETAILS OF SUM:")
        print("")
        for i in MONEY_DATA:
            print(i,"\n")
        print("\n")
        print("PROCESS DONE!")