'''
               Project 8
            Francis Kasmikha

Starts off by asking for the file name
The program will ask for a input value
based up on that value it will open up certain functions.
will ask you for a value weather that is a year or platform
It will also ask you for a key if you submit 4
Will continually ask you for values until you choose 5 for an input
will also plot the information if you would like it to do so.
'''

import csv
from operator import itemgetter
import pylab

def open_file():
    '''
        This function basically prompts the user for a file to read
        If the file exists then it will open up that file and not repeat
        if the file does not exist then it will go try again and say error, until the user enters a file that exists
    '''
    start_program = "go"
    while start_program == "go":
        try:
            filename = input("Enter filename: ")
            fp = open(filename,encoding ='utf-8')
        except FileNotFoundError:
            print("File not found! Please try again!")
        else:
            start_program = "no"
    return fp

def read_file(fp):
    '''
        this function will have 6 open dictionaries
        It will read the csv file, that you open in open file.
        Will collect values for name,genre,publisher
        Will add up sales values to make a global sales
        then will start adding to dictionaries, if it does exist in the dictionary it will add it and if it doesnt it
        will add a new key, value
        Then once the entire dictionaries is made, it will sort them and start adding the new key and values into the
        final dictionary
    '''
    D1 ={}
    D2 = {}
    D3 = {}
    D1_final = {}
    D2_final ={}
    D3_final = {}
    reader = csv.reader(fp)
    for line in reader:
        try:
            name = (line[0].strip()).lower()
            platform = (line[1].strip()).lower()
            genre = (line[3].strip()).lower()
            publisher = (line[4].strip()).lower()
            year = int(line[2])
            na_sales = (float(line[5])*1000000)
            europe_sales =(float(line[6])*1000000)
            japan_sales = (float(line[7])*1000000)
            other_sales= (float(line[8])*1000000)
        except:
            continue
        global_sales = europe_sales + japan_sales + na_sales + other_sales

        if name in D1:
            D1[name] += [(name,platform,year,genre,publisher,global_sales)]
        else:
            D1[name] = [(name,platform,year,genre,publisher,global_sales)]
        if genre in D2:
            D2[genre] += [(genre,year,na_sales,europe_sales,japan_sales,other_sales,global_sales)]
        else:
            D2[genre] = [(genre,year,na_sales,europe_sales,japan_sales,other_sales,global_sales)]

        if publisher in D3:
            D3[publisher] += [(publisher,name,year,na_sales,europe_sales,japan_sales,other_sales,global_sales)]
        else:
            D3[publisher] = [(publisher,name,year,na_sales,europe_sales,japan_sales,other_sales,global_sales)]
    for i in sorted(D1):
        D1_final[i] = sorted(D1[i], key=itemgetter(5), reverse=True)
    for i in sorted(D2):
        D2_final[i] = sorted(D2[i], key=itemgetter(6), reverse=True)
    for i in sorted(D3):
        D3_final[i] = sorted(D3[i], key=itemgetter(7), reverse=True)

    return D1_final,D2_final,D3_final


def get_data_by_column(D1, indicator, c_value):
    '''
        will create a master list, that is empty
        then go through the values in D1 and look through each line in the values and if indicator is year then will
        look at line =[2] and if indicator is platform then will look at line = [2]
        will then append the line in values if platform or year is found
        at the end it will sort it alphabetically and by global sales
    '''
    master_list = []
    for value in D1.values():
        for line in value:
            if indicator == "year":
                num =1
                if line[2] == c_value:
                    master_list.append(line)
            if indicator == "platform":
                num =2
                if line[1] == c_value:
                    master_list.append(line)
    master_list = sorted(master_list, key=itemgetter(5), reverse=True)
    master_list = sorted(master_list, key=itemgetter(num))
    return master_list

def get_publisher_data(D3, publisher):
    '''
        Make and empty list
        iteriate through the keys in D3
        if the key is equal to the publisher that was entered
        that line in the value for the key will be added to the tuple
        will sort it alphabetically and then by the sales in descending order
    '''
    tuple_list =[]
    for key in D3.keys():
        if key == publisher:
            for line in D3[key]:
                tuple_list.append(line)
    tuple_list = sorted(tuple_list, key=itemgetter(1))
    tuple_list = sorted(tuple_list, key=itemgetter(7), reverse=True)
    return tuple_list

