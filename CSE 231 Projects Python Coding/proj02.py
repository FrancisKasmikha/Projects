import math
print("\nWelcome to car rentals. ")
print("\nAt the prompts, please enter the following: ")
print("\tCustomer's classification code (a character: BDW) ")
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)")
answer = input('''\nWould you like to continue (Y/N)? ''')
#the prompt for the numbers asking him what they want




while answer == 'Y':
    #the while here goes from if he says Y or if he dosen't will print a statement
    code= input("\nCustomer code (BDW): ")
    while code != 'B' and code != 'D' and code != 'W':
        print('\t*** Invalid customer code. Try again. ***')
        code=input("Customer code (BDW): ")
    days= input("\nNumber of days: ")
    day=float(days)
    odostant= input("Odometer reading at the start: ")
    odostart= int(odostant)
    odoemd= input("Odometer reading at the end:   ")
    odoend= int(odoemd)
    odogat= odoend-odostart
    if odoend > odostart:
        odofin =(odoend-odostart)/10
    elif odoend < odostart:
        odofin =((1000000-odostart)+odoend)/10
    odofinish=float(odofin)
    averagemiles = (odofinish/day)
    guys=float(averagemiles)
    weeks= day/7
    shift = math.ceil(weeks)
    week=float(weeks)
    weekl= day/5
    weekh=float(weekl)
    weekdo= odofinish/shift
    weekho= odofinish/weekh
    weekavg= float(weekdo)
    weekavgs=float(weekho)
#right here is where i set all my variables.
#this is where i make them a float as well.
#This is also where I make the final miles either from 1000000 and on or under




    if code == 'B':
        print('\nCustomer summary:')
        print("\tclassification code:",code)
        print("\trental period (days):",days)
        print("\todometer reading at start:",odostart)
        print("\todometer reading at end:  ",odoend)
        print("\tnumber of miles driven: ", odofinish)
        amount= (day*40)+(.25*odofinish)
        print('\tamount due: $ ', round(amount,2))
#where i print out the numbers for B if they input that
#where all the calculations are done, it is printing out the variables and making functions



    elif code == 'D':
        print('\nCustomer summary:')
        print("\tclassification code:", code)
        print("\trental period (days):", days)
        print("\todometer reading at start:", odostart)
        print("\todometer reading at end:  ", odoend)
        print("\tnumber of miles driven: ", odofinish)
        if guys<=100:
            amountsss= 60*day
        elif guys>100:
            amountsss = (((guys-100)*day)*.25)+(day*60)
        amounth=float(amountsss)
        print('\tamount due: $ ', round(amounth,2))
    #If it is D then the code will give you this
    #it is also saying at the end if the miles are above 100 or lower than 100 what computations it will do

    elif code == 'W':
        print('\nCustomer summary:')
        print("\tclassification code:", code)
        print("\trental period (days):", days)
        print("\todometer reading at start:", odostart)
        print("\todometer reading at end:  ", odoend)
        print("\tnumber of miles driven: ", odofinish)
        if weekavg>0 and weekavg<=900:
            amountw= 190 * shift
        elif weekavg<1500:
            amountw= (190*shift) + (100*shift)
        else:
            amountw= ((190*shift)+(200*shift)+((weekavg-1500)*.25*shift))
        amountrew=float(amountw)
        print('\tamount due: $', round(amountrew,2))
#the ouput if you put W
#The calculations that are made to get the answers if between 900 or lower or above 1500






    answer = input('''\nWould you like to continue (Y/N)? ''')







print("Thank you for your loyalty.")



