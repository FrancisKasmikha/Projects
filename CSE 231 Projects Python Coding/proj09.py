###########################################################
#  Computer Project #9
#           Francis Kasmikha
#               Algorithm
#       prompts a filename
#       open file based on what inputted, will keep asking until appropriate response
#       build dictionary based on the file that is opened
#       iterates through excel sheets
#       print header
#       reads through dict file (iterates through files later find calculations
#       Goes through for loops to calculate total spread through state and country
#       goes through for loops and if statements to return global and total global sales
#       uses plots
#       uses index and read line
#       slices
#       uses tuples, floats, ints, to calculate data
#       main function to solve test cases
#       formats functions
###########################################################

import csv
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from operator import itemgetter


def open_file():
    '''
        This function basically prompts the user for a file to read
        If the file exists then it will open up that file and not repeat
        if the file does not exist then it will go try again and say error, until the user enters a file that exists
    '''
    start_program = "go"
    while start_program == "go":
        try:
            filename = input("Data file: ")
            if filename =="":
                filename = "ncov.csv"
            fp = open(filename,encoding ='utf-8')
        except FileNotFoundError:
            print("Error. Try again.")
        else:
            start_program = "no"
    return fp

    
    pass


def build_dictionary(fp):
    '''
        Gets the master dictionary of countrys with areas infected.
        A dictionary inside of a dictionary with a tuple inside of that

        This function accepts the previously generated file pointer as input and returns the
        required dictionary.
    '''
    master_dict= {}
    reader = csv.reader(fp)
    fp.readline()
    for line in reader:
        try:
            country = line[2]
            area = line[1]
            if area == "":
                area = "N/A"
            last_update = line[3]
            cases = line[4]
            deaths = line[5]
            recovered = line[6]
        except:
            continue
        Dict = {}
        Dict[area] = (last_update, int(cases), int(deaths), int(recovered))
        if country in master_dict:
            master_dict[country] += [Dict]
        else:
            master_dict[country] = [Dict]
    return master_dict
    

def top_affected_by_spread(master_dict):
    '''
        This function accepts the data dictionary as created by the function above and returns
        a sorted list (in descending order) of the top 10 countries with the most areas affected
        by nCoV
    '''
    D1 = {}
    D2 = {}
    for countrie, area in master_dict.items():
        for areas in area:
            for key, value in areas.items():
                if countrie in D1:
                    D1[countrie] += 1
                else:
                    D1[countrie] = 1
    for key in sorted(D1.keys()):
        D2[key] = D1[key]
    listoftuples = sorted(D2.items(), key=lambda x: x[1], reverse=True)
    return listoftuples[0:10]


def top_affected_by_numbers(master_dict):
    '''
        This function accepts the data dictionary and produces a sorted list of the top 10 countries with
        the most total people affected within every country
    '''
    D1 = {}
    D2 = {}
    for countrie, area in master_dict.items():
        for areas in area:
            for key, value in areas.items():
                if countrie in D1:
                    D1[countrie] += value[1]
                else:
                    D1[countrie] = value[1]
    for key in sorted(D1.keys()):
        D2[key] = D1[key]
    listoftuples = sorted(D2.items(), key=lambda x: x[1], reverse=True)
    return listoftuples[0:10]

def is_affected(master_dict, country):
    '''
        This function takes in the data dictionary and the name of a country (string) and
        returns a Boolean (True or False) depending on whether a country is affected
        by nCoV
    '''
    try:
        if len(country) == 2:
            country = country.upper()
        elif len(country) > 2:
            country = country.title()
    except:
        pass
    try:
        for key in master_dict[country]:
            pass
        return True
    except:
        return False



def plot_by_numbers(list_of_countries, list_of_numbers):
    '''
        This function plots the number of areas/people inffected by country.
        
        parameters: 
            list_of_countries: list of countries
            list_of_numbers: list of the number of areas/people inffected
            
        Returns: None
    '''
    fig, ax = plt.subplots()
    
    x_pos = [i for i, _ in enumerate(list_of_countries)]
    
    ax.barh(x_pos, list_of_numbers, align='center', color='red')
    ax.set_yticks(x_pos)
    ax.set_yticklabels(list_of_countries)
    ax.invert_yaxis()
    ax.set_xlabel('Count')
    ax.set_title('Novel Coronavirus statistics')
    
    plt.show()


def affected_states_in_country(master_dict, country):

    '''
        This function takes in the data dictionary and the name of a country (string) and
        returns a set of affected areas within a country
    '''
    try:
        if len(country) == 2:
            country = country.upper()
        elif len(country) > 2:
            country = country.title()
    except:
        pass
    my_set= set()
    try:
        for key in master_dict[country]:
            for keys, value in key.items():
                my_set.add(keys)
    except:
        pass
    return my_set


def main():
    """"
    The main function prints the provided BANNER and MENU and then asks the user
    to make a choice between the various available options shown in the menu. If the user inputs
    something other than an integer, print an error message and reprompt.
    """
    BANNER = '''
.__   __.   ______   ______   ____    ____
|  \ |  |  /      | /  __  \  \   \  /   /
|   \|  | |  ,----'|  |  |  |  \   \/   / 
|  . `  | |  |     |  |  |  |   \      /  
|  |\   | |  `----.|  `--'  |    \    /   
|__| \__|  \______| \______/      \__/  
    '''
    print(BANNER)
    MENU = ''' 
[1] Countries with most areas infected
[2] Countries with most people affected
[3] Affected areas in a country
[4] Check if a country is affected
[5] Exit

Choice: '''
    fp = open_file()
    master_dict = build_dictionary(fp)
    choice = input(MENU)
    while choice != "5":

        if choice == "1":
            print("{:<20s} {:15s}".format("Country", "Areas affected"))
            print("----------------------------------------")
            top_affected_area = top_affected_by_spread(master_dict)
            x_list = []
            y_list =[]
            for line in top_affected_area:
                print("{:<20s} {:5d}".format(line[0],line[1]))
                x_list.append(line[0])
                y_list.append(line[1])
            x_list = x_list[0:5]
            y_list = y_list[0:5]
            plot = input('Plot? (y/n) ')
            if plot == "y":
                plot_by_numbers(x_list,y_list)

        if choice == "2":
            print("{:<20s} {:15s}".format("Country", "People affected"))
            print("----------------------------------------")
            top_affected_cases = top_affected_by_numbers(master_dict)
            x_list = []
            y_list = []
            for line in top_affected_cases:
                print("{:<20s} {:5d}".format(line[0], line[1]))
                x_list.append(line[0])
                y_list.append(line[1])
            x_list = x_list[1:6]
            y_list = y_list[1:6]
            plot = input('Plot? (y/n) ')
            if plot == "y":
                plot_by_numbers(x_list, y_list)
        if choice == "3":
            try:
                country = input("Country name: ")
                countries = affected_states_in_country(master_dict,country)
                print("-"*30)
                if len(countries) == 0:
                    print("Error. Country not found.")
                if len(countries) > 0:
                    print("{:<30s}".format("Affected area"))
                    print("-" * 30)
                    countries = sorted(countries)
                    for i,t in enumerate(countries, start=1):
                        print("[{:02d}] {:<30s}".format(i,t))
            except:
                print("Error. Try again.")
        if choice == "4":
            country =input("Country name: ")
            print("-"*30)
            countries = is_affected(master_dict,country)
            if countries == True:
                print("{} is affected.".format(country))
            if countries == False:
                print("{} is not affected.".format(country))
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
            print("Error. Try again.")

        choice = input(MENU)
    print("Stay at home. Protect your community against COVID-19")
if __name__ == "__main__":    
    main()