def display_global_sales_data(L, indicator):
    '''
        this function is here so that you can print the information from the list
        if my indicator is year or platform that will change the header that I print out
        will then print out the information by iterating through the entire list
        if its year i will use Line[2] of the list and if its platform I will use line[1]
        Will then add up the total sales and keep adding them to a counter
        will print out Total Sales in the end
    '''
    header1 = ['Name', 'Platform', 'Genre', 'Publisher', 'Global Sales']
    header2 = ['Name', 'Year', 'Genre', 'Publisher', 'Global Sales']
    if indicator == "year":
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Year', 'Genre', 'Publisher', 'Global Sales'))
        total_global= 0
        for line in L:
            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(line[0][:25],str(line[2]),line[3][:15],line[4][:25],line[5]))
            total_global += int(line[5])
        print("\n{:90s}{:<12,.02f}".format("Total Sales", total_global))
    elif indicator == "platform":
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Platform', 'Genre', 'Publisher', 'Global Sales'))
        total_global = 0
        for line in L:
            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(line[0][:25], line[1], line[3][:15], line[4][:25], line[5]))
            total_global += int(line[5])
        print("\n{:90s}{:<12,.02f}".format("Total Sales",total_global))

def get_genre_data(D2, year):
    '''
        Will make an empty list
        will iterate through the values in D2
        set my counts to 0 and as I read through each value
        add to my counters
        If my counters is bigger than 0 then it will append the tuple into the list
    '''
    tuple_list = []
    for value in D2.values():
        count = 0
        tot_na_sales = 0
        total_eur_sales = 0
        total_jpn_sales = 0
        total_other_sales = 0
        total_global_sales = 0
        for line in value:
            if year == line[1]:
                count += 1
                gen = line[0]
                na_sales = line[2]
                tot_na_sales += na_sales
                europe_sales = line[3]
                total_eur_sales += europe_sales
                japan_sales = line[4]
                total_jpn_sales += japan_sales
                other_sales = line[5]
                total_other_sales += other_sales
                global_sales = line[6]
                total_global_sales += global_sales
        if count > 0:
            tuple_list.append((gen, count, tot_na_sales, total_eur_sales, total_jpn_sales, total_other_sales,total_global_sales))
    tuple_list = sorted(tuple_list, key=itemgetter(0))
    tuple_list = sorted(tuple_list, key=itemgetter(6), reverse=True)
    return tuple_list

    
