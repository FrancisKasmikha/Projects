''' Insert heading comments here.'''
#########################################
#Project 5 CSE 231 Francis Kasmikha
#ask for a file name
#will take the file name and see the us value
#will then take all the values and test to see for the minimum value
#will then take the values and test for maximum value
#Then will do herd immunity and see if its less than 90 percent
# will then print the herd immunity
#now we will take all that information and make it into a file
#
##########################################

def open_file():
    '''Insert docstring here.'''
    c = "go"
    while c == "go":
        try:
            filename = input("Input a file name: ")
            fp = open(filename)
        except FileNotFoundError:
            print("Error: file not found. Please try again.")
        else:
            c ="no"
    return fp
    
def get_us_value(fp):
    '''Insert docstring here.'''
    for line in fp:
        state =  line[:25].strip()
        if state =="United States":
            percentage = float((line[25:].strip()))
    return percentage
    
def get_min_value_and_state(fp):
    fp.seek(0)
    title = fp.readline()
    header = fp.readline()
    min_value = 125
    for line in fp:
        try:
            percentage = float((line[25:].strip()))
        except ValueError:
            fp.readline()
        if percentage < min_value:
            min_value = percentage
            state = line[:25].strip()

    return state,min_value



def get_max_value_and_state(fp):
    '''Insert docstring here.'''
    fp.seek(0)
    title = fp.readline()
    header = fp.readline()
    max_value = 5
    for line in fp:
        try:
            percentage = float((line[25:].strip()))
        except ValueError:
            fp.readline()
        if percentage > max_value:
            max_value = percentage
            state = line[:25].strip()

    return state,max_value
        
def display_herd_immunity(fp):
    '''Insert docstring here.'''
    fp.seek(0)
    title = fp.readline()
    startline = fp.readline()
    print("\nStates with insufficient Measles herd immunity.")
    print("{:<25s}{:>5s}".format("State","Percent"))
    for line in fp:
        try:
            percentage = float((line[25:].strip()))
            if percentage < 90.0:
                state = line[:25].strip()
                print("{:<25}{:>5}%".format(state, percentage))
        except ValueError:
            fp.readline()
    return

    pass  # insert your code here

def write_herd_immunity(fp):
    '''Insert docstring here.'''
    fp.seek(0)
    file_write= open('herd.txt', "w")
    file_write.write("\nStates with insufficient Measles herd immunity.\n")
    file_write.write("{:<25s}{:>5s}\n".format("State","Percent"))
    for line in fp:
        try:
            percentage = float((line[25:].strip()))
            if percentage < 90.0:
                state = line[:25].strip()
                file_write.write("{:<25}{:>5}%\n".format(state, percentage))
        except ValueError:
            fp.readline()


    file_write.close()






    pass  # insert your code here

def main():   
    '''Insert docstring here.'''
    fp = open_file()
    title = fp.readline()
    header = fp.readline()
    print("\n" + title)
    value = get_us_value(fp)
    print("\nOverall US MMR coverage: {}%".format(value))
    min_state, min_value = get_min_value_and_state(fp)
    print("State with minimal MMR coverage: {} {}%".format(min_state,min_value))
    max_state, max_value = get_max_value_and_state(fp)
    print("State with maximum MMR coverage: {} {}%".format(max_state, max_value))
    write_herd_immunity(fp)






    displayherd =display_herd_immunity(fp)



if __name__ == "__main__":
    main()    
