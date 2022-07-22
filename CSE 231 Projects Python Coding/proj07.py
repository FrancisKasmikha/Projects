''' Your header goes here '''
#####################################################
#           Project 7     Francis Kasmikha
#     Algorithm
#   Prompt for a File Name
#   Open the file and go through the excel sheet.
#   Goes through functions(main)
#   Goes through for the for loops in each function and iteritate through the excel spread sheets.
#   will find the states or population or reps and put them into a list.
#   Based on how many states appear in the Census, It will add a Rep to the count
#   On the count, it will go off the number of times the states have appeared
#   Then will add up the reps to each state and store them in the list
#   Once you have all the information you will go and have it displayed.
#   Call for that function like you did the rest, and it will start printing off all your data
#
######################################################

import math
import csv

def open_file():
    "This function basically prompts the user for a file to read"
    "If the file exists then it will open up that file and not repeat"
    "if the file does not exist then it will go try again and say error, until the user enters a file that exists"
    start_program = "go"
    while start_program == "go":
        try:
            filename = input("Enter filename: ")
            fp = open(filename)
        except FileNotFoundError:
            print("File not found! Please try again!")
        else:
            start_program = "no"
    return fp

def calc_multipliers():
    """
    will make multipliers based on a function that your given
    will go from n=2 to n =61
    It will make a List based on the values that are calculated
    Finally will return the whole list in the end
    """
    n = 2
    mult = []
    while n < 61:
        x = 1 / math.sqrt(n * (n - 1))
        n += 1
        mult.append(x)
    return mult

def calc_priorities(s,p,m):
    """"
     This Function will establish what is a priority when given the State and the Population
     Will make two empty list in the beginning for the state and priority values
     It will go through the population and multiple that by each multiplier value
     In the end, It will make the state appear more than once and the priority value as well
     Then make it a tuple using the .zip
    """
    priority = []
    state = []
    p = int(p)
    for line in m:
        prior = line * p
        prior = int(prior)
        priority.append((prior))
        state.append((s))
    list_prior = list(zip(priority,state))
    return list_prior

def read_file_make_priorities(fp,multipliers):
    """
    Well this function is a hefty one
    What this will first do is open up a excel file using the pointer from the open file
    After that is done, We start reading the file, and then skip the header
    Create many empty list for the States,Reps,Pops, just in case we need them
    Then We make a master list, so a small list that is easier to handle than the bigger one
    Iteriate through the master list and get the name of the states and give them a rep of 1
    After that we use the calc_priorities function to get the priorities again
    """
    reader = csv.reader(fp)
    state_reps_list = []
    state =[]
    rep =[]
    population = []
    master_list = []
    the_priotities = []
    fp.readline()
    for line_list in reader:
        master_list.append(line_list)
    for line in master_list:
        if line[1] != "Puerto Rico" and line[1] != "District of Columbia":
            state.append(line[1])
            population.append(line[2])
            rep.append(line[3])
            state_reps_list.append([line[1],1])
            for state_priorities in calc_priorities(line[1],line[2],multipliers):
                the_priotities.append(state_priorities)
    my_priorities = sorted(the_priotities, reverse=True)
    state_sorted = sorted(state_reps_list)
    my_priorities = my_priorities[:385]
    return state_sorted,my_priorities


def add_to_state(state,states):
    """
    This function dosen't do too much
    Will read the priorities and every time a state shows up in the list it will add 1 to its rep value
    Adds the reps up and returns nothing
    """
    for rep in states:
        if rep[0] == state:
            rep[1] += 1
    pass
def display(states):
    """
    This function will print and display everything we have computed
    I have also included .replace to get rid of the parentheses
    """
    print("\nState          Representatives")
    for line in states:
        State_rep = line[0].replace("\"", "")
        print("{:<15s}{:>4d}".format(State_rep,line[1]))
    pass

def main():
    """
    This will basically just call the functions and give you their returned values
    Will also print out the values based on the Display Function
    """
    fp = open_file()
    calc_mult = calc_multipliers()
    state_sorted,my_priorities = read_file_make_priorities(fp,calc_mult)
    for state in my_priorities:
        add_to_state(state[1], state_sorted)
    display(state_sorted)
    pass

if __name__ == "__main__":
    main()
