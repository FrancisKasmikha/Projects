'''
                 Project 10
            Francis Kasmikha
    Take in a input
    uses classes to make montana card game
    will first intialize the list of list that we will create from the module
    Then we have the display function of course will display the printed answer
    validate move whcih will see if this move can even e=be made or not
    then movie, based on validate they are almost the same
    will shuffle the cards, so it will do so based on how you want the game played
    check if you won and at the end ask for more inputs and if user quits the game ends
    Execute Order 66, signing off
    exhausted
'''

#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same random number (needed to replicate tests)

D = cards.Deck()

def initialize():
    '''
        That function has no parameters. It creates, initializes, and returns the tableau. This corresponds
        to the setup in the game rules:
        •tableau is a list of 4 lists, each list containing 13 cards or empty spaces (aces). The
        first element of tableau is the leftmost column when displayed
    '''
    D.shuffle()
    master_tableau = []
    tableau_1 = []
    tableau_2 = []
    tableau_3 = []
    tableau_4 = []
    for _ in range(13):
        tableau_1.append(D.deal())
    for _ in range(13):
        tableau_2.append(D.deal())
    for _ in range(13):
        tableau_3.append(D.deal())
    for _ in range(13):
        tableau_4.append(D.deal())
    master_tableau.append(tableau_1)
    master_tableau.append(tableau_2)
    master_tableau.append(tableau_3)
    master_tableau.append(tableau_4)
    return master_tableau
    pass
    
def display(tableau):
    '''
        This function displays the current state of the game.
        It display four rows of 13 cards with row and column labels.
        Ace is displayed with a blank.
        
        parameters: 
            tableau: data structure representing the tableau 
        
        Returns: None
    '''

    print("{:3s} ".format(' '), end = '')
    for col in range(1,14):
        print("{:3d} ".format(col), end = '')
    print()
        
    for r,row_list in enumerate(tableau):
        print("{:3d}:".format(r+1), end = '')
        for c in row_list:
            if c.rank() == 1:
                print("  {}{}".format(' ',' '), end = '')
            else:
                print("{:>4s}".format(str(c)),end = '')
        print()

def validate_move(tableau, source_row, source_col, dest_row, dest_col,):
    '''
        That function has five parameters: the data structure representing the tableau and four ints the
        source row & column and the destination row & column. Row and column ints are in the
        ranges 0 <= row <= 3 and 0 <= column <= 12. The function will return True, if the move is
        valid; and False, otherwise
    '''
    source_rows = tableau[source_row]
    source_card = source_rows[source_col]
    dest_rows = tableau[dest_row]
    dest_card = dest_rows[dest_col]
    dest_card2 = dest_rows[dest_col-1]
    source_rank = source_card.rank()-1
    if dest_card.rank() == 1 and dest_col ==0 and source_card.rank() == 2:
        return True
    if dest_card.rank() == 1 and dest_col != 0 and dest_card2.suit() == source_card.suit() and dest_card2.rank() == (source_rank):
        return True
    return False
def move(tableau,source_row,source_col,dest_row,dest_col):
    '''
        That function has five parameters: the data structure representing the tableau and four ints the
        source row & column and the destination row & column. Row and column ints are in the
        ranges 0 <= row <= 3 and 0 <= column <= 12. If the move is valid, the function will update the
        tableau and return True; otherwise, it will do nothing to it and return False.
    '''
    source_rows = tableau[source_row]
    source_card = source_rows[source_col]
    dest_rows = tableau[dest_row]
    dest_card = dest_rows[dest_col]
    dest_card2 = dest_rows[dest_col-1]
    source_rank = source_card.rank()-1
    if dest_card.rank() == 1 and dest_col ==0 and source_card.rank() == 2:
        test = tableau[source_row][source_col]
        tableau[source_row][source_col] = tableau[dest_row][dest_col]
        tableau[dest_row][dest_col] = test
        return True
    if dest_card.rank() == 1 and dest_col != 0 and dest_card2.suit() == source_card.suit() and dest_card2.rank() == (source_rank):
        test = tableau[source_row][source_col]
        tableau[source_row][source_col] = tableau[dest_row][dest_col]
        tableau[dest_row][dest_col] = test
        return True
    return False
    pass
  