def display_genre_data(genre_list):
    '''
        Function here to print out all information
        Will print the header first
        set total sales to 0
        iterate through the list and have the values printed
        have the sales added to the counter at the end each time
        print the total sales in the end
    '''
    header = ['Genre', 'North America', 'Europe', 'Japan', 'Other', 'Global']
    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format('Genre', 'North America', 'Europe', 'Japan', 'Other', 'Global'))
    total_sales = 0
    for line in genre_list:
        print("{:15s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(line[0],line[2],line[3],line[4],line[5],line[6],))
        total_sales += float(line[6])
    print("\n{:75s}{:<15,.02f}".format("Total Sales",total_sales))
    pass

def display_publisher_data(pub_list):
    '''
        function here to print the publisher data
        will print the header out in the first part
        will set a counter for total sales
        iterate through the list and have the values printed out in the correct order
        will keep adding to the total sales counter
        print the total sales in the end
    '''
    print("{:30s}{:15s}{:15s}{:15s}{:15s}{:15s}".format('Title', 'North America', 'Europe', 'Japan', 'Other', 'Global'))
    total_sales = 0
    for line in pub_list:
        print("{:30s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(line[1][:25],line[3],line[4],line[5],line[6],line[7],))
        total_sales += (line[7])
    print("\n{:90s}{:<15,.02f}".format("Total Sales",total_sales))
    pass
def get_totals(L, indicator):
    '''
        will make 2 empty list and an empty dictionary
        iterate through the list
        if indicator is year will go through index 1 and index 5 to make a dictionary
        if indicator is platform go through index 2 and index 5 to make a dictionary
        sort the dictionary in the end and append the key and the value
        return the two list in the end
    '''
    L1 = []
    L2 = []
    D = {}
    for line in L:
        if indicator == "year":
            if line[1] in D:
                D[line[1]] += line[5]
            else:
                D[line[1]] = line[5]
        if indicator == "platform":
            if line[2] in D:
                D[line[2]] += line[5]
            else:
                D[line[2]] = line[5]
    for key in sorted(D):
        L1.append(key)
        L2.append(D[key])
    return L1,L2


def prepare_pie(genres_list):
    '''
        will make two empty list
        will make a master list
        iterate through the genre list
        making the master list by adding the value in genre list
        then sorting them alphabetically and by the global sales
        then will goes through the master list and add those new values to 2 lists
        will return the two list
    '''
    L1= []
    L2=[]
    master_list = []
    for line in genres_list:
        master_list.append(line)
    master_list = sorted(master_list,key=itemgetter(0))
    master_list = sorted(master_list,key=itemgetter(6), reverse=True)
    for line in master_list:
        L1.append(line[0])
        L2.append(line[6])
    return L1,L2
    
    pass

def plot_global_sales(x,y,indicator, value):
    '''
        This function plots the global sales per year or platform.
        
        parameters: 
            x: list of publishers or year sorted in ascending order
            y: list of global sales that corresponds to x
            indicator: "publisher" or "year"
            value: the publisher name (str) or year (int)
        
        Returns: None
    '''
    
    if indicator == 'year':    
        pylab.title("Video Game Global Sales in {}".format(value))
        pylab.xlabel("Platform")
    elif indicator == 'platform':    
        pylab.title("Video Game Global Sales for {}".format(value))
        pylab.xlabel("Year")
    
    pylab.ylabel("Total copies sold (millions)")
    
    pylab.bar(x, y)
    pylab.show()

def plot_genre_pie(genre, values, year):
    '''
        This function plots the global sales per genre in a year.
        
        parameters: 
            genre: list of genres that corresponds to y order
            values: list of global sales sorted in descending order 
            year: the year of the genre data (int)
        
        Returns: None
    '''
            
    pylab.pie(values, labels=genre,autopct='%1.1f%%')
    pylab.title("Video Games Sales per Genre in {}".format(year))
    pylab.show()
    
def main():
    # Menu options for the program
    '''
    parameter:
    will ask for a choice input
    ask for either a year or a platiform or publisher key based up on you choice in choice
    ask to plot or not
    ask for index value if choice is 4
    calls the functions and prints out the values from the display functions

    returns nothing

    '''
    MENU = '''Menu options
    
    1) View data by year
    2) View data by platform
    3) View yearly regional sales by genre
    4) View sales by publisher
    5) Quit
    
    Enter choice: '''
    fp = open_file()
    D1,D2,D3 = read_file(fp)
    choice = input(MENU)
    while choice != '5':


        if choice == "1":
            start_program = "go"
            while start_program == "go":
                try:
                    c_value = int(input("Enter year: "))
                    D = get_data_by_column(D1, "year", c_value)
                    if len(D) == 0:
                        print("The selected year was not found in the data.")
                    else:
                        print("\n{:^80s}".format("Video Game Sales in {}".format(c_value)))
                        display_global_sales_data(D, "platform")
                        plot = input("Do you want to plot (y/n)? ")
                        if plot == "y":
                            L1, L2 = get_totals(D, "year")
                            plot_global_sales(L1, L2, "year", c_value)
                except ValueError:
                    print("File not found! Please try again!")
                    start_program = "no"
                else:
                    start_program = "no"

        if choice == "2":
            start_program = "go"
            while start_program == "go":
                try:
                    c_value = (input("Enter platform: "))
                    if c_value.isalpha() == False:
                        c= int("abc")
                        d = 5 + c
                    D = get_data_by_column(D1, "platform", c_value)
                    if len(D) == 0:
                        print("The selected platform was not found in the data.")
                    else:
                        print("\n{:^80s}".format("Video Game Sales for {}".format(c_value)))
                        display_global_sales_data(D, "year")
                        plot = input("Do you want to plot (y/n)? ")
                        if plot == "y":
                            L1, L2 = get_totals(D, "platform")
                            plot_global_sales(L1, L2, "platform", c_value)
                except ValueError:
                    print("File not found! Please try again!")
                    start_program = "no"
                else:
                    start_program = "no"
        if choice == "3":
            start_program = "go"
            while start_program == "go":
                try:
                    c_value = int(input("Enter year: "))
                    D = get_genre_data(D2, c_value)
                    if len(D) == 0:
                        print("The selected year was not found in the data.")
                    else:
                        print("\nRegional Video Games Sales per Genre")
                        display_genre_data(D)
                        plot = input("Do you want to plot (y/n)? ")
                        if plot == "y":
                            L1, L2 = prepare_pie(D)
                            plot_genre_pie(L1, L2, c_value)
                except ValueError:
                    print("Invalid year")
                    start_program = "no"
                else:
                    start_program = "no"

        if choice == "4":
            start_program = "go"
            while start_program =="go":
                try:
                    pub_input = input("Enter keyword for publisher: ")
                    match = []
                    dict_match ={}
                    for key in D3:
                        if pub_input in key:
                            dict_match[key]= 0
                    for line in dict_match:
                        match.append(line)
                    if len(match) > 1:
                        print("There are {} publisher(s) with the requested keyword!".format(len(match)))
                        for i, t in enumerate(match):
                            print("{:<4d}{}".format(i, t))
                        index_input = input("Select the index for the publisher to use: ")
                        pointer = match[int(index_input)]
                        if pointer in D3:
                            List = get_publisher_data(D3,pointer)
                            print(("\nVideo Games Sales for {}".format(pointer)))
                            display_publisher_data(List)
                        # PROMPT USER FOR INDEX
                    if len(match) < 1:
                        index = 0
                        print('No publisher name containing "{}" was found!'.format(pub_input))
                except ValueError:
                    start_program = "no"
                except IndexError:
                    start_program = "no"
                else:
                    start_program = "no"
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice!= "5":
            print("Invalid option. Please Try Again!")

        choice = input(MENU)
    print("\nThanks for using the program!")
    print("I'll leave you with this: \"All your base are belong to us!\"")

if __name__ == "__main__":
    main()