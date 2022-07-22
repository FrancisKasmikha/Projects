##################################
# Computer Project   4
#  Functions
#    prompt for an Calculation
#    input a value for N or X
#    loop while not end-of-data
#       calls a function based on what you inputed
#       output your approximation
#       output the approximation through the Math Module
#       Then calculates the Difference
#       Will prompt user again
#    display closing message if X is inputed
############################

import math



def display_options():

    MENU = '''\nPlease choose one of the options below:
             A. Display the sum of squares of the first N natural numbers.         
             B. Display the approximate value of Pi.
             C. Display the approximate value of the sine of X.
             D. Display the approximate value of the cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''

    print(MENU)


def sum_natural_squares(N):
    '''Insert docstring here.'''
    N = int(N)
    sum_sq = 0
    term = 0
    n = 0
    while n < N:
        n +=1
        term = n**2
        sum_sq += term
    return sum_sq

    pass  # insert your code here


def approximate_pi():
    '''Insert docstring here.'''
    term = 1
    sum_pi = 0
    n=1
    EPSILON = 1.0e-7
    while abs(term) > EPSILON:
        sum_pi += 4 * term
        term = (((-1)**n)/((2*n)+1))
        n += 1
    return sum_pi


    pass  # insert your code here


def approximate_sin(x):
    '''Insert docstring here.'''
    term = x
    sum_sin = 0
    n = 1
    EPSILON = 1.0e-7
    while abs(term) > EPSILON:
        sum_sin += term
        term = (((-1)**n)*((x)**(2*n+1)))/(math.factorial((2*n+1)))
        n += 1
    return sum_sin


    pass  # insert your code here


def approximate_cos(x):
    '''Insert docstring here.'''
    x = float(x)
    term = (-1*(x)**2)/(math.factorial(2))+1
    sum_cos = 0
    n = 2
    EPSILON = 1.0e-7
    while abs(term) > EPSILON:
        sum_cos += term
        term = (((-1)**n)*((x)**(2*n)))/(math.factorial((2*n)))
        n += 1
    return sum_cos


    pass  # insert your code here

def call_letter():
    letter = input("\n\tEnter option: ")
    letter = letter.lower()
    return letter

def main(x,y):
    z=y
    if x == 1:
        sum_natural = sum_natural_squares(z)
        print("\n\tThe sum: ",sum_natural)
    if x == 2:
        sum_pi = approximate_pi()
        print("\n\tApproximation:", format(sum_pi,'.10f'))
        print("\tMath module:  ", format(math.pi,'.10f'))
        if math.pi > sum_pi:
            diff = (math.pi)- (sum_pi)
        elif sum_pi > math.pi:
            diff = (sum_pi)- (math.pi)
        print("\tdifference:   ",format(diff,'.10f'))
    if x == 3:
        z = float(y)
        sin_sum = approximate_sin(z)
        sum_mod = math.sin(z)
        print("\n\tApproximation:", format(sin_sum,'.10f'))
        print("\tMath module:  ", format(sum_mod,'.10f'))
        if sin_sum > math.sin(y):
            diff = (sin_sum)- (math.sin(y))
        elif math.sin(y) > sin_sum:
            diff = (math.sin(y))- (sin_sum)
        elif math.sin(y)==sin_sum:
            diff = 0
        print("\tdifference:   ", format(diff,'.10f'))

    if x ==4:
        z = float(y)
        sin_cos = approximate_cos(y)
        sum_mod = math.cos(z)
        print("\n\tApproximation:", format(sin_cos,'.10f'))
        print("\tMath module:  ", format(sum_mod,'.10f'))
        if sin_cos > math.cos(z):
            diff = (sin_cos)- (math.cos(z))
        elif math.cos(z) > sin_cos:
            diff = (math.cos(y))- (sin_cos)
        elif math.cos(z)== sin_cos:
            diff = 0

        print("\tdifference:   ", format(diff,'.10f'))





        pass  # insert your code here

if __name__ == "__main__":
    run = "yes"
    while run == "yes":
        display_options()
        dog ='go'
        while dog =="go":
            letter = call_letter()
            if letter != "a" and letter != "b" and letter != "c" and letter != "d" and letter != "m" and letter != "x":
                letter = letter.upper()
                letters = letter.strip("\'")
                print("\nError:  unrecognized option [{}]".format((letter)))
                run ="yes"
                dog ="no"
            elif letter == "a" or letter == "b" or letter == "c" or letter == "d":
                Prog = letter
                if Prog == "a":
                    a=1
                    OptionA = input("\nEnter N: ")
                    if not OptionA.isdigit() or int(OptionA) <= 0:
                        print("\n\tError: N was not a valid natural number. [{}]".format(OptionA))
                        dog = "go"
                    elif OptionA.isdigit():
                        b = int(OptionA)
                        main(a,b)
                elif Prog == "b":
                    b=2
                    a=0
                    main(b,a)
                elif Prog == "c":
                    a = 3
                    OptionC = input("\n\tEnter X: ")
                    if OptionC.isalpha():
                        print("\n\tError: X was not a valid float. [{}]".format(OptionC))
                        dog = "go"
                    elif not OptionC.isalpha():
                        b = float(OptionC)
                        main(a,b)
                elif Prog == "d":
                    a = 4
                    OptionD = input("\n\tEnter X: ")
                    if OptionD.isalpha():
                        print("\n\tError: X was not a valid float.  [{}]".format(OptionD))
                        dog = "go"
                    elif not OptionD.isalpha():
                        b = float(OptionD)
                        main(a,b)





            elif letter == "m":
                run ="yes"
                dog ="no"
            elif letter == 'x':
                print("Hope to see you again.")
                run = "no"
                dog = "no"
            ''

