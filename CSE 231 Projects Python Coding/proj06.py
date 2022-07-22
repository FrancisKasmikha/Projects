''' Insert heading comments here.'''

import csv


def open_file():
    '''Insert docstring here.'''
    '''Insert docstring here.'''
    c = "go"
    while c == "go":
        try:
            filename = input("Enter filename: ")
            fp = open(filename)
        except FileNotFoundError:
            print("File not found! Please try again!")
        else:
            c ="no"
    return fp
    pass  # insert your code here


def read_file(fp):
    '''Insert docstring here.'''
    reader = csv.reader(fp)
    master_list = []
    fp.readline()
    for line_list in reader:
        master_list.append(line_list)
    return master_list

    pass  # insert your code here


def shoots_left_right(master_list):
    '''Insert docstring here.'''
    left_handed = 0
    right_handed = 0
    for line in master_list:
        handed = line[1]
        if handed == 'R':
            right_handed += 1
        elif handed== "L":
            left_handed += 1
    return left_handed,right_handed



    pass  # insert your code here


def position(master_list):
    '''Insert docstring here.'''
    C = 0
    L = 0
    D = 0
    R = 0
    for line in master_list:
        pos = line[2]
        if pos == 'R':
            R += 1
        elif pos == "L":
            L += 1
        elif pos == "D":
            D += 1
        elif pos == "C":
            C += 1

    return L, R, C, D
    pass  # insert your code here


def off_side_shooter(master_list):
    left_and_right = 0
    right_and_left = 0
    for line in master_list:
        handed = line[1]
        pos = line[2]
        if handed == "R":
            if pos == "L":
                right_and_left += 1
        elif handed == "L":
            if pos == "R":
                left_and_right +=1
    return right_and_left,left_and_right
    pass  # insert your code here


def points_per_game(master_list):
    list_prac = []
    list_real = []
    for line in master_list:
        ppg = float(line[18])
        name = line[0]
        pos = line[2]
        player_list = (ppg,name,pos)
        list_prac.append(player_list)
    list_prac.sort()
    for line in list_prac[-1:-11:-1]:
        list_real.append(line)
    return list_real
    pass  # insert your code here


def games_played(master_list):
    '''Insert docstring here.'''
    list_prac = []
    list_real = []
    for line in master_list:
        games_play = line[3]
        games_play = games_play.replace(',','')
        games_play = int(games_play)
        name = line[0]
        player_list = (games_play,name)
        list_prac.append(player_list)
    list_prac.sort()
    for line in list_prac[-1:-11:-1]:
        list_real.append(line)
    return list_real


    pass  # insert your code here


def shots_taken(master_list):
    '''Insert docstring here.'''
    list_prac = []
    list_real = []
    for line in master_list:
        shots_play = line[9]
        if shots_play == "--":
            continue
        else:
            shots_play = shots_play.replace(',','')
            shots_play = int(shots_play)
        name = line[0]
        player_list = (shots_play, name)
        list_prac.append(player_list)
    list_prac.sort()
    for line in list_prac[-1:-11:-1]:
        list_real.append(line)
    return list_real
    pass  # insert your code here


def main():
    '''Insert docstring here.'''
    fp = open_file()
    master_list = read_file(fp)
    left, right = shoots_left_right(master_list)
    print("\n\n{:^10s}".format("Shooting"))
    print("left:  {:4d}".format(left))
    print("right: {:4d}".format(right))
    L,R,C,D = position(master_list)
    print("\n{:^12s}".format("Position"))
    print("left:    {:4d}".format(L))
    print("right:   {:4d}".format(R))
    print("center:  {:4d}".format(C))
    print("defense: {:4d}".format(D))
    right_and_left,left_and_right = off_side_shooter(master_list)
    print("\n{:^24s}".format("Off-side Shooter"))
    print("left-wing shooting right: {:4d}".format(right_and_left))
    print("right-wing shooting left: {:4d}".format(left_and_right))
    print("\n{:^36s}".format("Top Ten Points-Per-Game"))
    print("{:<20s}{:>8s}{:>16s}".format("Player","Position","Points Per Game"))
    points_listt = points_per_game(master_list)
    for line in points_listt:
        print("{:<20s}{:>8s}{:>16.2f}".format(line[1],line[2],line[0]))
    print("\n{:^36s}".format("Top Ten Games-Played"))
    print("{:<20s}{:>16s}".format("Player","Games Played"))
    games_play_players = games_played(master_list)
    for line in games_play_players:
        print("{:<20s}{:>16,d}".format(line[1],line[0]))
    print("\n{:^36s}".format("Top Ten Shots-Taken"))
    print("{:<20s}{:>16s}".format("Player","Shots Taken"))
    shots_play_players = shots_taken(master_list)
    for line in shots_play_players:
        print("{:<20s}{:>16,d}".format(line[1], line[0]))

    pass  # insert your code here


if __name__ == "__main__":
    main()
