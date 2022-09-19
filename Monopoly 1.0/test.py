# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:52:22 2021

@author: 4664
"""
import time, string


database = {'p1': [0, 1500, {1 : 2 , 3 : 3 , 21 : 0.0 , 29 : 0}, ['Brown'], 0, 1],
            'p2': [0, 1500, {5 : 0 , 18 : 0 , 39 : 0}, [], 0, 0],
            'p3': [0, 1500, {6 : 1 , 8 : 0 , 9 : 0 , 25 : 0}, ['Light Blue'], 0, 0],
            'p4': [0, 1500, {32 : 0 , 31 : 0 , 34 : 0}, ['Green'], 0, 0],
            'p5': [0, 1500, {}, [], 0, 0],
            'p6': [0, 1500, {}, [], 0, 0]}

tot_houses = 32
tot_hotels = 12
freePMon = 100
double = 0
roll_num = 0
chance_com_reroll = 0
choice = []
houses = {}


'''
database = {'Chinnywei': [9, 344, {5 : 1, 15: 1, 14: 1, 16: 0.0, 32: 0, 37: 2, 18: 0, 39: 1, 1: 0, 19: 0, 34: 0, 9: 0}, [], 0, 0],
            'Leo': [8, 414, {6: 0, 12: 1, 26: 0, 3: 0, 11: 0, 28: 1, 23: 0, 29: 0, 8: 0, 24: 0, 21: 0}, ['Red'], 0, 0]}
'''

locations = ['Go', 'Old Kent Road (B)', 'Community chest', 'Whitechapel Road (B)', 'Income Tax',
          'Kings Cross Station', 'The Angel, Islington (LB)', 'Chance', 'Euston Road (LB)', 'Pentonville Road (LB)',
          'Jail', 'Pall Mall (P)', 'Electric Company', 'Whitehall (P)', 'Northumbland Avenue (P)',
          'Marylebone Station', 'Bow Street (O)', 'Community Chest', 'Marlborough Street (O)', 'Vine Street (O)',
          'Free Parking', 'Strand (R)', 'Chance', 'Fleet Street (R)', 'Trafalgar Square (R)', 
          'Frenchurch Station','Leicester Square (Y)','Coventry Street (Y)', 'Water Works','Piccadilly (Y)',
          'Go to Jail', 'Regent Street (G)', 'Oxford Street (G)', 'Community Chest', 'Bond Street (G)',
          'Liverpool St. Station', 'Chance', 'Park Lane (DB)', 'Super tax', 'Mayfair (DB)']

chance_deck = ['go', 'jail', 'pall_mall', 'trafalgar', 'street_repairs', 'station', 'dividend', 'jail_card', 'back_3', 
               'general_repairs', 'speeding', 'school', 'drunk', 'loan_matures', 'crossword', 'mayfair']

community_chest_deck = ['bank_error', 'doctor', 'stock', 'old_kent', 'annuity', 'income', 'birthday', 'fine', 'hospital',
                        'interest', 'insurance', 'beauty', 'inherit']

property = {1 : [2, 10, 30, 90, 160, 250, [60, 50, 30]],
            3 : [4, 20, 60, 180, 320, 450, [60, 50, 30]],
            5 : [25, 50, 100, 200, 0, 0, [200, 0, 100]],
            6 : [6, 30, 90, 270, 400, 550, [100, 50, 50]],
            8 : [6, 30, 90, 270, 400, 550, [100, 50, 50]],
            9 : [8, 40, 100, 300, 450, 600, [120, 50, 60]],
            11 : [10, 50, 150, 450, 625, 750, [140, 100, 70]],
            12 : [roll_num*4, roll_num*10, 0, 0, 0, 0, [150, 0, 75]],
            13 : [10, 50, 150, 450, 625, 750, [140, 100, 70]],
            14 : [12, 60, 180, 500, 700, 900, [160, 100, 80]],
            15 : [25, 50, 100, 200, 0, 0, [200, 0, 100]],
            16 : [14, 70, 200, 550, 750, 950, [180, 100, 90]],
            18 : [14, 70, 200, 550, 750, 950, [180, 100, 90]],
            19 : [16, 80, 220, 600, 800, 1000, [200, 100, 100]],
            21 : [18, 90, 250, 700, 875, 1050, [220, 150, 110]],
            23 : [18, 90, 250, 700, 875, 1050, [220, 150, 110]],
            24 : [20, 100, 300, 750, 925, 1100, [240, 150, 120]],
            25 : [25, 50, 100, 200, 0, 0, [200, 0, 100]],
            26 : [22, 110, 330, 800, 975, 1150, [260, 150, 130]], 
            27 : [22, 110, 330, 800, 975, 1150, [260, 150, 130]], 
            28 : [roll_num*4, roll_num*10, 0, 0, 0, 0, [150, 0, 75]],
            29 : [24, 120, 360, 850, 1025, 1200, [280, 150, 140]],
            31 : [26, 130, 390, 900, 1100, 1275, [300, 200, 150]],
            32 : [26, 130, 390, 900, 1100, 1275, [300, 200, 150]],
            34 : [28, 150, 450, 1000, 1200, 1400, [320, 200, 160]],
            35 : [25, 50, 100, 200, 0, 0, [200, 0, 100]],
            37 : [35, 175, 500, 1100, 1300, 1500, [350, 200, 175]],
            39 : [50, 200, 600, 1400, 1700, 2000, [400, 200, 200]]}
        

streets = {'Brown':       [1, 3],
           'Light Blue':  [6, 8 , 9],
           'Pink':        [11, 13, 14],
           'Orange':      [16, 18, 19],
           'Red':         [21, 23, 24],
           'Yellow':      [26, 27, 29],
           'Green':       [31, 32, 34],
           'Dark Blue':   [37, 39]}

def info():
    pass

def auction(p, a):
    '''
    p- player who auctioned
    a- the property being auctioned (for going bankgrupt, ignore for normal auction)
    Auction
    '''
    
    bid = 1
    players = {key:1 for key in database if key != p}
    
    time.sleep(0.5)
    if a == '':
        print("\n\nAuction starts at £1. Type enter to pass or a number to place bet.")
    else:
        print("\n\n\n\nAuctioning off " + locations[a] + ". Auction starts at £1. Type enter to pass or a number to place bet.")
        time.sleep(0.5)
        if isinstance(database[p][2][a], float) == True:
            print("\nThis is property is mortgaged and will go to the new player as mortgaged.")
    
    while True:
        if sum(players.values()) == 1:
            for keys in players:
                if players.get(keys) == 1:
                    print("Congrats- " + keys + " wins this auction!")
                    pay(-bid, keys, "")
                    if a == '':
                        database[keys][2][database[p][0]] = 0
                    else:
                        if isinstance(database[p][2][a], float) == True:
                            database[keys][2][a] = 0.0
                        else:
                            database[keys][2][a] = 0
                        database[p][2].pop(a)
            break
        else:
            for n in players:
                time.sleep(0.5)
                if sum(players.values()) == 1:
                    break
                elif players[n] == 0:
                    pass
                else:
                    while True:
                        ans = input(n + "'s turn to place bid-   £")
                        time.sleep(0.5)
                        if ans == "":
                            print("You passed. You will not be able to participate for the rest of the auction.\n")
                            players[n] = 0
                            break
                        elif int(ans) > bid:
                            print("You have placed the highest bid so far. \n")
                            bid = int(ans)
                            break
                        elif int(ans) <= bid:
                            print("Your bid isn't high enough. Try again.")
                        else:
                            print("Your input isn't valid.")


def trading(p, a):
    pass


def mortgage(p):
    '''
    p- player
    '''
    
    print("Welcome to mortgaging.")
    time.sleep(0.5)
    print("\nProperty can be mortgaged for half it's value, however all buildings on a property must be sold before it can be mortgaged.")
    time.sleep(0.5)
    print("\nRent cannot be collect from mortgaged property. To repay mortgage, you must pay with 10% interest. \n\n")
    time.sleep(0.5)
    
    while True:
        ans = input("\nDo you want to mortgage (A), unmortgage property (B) or exit (C)?   ")
        if ans == 'A':
            owned_prop = [i for i in database[p][2] if isinstance(database[p][2][i], int) == True]
            if owned_prop == []:
                print("There are no available properties to mortgage.")
            else:
                print("\nOptions of property to mortage:")
                counter = 0
                time.sleep(0.3)
                for i in owned_prop:
                    print(string.ascii_uppercase[counter] + "- " + locations[i] + " £" +  str(property[i][6][2]))
                    counter += 1
                    time.sleep(0.3)
                while True:
                    choice = []
                    houses = {}
                    ans = input("Please list the properties you want to mortage (enter in the format A,B,C) or enter Z to cancel:   ")
                    if ans == "Z":
                        break
                    else:
                        for i in ans:
                            if i.isalpha():
                                if i in string.ascii_uppercase[0:int(len(owned_prop))]:
                                    choice.append(i)
                                else:
                                    print(i + " is an invalid input.")
                            if i.isnumeric():
                                print(i + " is an invalid input.")
                                
                        if choice == []:
                            print("You didn't enter any valid property options.")
                            time.sleep(0.5)
                        else:
                            choice = set(choice)
                            choice = [owned_prop[(ord(i.lower()) - 96) - 1] for i in choice]
                            print("Choice & money from mortgaging:" )
                            time.sleep(0.3)
                            for i in choice:
                                print(locations[i] + ": £" +  str(property[i][6][2]))
                                time.sleep(0.3)
                            while True:
                                ans = input("Finalise the mortgage (F), edit (E) or cancel (C)?   ")
                                if ans == "F": 
                                    for i in database[p][3]:
                                        if len(set(streets[i]).intersection(set(choice))) > 0:
                                            for j in streets[i]:
                                                houses[j] = database[p][2][j]
                                    for i in choice:
                                        if i not in list(houses) and i not in [5, 15, 25, 35]:
                                            houses[i] = database[p][2][i]
                                    if sum(houses.values()) != 0:
                                        print("\n" + p + " has at least 1 house on streets where you want to mortgage property:")
                                        time.sleep(0.3)
                                        for i in houses:
                                            print(locations[i] + ": " + str(houses[i]) + " house(s)")
                                            time.sleep(0.3)
                                        while True:
                                            ans = input("Sell all houses on these properties so that you can mortgage them (Y/N)?   ")
                                            if ans == "Y":
                                                tot_price = 0
                                                for i in houses:
                                                    tot_price += (houses[i] * property[i][6][1] / 2)
                                                    database[p][2][i] = 0
                                                pay(tot_price, p, '') #
                                                print("\n")
                                                break
                                            elif ans == "N":
                                                break
                                            else:
                                                print("Invalid input.")
                                    
                                    if ans != "N":
                                        tot_price = 0
                                        [tot_price := tot_price + property[i][6][2] for i in choice]
                                        print("\n")
                                        pay(tot_price, p, "")
                                        for i in choice:
                                            database[p][2][i] = 0.0
                                            if i == choice[-1]:
                                                print(locations[i], end = "")
                                            else:
                                                print(locations[i] + ", ", end = "")
                                        print(" has/ have been mortgaged.")
                                        break
                                                                  
                                elif ans == "E":
                                    break
                                elif ans == "C":
                                    break
                                else:
                                    print("Invalid input.")
                            if ans == "E":
                                pass
                            elif ans == "C":
                                break
                            else:
                                break
                    
                
        elif ans == 'B':
            owned_prop = [i for i in database[p][2] if isinstance(database[p][2][i], float) == True]
            if owned_prop == []:
                print("There are no available properties to unmortgage.")
            else:
                print("Options of property to unmortage:")
                counter = 0
                time.sleep(0.3)
                for i in owned_prop:
                    print(string.ascii_uppercase[counter] + "- " + locations[i] + + " £" +  str(property[i][6][2]*1.1))
                    counter += 1
                    time.sleep(0.3)
                while True:
                    choice = []
                    houses = {}
                    ans = input("Please list the properties you want to unmortage (enter in the format A,B,C) or enter Z to cancel:   ")
                    if ans == "Z":
                        break
                    else:
                        for i in ans:
                            if i.isalpha():
                                if i in string.ascii_uppercase[0:int(len(owned_prop))]:
                                    choice.append(i)
                                else:
                                    print(i + " is an invalid input.")
                            if i.isnumeric():
                                print(i + " is an invalid input.")
                                
                        if choice == []:
                            print("You didn't enter any valid property options.")
                            time.sleep(0.5)
                        else:
                            choice = set(choice)
                            choice = [owned_prop[(ord(i.lower()) - 96) - 1] for i in choice]
                            print("Choice & price of unmortgaging:" )
                            time.sleep(0.3)
                            for i in choice:
                                print(locations[i] + ": £" +  str(round(property[i][6][2]*1.1)))
                                time.sleep(0.3)
                            while True:
                                ans = input("Finalise the unmortgage (F), edit (E) or cancel (C)?   ")
                                if ans == "F": 
                                    tot_price = 0
                                    [tot_price := tot_price + (property[i][6][2]*1.1) for i in choice]
                                    pay(-round(tot_price), p, "")
                                    for i in choice:
                                        database[p][2][i] = 0
                                        if i == choice[-1]:
                                            print(locations[i], end = "")
                                        else:
                                            print(locations[i] + ", ", end = "")
                                    print(" has/ have been unmortgaged.")
                                    break
                                    
                                elif ans == "E":
                                    break
                                elif ans == "C":
                                    break
                                else:
                                    print("Invalid input.")
                            if ans == "E":
                                pass
                            elif ans == "C":
                                break
                            else:
                                break
                        
        elif ans == 'C':
            break
        
        else:
            print("Invalid input.")


def buy_houses():
    '''
    houses
    '''
    while True:
        global tot_houses, tot_hotels
        streets_list = list(streets.keys())
        name = input("Please enter your Monopoly name to buy/ sell houses or C to cancel:   ")
        
        if name in database:
            while True:
                ans = input("Do you want to buy (B), sell (S) houses or cancel (C)?   ")
                
                if ans == "B":
                    print("\nOptions:")
                    time.sleep(0.3)
                    for st_index in range(8):
                        print(str(st_index+1) + "- " + streets_list[st_index])
                        time.sleep(0.3)
                    print("I- more information")
                    time.sleep(0.3)
                    print("C- Cancel")
                    time.sleep(0.3)
                    
                    while True:
                        streets_house = input("\n\nChoose which street you want to buy houses/ hotels for:   ")
                        time.sleep(0.5)
                        if streets_house.isnumeric():
                            if int(streets_house) in range(1, 9):
                                st_colour = streets_list[int(streets_house )-1]
                                st_prop = streets[st_colour]
                                
                                if st_colour in database[name][3]:
                                    houses_list = {index: database[name][2][index] for index in st_prop}
                                    print("\nOptions:")
                                    time.sleep(0.3)
                                    counter = 1
                                    for prop_index in st_prop:
                                        print(str(counter) + "- " + locations[prop_index] + ": " + str(database[name][2][prop_index]) + " houses")
                                        counter += 1
                                        time.sleep(0.3)
                                    print("C- Cancel")
                                    time.sleep(1)
                                    
                                    
                                    while True:
                                        houses_list = {index: database[name][2][index] for index in st_prop}
                                        on = 0
                                        choice = []
                                        
                                        ans = input("Enter the properties you want to buy houses/ hotels for (in the format 1,2,3) or cancel (C)-   ")
                                        if ans == 'C':
                                            break
                                        for i in ans:
                                            if i.isnumeric():
                                                if on == 1:
                                                    print("You have to separate numbers with ,")
                                                    time.sleep(0.3)
                                                    choice = []
                                                    break
                                                elif on > len(st_prop):
                                                    print("Invalid input")
                                                    time.sleep(0.3)
                                                    choice = []
                                                    break
                                                on = 1
                                                choice.append(i)
                                            elif i == ",":
                                                if on == 0:
                                                    print("Invalid input")#
                                                    time.sleep(0.3)
                                                    choice = []
                                                    break
                                                on = 0
                                            elif i == " ":
                                                pass
                                            else:
                                                print("Invalid input")
                                                time.sleep(0.3)
                                                choice = []
                                                break
                                        
                                        choice = [int(st_prop[int(i)-1]) for i in choice]
                                        num_houses = 0
                                        num_hotels = 0
                                        for i in choice:
                                            houses_list[i] += 1
                                            if houses_list[i] < 5:
                                                num_houses += 1
                                            elif houses_list[i] == 5:
                                                num_hotels += 1
                                        
                                        if choice == []:
                                            pass
                                        elif num_houses > tot_houses:
                                            if tot_houses == 0:
                                                print("Sorry! All 32 houses have been bought. Please wait till there are houses available.")
                                                time.sleep(0.3)
                                            else:
                                                print("Sorry! There are only " + str(tot_houses) + " left to buy.")
                                                time.sleep(0.3)
                                        elif num_hotels > tot_hotels:
                                            if tot_hotels == 0:
                                                print("Sorry! All 12 hotels have been bought. Please wait till there are hotels available.")
                                                time.sleep(0.3)
                                            else:
                                                print("Sorry! There are only " + str(tot_hotels) + " left to buy.")
                                                time.sleep(0.3)
                                        elif all(i < 6 for i in list(houses_list.values())) == False:
                                            print("You cannot get more than 1 hotel per property! Don't be greedy! xd")
                                            time.sleep(0.3)
                                        elif max(houses_list.values()) - min(houses_list.values()) > 1:
                                            print("You cannot buy a house on this property now-", end = "")
                                            time.sleep(0.5)
                                            print(" you must have " + str(min(houses_list.values()) + 1) + " houses on each property on this street before you can get a " + str(max(houses_list.values())) + "th house on ")
                                            time.sleep(0.5)
                                            print("Currently, you own ", end = "")
                                            for i in st_prop:
                                                print(str(database[name][2][i]) + " house(s) on " + locations[i] , end = "  ")
                                            print("\n")
                                            time.sleep(1)
                                        else:
                                            print("\n")
                                            pay(-(len(choice)*property[choice[0]][6][1]), name, '')
                                            print("\nCongratulations- you now own: ")
                                            time.sleep(0.3)
                                            for i in houses_list:
                                                database[name][2][i] = houses_list[i]
                                                if database[name][2][i] == 5:
                                                    print("1 hotel on " + locations[i])
                                                else:
                                                    print(str(database[name][2][i]) + " house(s) on " + locations[i])
                                                time.sleep(0.3)
                                            time.sleep(0.7)
                                            break
                                                        
                                            
                                else:
                                    print("You don't have a completed " + st_colour + " street")
                                    time.sleep(0.5)
                                    
                            else:
                                print("Invalid input")
                                
                        elif streets_house == "I":
                            info(name)
                            pass
                            
                        elif streets_house == "C":
                            print("\n")
                            time.sleep(0.5)
                            break
                            
                        else:
                            print("Invalid input.")
                    
                    
                    
                elif ans == "S":
                    owned_prop = database[name][2]
                    sell_houses = [i for i in database[name][2] if database[name][2][i] != 0]
                    if sell_houses == []:
                        print("There are no available properties to sell houses for.")
                    else:
                        print("\nOptions:")
                        counter = 0
                        time.sleep(0.3)
                        for i in sell_houses:
                            print(string.ascii_uppercase[counter] + "- " + locations[i] + ":  " + str(owned_prop[i]) + " houses (£" + str(property[i][6][1] / 2) + " per house)")
                            counter += 1
                            time.sleep(0.3)
                        while True:
                            choice = []
                            owned_prop = database[name][2].copy()
                            sell_houses = [i for i in database[name][2] if database[name][2][i] != 0]
                            
                            ans = input("\n\nPlease list the properties you want to sell houses for (enter in the format A,B,C) or enter Z to cancel:   ")
                            if ans == "Z":
                                print("\n\n")
                                break
                            else:
                                for i in ans:
                                    if i.isalpha():
                                        if i in string.ascii_uppercase[0:int(len(sell_houses))]:
                                            choice.append(i)
                                        else:
                                            print(i + " is an invalid input.")
                                    if i.isnumeric():
                                        print(i + " is an invalid input.")
                                        
                                if choice == []:
                                    print("You didn't enter any valid property options.")
                                    time.sleep(0.5)
                                    
                                else:
                                    choice = set(choice)
                                    choice = [sell_houses[(ord(i.lower()) - 96) - 1] for i in choice]
                                    price = 0
                                    for i in choice:
                                        while True:
                                            ans = input("Enter number of houses to sell from " + locations[i] + " or pass (P)-   ")
                                            if ans.isnumeric():
                                                if int(ans) > owned_prop[i]:
                                                    print("You cannot sell " + str(ans) + " houses- you only own " + str(owned_prop[i]) + " on this property.")
                                                    time.sleep(0.5)
                                                else:
                                                    owned_prop[i] -= int(ans)
                                                    price += int(ans) * (property[i][6][1] / 2)
                                                    break
                                            elif ans == "P":
                                                break
                                            else:
                                                print("Invalid input.")
                                             
                                    fail = 0
                                    for i in choice:
                                        for colour in streets:
                                            if i in streets[colour]:
                                                streets_houses = {j: owned_prop[j] for j in streets[colour]}
                                            if max(streets_houses.values()) - min(streets_houses.values()) > 1:
                                                print("\nSell houses evenly- you must have at most " + str(max(streets_houses.values())-1) + " on every property on " + colour + " street before you can sell more houses.")
                                                time.sleep(0.5)
                                                fail = 1
                                                break
                                        if fail == 1:
                                            break
                                        
                                        
                                    if fail == 0 and price != 0:
                                        print("\n")
                                        pay(price, name, '')
                                        database[name][2] = owned_prop #FIX ISSUES WITH ACCIDENTLY STORING VALUES OF SELLIGN HOUSES WHEN IT'S NTO MEANT TO
                                        print("\nYou now own...")
                                        time.sleep(0.3)
                                        for i in choice:
                                            print(str(owned_prop[i]) + " house(s) on " + locations[i])
                                            time.sleep(0.3)
                                        time.sleep(0.7)
                                        print("\n")
                                        break
                                        
                                     
                elif ans == "C":
                    print("\n\n")
                    break
                
                else:
                    print("Invalid input")
            
        
        elif name == "C":
            print("\n\n")
            break
        
        
        else:
            print("Not a valid Monopoly name.")

        print("\n")


def pay(x, a, b):
    '''
    x- amount that needs to be transferred
    a- key to database dictionary for first player
    b- key to database dictionary for second player
    Transfers the money to/from that account (for 2 ppl interactions, use +ve value. From a to b)
    Prints value of player's account
    '''
    
    global database
    
    if x == 0:
        return
    
    print('Monies transferring  ', end = '')
    for i in range(3):
        time.sleep(0.5)
        print('$  ', end = '')
    time.sleep(0.5)
    
    if b == '':
        database[a][1] += x
        if x> 0:
            print("\n£" + str(x) + " has been transferred to your account. ", end = "" )
            time.sleep(0.5)
            print("You've now got £" + str(database[a][1]) + " in your account now.")
            time.sleep(0.5)
            print('Pogggg')
        elif x< 0:
            print("\n-£" + str(-x) + " has been transferred from your account. ", end = "")
            time.sleep(0.5)
            print("You've now got £" + str(database[a][1]) + " in your account now.")
            time.sleep(0.5)
            print('Ummmmmm... worth???')
        else:
            print('\nGlitch in the matrix')
        time.sleep(0.5)
    
    else:
        database[a][1] -= x
        database[b][1] += x
        print("\n£" + str(x) + " has been transferred from " + a + " to " + b)
        time.sleep(0.5)
        print(a + " now has £" + str(database[a][1]))
        time.sleep(0.5)
        print(b + " now has £" + str(database[b][1]))
        time.sleep(0.5)
        print('Lmao finessed.')



def bankruptcy(x, p, a, r):
    '''
    x- the value that needs to be paid
    p- player to check for bankruptcy
    a- the player that p owes money (leave '' if it's the bank')
    r- recall function (leave '' if first bankruptcy call)
    '''
    
    if x > database[p][1]:
        if r == '':
            print("You are about to go bankrupt!!!")
            time.sleep(0.5)
            print("\nThe money that you have to pay is more than what you have in your account.")
            time.sleep(0.5)
            print("\nYou have to pay £" + str(x) + " and you only have £" + str(database[p][1]))
            time.sleep(0.5)
        while True:
            ans = input("\n\nDo you want to sell houses (H), mortgage (M), trade (T) or declare bankrupcy (D)?   ")
            print("\n")
            if ans == 'H':
                buy_houses()
                bankruptcy(x, p, a, 1)
                return
            elif ans == 'M':
                mortgage(p)
                bankruptcy(x, p, a, 1)
                return
            elif ans == 'T':
                trading(p, '')
                bankruptcy(x, p, a, 1)
                return
            elif ans == 'D':
                ans = input("Are you sure? You will be permanently out of the game and cannot undo this action. (Y/N)?   ")
                if ans == 'N':
                    pass
                elif ans == 'Y':
                    price = 0
                    owned_prop = database[p][2].copy()
                    print("\nSelling all houses", end = "")
                    for i in range(3):
                        time.sleep(0.5)
                        print('.', end = '')
                    time.sleep(0.5)
                    print("\n")
                    
                    for i in owned_prop:
                        if database[p][2][i] != 0:
                            price += database[p][2][i] * property[i][6][1]
                            database[p][2][i] = 0
                    pay(price, p, '')
                    
                    if a == '':
                        for i in owned_prop:
                            auction(p, i)
                    else:
                        pay(database[p][1], p, a)
                        print("\nTransferring properties", end = "")
                        for i in range(3):
                            time.sleep(0.5)
                            if i == 2:
                                print('.')
                            else:
                                print('.', end = '')
                        time.sleep(0.5)
                        for i in owned_prop:
                            if isinstance(database[p][2][i], float) == True:
                                database[a][2][i] = 0.0
                                if i == list(database[p][2])[-1]:
                                    print(locations[i] + " (mortgaged)", end = " ")
                                else:
                                    print(locations[i] + " (mortgaged)", end = ", ")
                            else:
                                database[a][2][i] = 0
                                if i == list(database[p][2])[-1]:
                                    print(locations[i], end = " ")
                                else:
                                    print(locations[i], end = ", ")
                            database[p][2].pop(i)
                            
                        print("has/ have been transferred from " + p + " to " + a) 
                    database.pop(p)
                    time.sleep(1)
                    print("\n\n\nAight " + p + "...")
                    time.sleep(1)
                    print("\nSry to break it to u but ur kinda dog at this game.", end = " ")
                    time.sleep(1)
                    print("Better luck next time!")
                    time.sleep(1.5)
                    print("\nI appreciate u playing anyways :p")
                    break
            else:
                print("Invalid input")
                
bankruptcy(1600, 'p1', 'p2', '')