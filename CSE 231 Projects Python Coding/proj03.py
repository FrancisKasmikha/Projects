import math
# getting the math function, in order to use math.ceil
print("2019 MSU Undergraduate Tuition Calculator.")
response = "yes"
start = "go"
#I needed a way end to the loop, did that through the response command response adnd the start variable was for the tab of resident at first, but i needed it to untab after.
while response == "yes":
    if start == "go":
        res = input("\nResident (yes/no): ")
        res = res.lower()
    elif start == "no":
        res = input("Resident (yes/no): ")
        res = res.lower()
#here is where i choose if the it will create a new line or not
    while res == "yes":
        level = input("Level—freshman, sophomore, junior, senior: ")
        level = level.lower()
        while level != "freshman" and level != "sophomore" and level != "junior" and level != "senior":
            print("Invalid input. Try again.")
            levels = input("Level—freshman, sophomore, junior, senior: ")
            level = levels.lower()
    #just establishing my variables. I use a while loop. so it they choose yes. i ask for their grade level and they need to respond with the right grade level
        int_part = 0
        int_full = 0
        # i coded this project by having a mixture of variables and then changing them when i needed to. like one would be 0 when i didnt need to use it this is an example of that
        if level == "freshman" or level == "sophomore":
            College_Eng_Fresh = input("Are you admitted to the College of Engineering (yes/no): ")
            College_Eng_Fresh = College_Eng_Fresh.lower()
            part = 0
            full = 0
            undergrad = 24
            C_part = 0
            C_full = 0
            #establishing all the variables in the loop based on freshman or sophomore
            if College_Eng_Fresh == "no":
                James_madison = input("Are you in the James Madison College (yes/no): ")
                James_madison = James_madison.lower()
                if James_madison == "yes":
                    JamesDollar = float(7.50)
                elif James_madison == "no":
                    JamesDollar = 0
                four_or_fewer = 0
                six_or_more = 0
            elif College_Eng_Fresh == "yes":
                four_or_fewer = float(402)
                six_or_more = float(670)
                JamesDollar= 0
# this is where the person will get prompted if they respond yes or no to being an engineer
            if level == "freshman":
                percredit = 482
                percredits = float(percredit)
            elif level == "sophomore":
                percredit = 494
                percredits = float(percredit)
#setting the values of precredit, which is like my universal variable. which one will get used depends entirely on if there a freshman or sophomore


        elif level == "junior" or level == "senior":
# now asking if there a junior or a senior
            undergrad = 24
            six_or_more = 0
            four_or_fewer = 0
            College_of_Study= input("Enter college as business, engineering, health, sciences, or none: ")
            College_of_Study= College_of_Study.lower()
            JamesDollar = 0
#establishing some values, these terms look  very simaler to ones I had before, becuase theya re if they arent true, the values will switch over to this
            CMSE_Major = input("""Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): """)
            CMSE_Major = CMSE_Major.lower()
            if CMSE_Major == "yes":
                C_part = float(402)
                C_full = float(670)
            elif CMSE_Major == "no":
                C_part = 0
                C_full = 0
    #if they are a csme major then these vaulues will be set.
#here is where I will ask for their major an depending on those values, I will add them all up and get a value
            if College_of_Study == "business":
                part = float(113)
                full = float(226)
                percredit = float(573)
                percredits = float(573)
            elif College_of_Study == "engineering":
                part = float(402)
                full = float(670)
                percredit = 573
                percredits = float(percredit)
            elif College_of_Study == "health" or College_of_Study == "sciences":
                part = float(50)
                full = float(100)
                percredit = 555
                percredits= float(percredit)
        # if not any of these variables then it will be this, will then ask them if there in James Madison
            elif College_of_Study != "health" or College_of_Study != "sciences" or College_of_Study != "engineering" or College_of_Study != "business":
                part = float(0)
                full = float(0)
                percredit = 555
                percredits = float(percredit)
                James_madison = input("Are you in the James Madison College (yes/no): ")
                James_madison = James_madison.lower()
                if James_madison == "yes":
                    JamesDollar = float(7.50)
                elif James_madison == "no":
                    JamesDollar = float(0)
