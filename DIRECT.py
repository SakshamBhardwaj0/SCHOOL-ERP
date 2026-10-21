from SYSTEM import *
print("")
print("THIS IS THE DIRECT , YOU CAN USE ALL LISTED FEATURES DIRECTLY:")
print("")
print("ENTER '1' FOR ADMMISSION")
print("ENTER '2' FOR ALOTTING CLASS TO A STUDENT")
print("ENTER '3' FOR STORING FEE INFO")
print("ENTER '4' FOR CREATING RESULT")
print("ENTER '5' FOR FINDING RESULT")
print("ENTER '6' FOR CALCULATING TOTAL FEE")
print("ENTER '7' FOR ALOTTING LIBRARY BOOK")
print("ENTER '8' FOR RETURURNING LIBRARY BOOK AND MORE")
print("ENTER '9' FOR CHECKING THE YEARLY FEE")
print("")
ASK = (int)(input("ENTER HERE: "))
if ASK == 1:
    ADMISSION()
elif ASK == 2:
    ALOT_CLASS()
elif ASK == 3:
    FEE_PROCEDURE()
elif ASK == 4:
    RESULT_CREATE()
elif ASK == 5:
    FIND_RESULT()
elif ASK == 6:
    TOTAL_FEE()
elif ASK == 7:
    ALOT_LIBRARY()
elif ASK == 8:
    LIBRARY_RETURN()
elif ASK == 9:
    CHECK_YEARLY_FEE()
elif ASK == 10:
    ASK2 = (input("ENTER STUDENT ID: "))
    ASK3 = (int)(input("ENTER EXAM NAME: "))
    ASK4 = (int)(input("IN WHICH YEAR THE BATCH WAS STARTED: "))
    print("\nPROCEEDING RANK...\n")
    print(MY_RANK(ASK2,ASK3,ASK4))