def shuffle_tableau(tableau):
    '''
    :parameter tableau

    :return shuff;ed tableau
        Only some cards are shuffled: cards that are already in a same-suit sequence starting with a 2 in
        the leftmost column are left in place and not shuffled. All other cards are shuffled and then dealt
        back into the tableau, but there will be one blank space in each row and it will be at the right end
        of the sequence that is left in place (or in the leftmost column,
    '''
    shuffle_list = []
    for tab in tableau:
        universal_suit = tab[0].suit()
        index = 0
        ice = 0
        for i,x in enumerate(tab,start=2):
            if x.rank() == i and x.suit() == universal_suit and ice == 0:
                index += 1
                i +=1
            if x.rank() != i and x.suit() != universal_suit:
                ice += 50
        for x in tab[index:]:
            shuffle_list.append(x)
        for x in tab[index:]:
            tab.pop()
    random.shuffle(shuffle_list)
    ace_list = []
    for i, shuf in enumerate(shuffle_list, start=0):
        if shuf.rank() == 1:
            ace_list.append(shuffle_list[i])
    for i, shuf in enumerate(shuffle_list, start=0):
        if shuf.rank() == 1:
            shufs = shuffle_list.pop(i)
    for i,tab in enumerate(tableau):
        if 0<= i <= 3:
            tab.append(ace_list[i])
    i = 0
    for tab in tableau:
        while len(tab) < 13:
            tab.append(shuffle_list[i])
            i +=1
    return tableau
    pass

def check_win(tableau):
    '''
        That function has one parameter: the data structure representing the tableau. The game is won
        when each row of the tableau is an increasing sequence of cards of the same suit starting with a 2
        in the leftmost column up through a king in the next to last column with a blank space
    '''
    for line in tableau:
        universal_suit = line[0].suit()
        count = 2
        for x in line[0:12]:
            if x.suit() != universal_suit:
                return False
            if x.rank() == count:
                count +=1
            else:
                return False
    return True
    pass
             
def main():
    '''
 Once you write all your function, it is time to write your main function:
a) Your program should start by initializing the tableau.
b) Display the tableau.
c) Ask to input an option and check the validity of the input.
d) If ‘Q’, quit the game
e) If ‘S’, shuffle the tableau and display the tableau
f) If ‘Sr Sc Dr Dc’, move card from Tableau (Sr, Sc) to empty Tableau (Dr, Dc).
g) If none of these options, the program should display an error message.
h) The program should repeat until the user won or quit the game.
i) Then ask if the user wants another game
j) Display a goodbye message.
    '''
    tableau = initialize()
    print("Montana Solitaire.")
    display(tableau)
    option = input("Enter choice:\n (q)uit, (s)huffle, or space-separated: source_row,source_col,dest_row,dest_col: ")
    shuf_count = 0
    while option != "q":
        if option == "s":
            if shuf_count < 2:
                shuffle_tableau(tableau)
                display(tableau)
                shuf_count += 1
            else:
                print("No more shuffles remain.")
                option = input("Enter choice:\n (q)uit, (s)huffle, or space-separated: source_row,source_col,dest_row,dest_col: ")
                option = option.lower().split(" ")
                play_again = input("Do you want to play again (y/n)?").lower()
                if play_again == "y":
                    main()
                else:
                    break

        try:
            if option != "s":
                option_tuple = option.strip().split()
                str_1 = int(option_tuple[0]) -1
                str_3 = int(option_tuple[1]) -1
                str_5 = int(option_tuple[2])-1
                str_7 = int(option_tuple[3])-1
                do_it ="yes"
                if 0<=str_1<=3:
                    if 0<=str_5<=3:
                        if 0 <=str_3<=12:
                            if 0<=str_7<=12:
                                do_it = "go"
                else:
                    print("Error: row and/or column out of range. Please Try again.")
                    do_it = "no"
                valid_tab = validate_move(tableau, str_1, str_3, str_5, str_7)
                if valid_tab == True and do_it == "go":
                    move(tableau, str_1, str_3, str_5, str_7)
                    display(tableau)
                else:
                    print("Error: invalid move.  Please try again.")
                    start = "no"
        except:
            print("Error: invalid input.  Please try again.")
        win = check_win(tableau)
        if win == True:
            print("You won!")
            play_again = input("Do you want to play again (y/n)?").lower()
            if play_again == "y":
                main()
            else:

                break
        option = input("Enter choice:\n (q)uit, (s)huffle, or space-separated: source_row,source_col,dest_row,dest_col: ")
    print("Thank you for playing.")
if __name__ == "__main__":
    main()  