# this is where i make my formulas , 1 was for 11 credits or less. the next was  the flat rate tuition and the last one was to charge them for how over they go.
        college_credit = input("Credits: ")
        while not college_credit.isdigit() or int(college_credit) <= 0:
            print("Invalid input. Try again.")
            college_credit = input("Credits: ")
        college_credits = float(college_credit)
        if college_credits >float(0) and college_credits<= float(11):
            TotalPrice = college_credits * percredits
            if college_credits <= float(4):
                Totals = TotalPrice + JamesDollar + four_or_fewer + part + C_part+undergrad
            elif college_credits >float(4):
                Totals = TotalPrice + JamesDollar + six_or_more + full +C_full+ undergrad
                if college_credits >= float(6):
                    Totals = Totals + 5
        elif college_credits >=float(12) and college_credits<float(18):
            TotalPrice = percredits*15
            Totals = TotalPrice + JamesDollar + six_or_more + full+C_full+undergrad + 5
        elif college_credits >float(18):
            TotalPrice = ((college_credits-18) * percredits) + (percredits*15) +5
            Totals = TotalPrice + JamesDollar + six_or_more + undergrad
        #so yeah here I print my total price with all the values i have made.
        TotalAllTogother = math.ceil(Totals)
        TotalAllTogother = '${:,.2f}.'.format(TotalAllTogother)
        print("Tuition is", TotalAllTogother)
        break
    while res == "no":
        Int_Student = input("International (yes/no): ")
        Int_Student = Int_Student.lower()
        if Int_Student == "yes":
            int_part = float(375)
            int_full = float(750)
        elif Int_Student == "no":
            int_part = 0
            int_full = 0
        #ask if their an international student, if they are they will be charged some money and if they arent they wont be charged.
        level = input("Level—freshman, sophomore, junior, senior: ")
        level = level.lower()
        while level != "freshman" and level != "sophomore" and level != "junior" and level != "senior":
            print("Invalid input. Try again.")
            level = input("Level—freshman, sophomore, junior, senior: ")
            level = level.lower()
        if level == "freshman" or level == "sophomore":
            College_Eng_Fresh = input("Are you admitted to the College of Engineering (yes/no): ")
            College_Eng_Fresh = College_Eng_Fresh.lower()
            part = 0
            full = 0
            undergrad = 24
            C_part = 0
            C_full = 0
            if College_Eng_Fresh == "no":
                James_madison = input("Are you in the James Madison College (yes/no) : ")
                James_madison = James_madison.lower()
                if James_madison == "yes":
                    JamesDollar = float(7.50)
                elif James_madison == "no":
                    JamesDollar = 0
                four_or_fewer = 0
                six_or_more = 0
            elif College_Eng_Fresh == "yes":
                four_or_fewer = float(402)
                six_or_more = float(670)
                JamesDollar= 0

            if level == "freshman":
                percredit = 1325.50
                percredits = float(percredit)
            elif level == "sophomore":
                percredit = 1325.50
                percredits = float(percredit)


        elif level == "junior" or level == "senior":

            undergrad = 24
            six_or_more = 0
            four_or_fewer = 0
            College_of_Study= input("Enter college as business, engineering, health, sciences, or none: ")
            College_of_Study= College_of_Study.lower()
            JamesDollar = 0
            CMSE_Major = input("""Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): """)
            CMSE_Major = CMSE_Major.lower()
            if CMSE_Major == "yes":
                C_part = float(402)
                C_full = float(670)
            elif CMSE_Major == "no":
                C_part = 0
                C_full = 0
            if College_of_Study == "business":
                part = float(113)
                full = float(226)
                percredit = float(1385.75)
                percredits = float(1385.75)
            elif College_of_Study == "engineering":
                part = float(402)
                full = float(670)
                percredit = 1385.75
                percredits = float(percredit)
            elif College_of_Study == "health" or College_of_Study == "sciences":
                part = float(50)
                full = float(100)
                percredit = 1366.75
                percredits= float(percredit)
            elif College_of_Study != "health" or College_of_Study != "sciences" or College_of_Study != "engineering" or College_of_Study != "business":
                part = float(0)
                full = float(0)
                percredit = 1366.75
                percredits = float(percredit)
                James_madison = input("Are you in the James Madison College (yes/no) : ")
                James_madison = James_madison.lower()
                if James_madison == "yes":
                    JamesDollar = float(7.50)
                elif James_madison == "no":
                    JamesDollar = float(0)
#the rest of my values are exactly the same as before expect that the prices have changed although the equations have not.
        college_credit = input("Credits: ")
        while not college_credit.isdigit() or int(college_credit) <= 0:
            print("Invalid input. Try again.")
            college_credit = input("Credits: ")
        college_credits= float(college_credit)
        if college_credits >float(0) and college_credits<= float(11):
            TotalPrice = college_credits * percredits
            if college_credits <= float(4):
                Totals = TotalPrice + JamesDollar + four_or_fewer + part + C_part+undergrad + int_part
            elif college_credits >float(4):
                Totals = TotalPrice + JamesDollar + six_or_more + full +C_full+ undergrad + int_full
                if college_credits >= float(6):
                    Totals = Totals + 5
        elif college_credits >=float(12) and college_credits<float(18):
            TotalPrice = percredits*15
            Totals = TotalPrice + JamesDollar + six_or_more + full+C_full+undergrad + 5 +int_full
        elif college_credits >float(18):
            TotalPrice = ((college_credits-18) * percredits) + (percredits*15) +5
            Totals = TotalPrice + JamesDollar + six_or_more + undergrad + int_full
        TotalAllTogother = math.ceil(Totals)
        TotalAllTogother = '${:,.2f}.'.format(TotalAllTogother)
        print("Tuition is", TotalAllTogother)
        break
    start = "no"
    # here we ask if you would like to restart the loop and if you say yes it will, say no it will end.
    response = input("Do you want to do another calculation (yes/no): ")
    response = response.lower()
