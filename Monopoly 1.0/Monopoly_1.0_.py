# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 22:24:16 2021

@author: Chin Wei Tang
"""
#%%


import time, random, string


# variables
tot_houses = 32
tot_hotels = 12
freePMon = 0
double = 0
roll_num = 0
chance_com_reroll = 0
delay = 0.3
choice = []
houses = {}


# database is a dictionary which stores the position, money, property & houses, streets, jail info (number if turns in jail), jail card of player
''''''
database = {1: [0, 1500, {}, [], 0, 0],
            2: [0, 1500, {}, [], 0, 0],
            3: [0, 1500, {}, [], 0, 0],
            4: [0, 1500, {}, [], 0, 0],
            5: [0, 1500, {}, [], 0, 0],
            6: [0, 1500, {}, [], 0, 0],
            7: [0, 1500, {}, [], 0, 0],
            8: [0, 1500, {}, [], 0, 0]}
            


# example of a real database from a past game
''' 
database = {'CHIN': [16, 556, {11: 4, 13: 4, 14: 4, 21: 0.0, 25: 1, 35: 1}, ['Pink'], 0, 0],
        'KALE': [11, 14, {6: 3, 8: 3, 9: 3, 26: 0, 27: 0, 29: 0}, ['Light Blue', 'Yellow'], 0, 0], 
        'BAGGY': [32, 704, {23: 0.0, 24: 0.0, 31: 1, 32: 1, 34: 1}, ['Green'], 0, 0], 
        'ROARLIKELEO': [13, 117, {15: 0.0, 16: 3, 18: 3, 19: 3}, ['Orange'], 0, 0], 
        'GIAN': [12, 314, {1: 5, 3: 5, 5: 0, 12: 1, 28: 1, 37: 0, 39: 0}, ['Brown', 'Dark Blue'], 0, 0]}
        '''


# dictionary that ties the associated properties with their street
streets = {'Brown':       [1, 3],
           'Light Blue':  [6, 8 , 9],
           'Pink':        [11, 13, 14],
           'Orange':      [16, 18, 19],
           'Red':         [21, 23, 24],
           'Yellow':      [26, 27, 29],
           'Green':       [31, 32, 34],
           'Dark Blue':   [37, 39]}

# list that keeps track of which properties are owned
owned_property = []

# sequential list of all the positions on the board
locations = ['Go', 'Old Kent Road (B)', 'Community chest', 'Whitechapel Road (B)', 'Income Tax',
          'Kings Cross Station', 'The Angel, Islington (LB)', 'Chance', 'Euston Road (LB)', 'Pentonville Road (LB)',
          'Jail', 'Pall Mall (P)', 'Electric Company', 'Whitehall (P)', 'Northumbland Avenue (P)',
          'Marylebone Station', 'Bow Street (O)', 'Community Chest', 'Marlborough Street (O)', 'Vine Street (O)',
          'Free Parking', 'Strand (R)', 'Chance', 'Fleet Street (R)', 'Trafalgar Square (R)', 
          'Frenchurch Station','Leicester Square (Y)','Coventry Street (Y)', 'Water Works','Piccadilly (Y)',
          'Go to Jail', 'Regent Street (G)', 'Oxford Street (G)', 'Community Chest', 'Bond Street (G)',
          'Liverpool St. Station', 'Chance', 'Park Lane (DB)', 'Super tax', 'Mayfair (DB)']



# property is dictionary which stores rent values for each property & price, cost of house and mortgage values for each property
# key is index to property in locations. First 6 values are price of rent for no house- 1 hotel, then [price of property, cost house, mortgage]
property = {1 : [2, 10, 30, 90, 160, 250, [60, 50, 30]],
            3 : [4, 20, 60, 180, 320, 450, [60, 50, 30]],
            5 : [25, 50, 100, 200, 0, 0, [200, 0, 100]],
            6 : [6, 30, 90, 270, 400, 550, [100, 50, 50]],
            8 : [6, 30, 90, 270, 400, 550, [100, 50, 50]],
            9 : [8, 40, 100, 300, 450, 600, [120, 50, 60]],
            11 : [10, 50, 150, 450, 625, 750, [140, 100, 70]],
            12 : ['4x roll num', '10x roll num', 0, 0, 0, 0, [150, 0, 75]],
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
            28 : ['4x roll num', '10x roll num', 0, 0, 0, 0, [150, 0, 75]],
            29 : [24, 120, 360, 850, 1025, 1200, [280, 150, 140]],
            31 : [26, 130, 390, 900, 1100, 1275, [300, 200, 150]],
            32 : [26, 130, 390, 900, 1100, 1275, [300, 200, 150]],
            34 : [28, 150, 450, 1000, 1200, 1400, [320, 200, 160]],
            35 : [25, 50, 100, 200, 0, 0, [200, 0, 100]],
            37 : [35, 175, 500, 1100, 1300, 1500, [350, 200, 175]],
            39 : [50, 200, 600, 1400, 1700, 2000, [400, 200, 200]]}



chance_deck = ['go', 'jail', 'pall_mall', 'trafalgar', 'street_repairs', 'station', 'dividend', 'jail_card', 'back_3', 
               'general_repairs', 'speeding', 'school', 'drunk', 'loan_matures', 'crossword', 'mayfair']

community_chest_deck = ['bank_error', 'doctor', 'stock', 'old_kent', 'annuity', 'income', 'birthday', 'fine', 'hospital',
                        'interest', 'insurance', 'beauty', 'inherit']



def auction(p, a):
    '''
    p- player who auctioned
    a- the property being auctioned (for going bankgrupt, ignore for normal auction)
    Auction
    '''
    global delay
    
    bid = 1
    players = {key:1 for key in database if key != p}
    
    time.sleep(0.5)
    
    if delay == 0:
        delay = 0.15
    
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



def bankruptcy(x, p, a, r):
    '''
    x- the value that needs to be paid
    p- player to check for bankruptcy
    a- the player that p owes money (leave '' if it's the bank')
    r- recall function (leave '' if first bankruptcy call)
    '''
    global double, roll_num, chance_com_reroll
    
    if x > database[p][1]:
        if r == '':
            print(p + " is about to go bankrupt!!!")
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
                    print("\nSelling all houses", end = "", flush=True)
                    for i in range(3):
                        time.sleep(0.5)
                        print('.', end = '', flush=True)
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
                        print("\n")
                        pay(database[p][1], p, a)
                        print("\nTransferring properties", end = "", flush=True)
                        for i in range(3):
                            time.sleep(0.5)
                            if i == 2:
                                print('.')
                            else:
                                print('.', end = '', flush=True)
                        time.sleep(0.5)
                        for i in owned_prop:
                            if isinstance(database[p][2][i], float) == True:
                                database[a][2][i] = 0.0
                                if i == list(database[p][2])[-1]:
                                    print(locations[i] + " (mortgaged)", end = " ", flush=True)
                                else:
                                    print(locations[i] + " (mortgaged)", end = ", ", flush=True)
                            else:
                                database[a][2][i] = 0
                                if i == list(database[p][2])[-1]:
                                    print(locations[i], end = " ", flush=True)
                                else:
                                    print(locations[i], end = ", ", flush=True)
                            database[p][2].pop(i)
                            
                        print("has/ have been transferred from " + p + " to " + a) 
                    double = 0
                    roll_num = 0
                    chance_com_reroll = 0
                    database.pop(p)
                    time.sleep(1)
                    print("\n\n\nAight " + p + "...")
                    time.sleep(1)
                    print("\nSry to break it to u but ur kinda dog at this game.", end = " ", flush=True)
                    time.sleep(1)
                    print("Better luck next time!")
                    time.sleep(1.5)
                    print("\nI appreciate u playing anyways :p")
                    time.sleep(1)
                    print("\n\n\n")
                    break
            else:
                print("Invalid input")



def buy_houses():
    '''
    houses
    '''
    while True:
        global tot_houses, tot_hotels, delay
        streets_list = list(streets.keys())
        name = input("Please enter your Monopoly name to buy/ sell houses or C to cancel:   ")
        
        if name in database:
            while True:
                ans = input("Do you want to buy (B), sell (S) houses or cancel (C)?   ")
                
                if ans == "B":
                    print("\nOptions:")
                    time.sleep(delay)
                    for st_index in range(8):
                        print(str(st_index+1) + "- " + streets_list[st_index])
                        time.sleep(delay)
                    print("I- more information")
                    time.sleep(delay)
                    print("C- Cancel")
                    time.sleep(delay)
                    
                    while True:
                        streets_house = input("\n\nChoose which street you want to buy houses/ hotels for:   ")
                        time.sleep(delay*2)
                        if streets_house.isnumeric():
                            if int(streets_house) in range(1, 9):
                                st_colour = streets_list[int(streets_house )-1]
                                st_prop = streets[st_colour]
                                
                                if st_colour in database[name][3]:
                                    houses_list = {index: database[name][2][index] for index in st_prop}
                                    print("\nOptions:")
                                    time.sleep(delay)
                                    counter = 1
                                    for prop_index in st_prop:
                                        print(str(counter) + "- " + locations[prop_index] + ": " + str(database[name][2][prop_index]) + " houses")
                                        counter += 1
                                        time.sleep(delay)
                                    print("C- Cancel")
                                    time.sleep(delay*3)
                                    
                                    
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
                                                    time.sleep(delay)
                                                    choice = []
                                                    break
                                                elif on > len(st_prop):
                                                    print("Invalid input")
                                                    time.sleep(delay)
                                                    choice = []
                                                    break
                                                on = 1
                                                choice.append(i)
                                            elif i == ",":
                                                if on == 0:
                                                    print("Invalid input")#
                                                    time.sleep(delay)
                                                    choice = []
                                                    break
                                                on = 0
                                            elif i == " ":
                                                pass
                                            else:
                                                print("Invalid input")
                                                time.sleep(delay)
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
                                                time.sleep(delay)
                                            else:
                                                print("Sorry! There are only " + str(tot_houses) + " left to buy.")
                                                time.sleep(delay)
                                        elif num_hotels > tot_hotels:
                                            if tot_hotels == 0:
                                                print("Sorry! All 12 hotels have been bought. Please wait till there are hotels available.")
                                                time.sleep(delay)
                                            else:
                                                print("Sorry! There are only " + str(tot_hotels) + " left to buy.")
                                                time.sleep(delay)
                                        elif all(i < 6 for i in list(houses_list.values())) == False:
                                            print("You cannot get more than 1 hotel per property! Don't be greedy! xd")
                                            time.sleep(delay)
                                        elif max(houses_list.values()) - min(houses_list.values()) > 1:
                                            print("You cannot buy a house on this property now-", end = "", flush=True)
                                            time.sleep(delay)
                                            print(" you must have " + str(min(houses_list.values()) + 1) + " houses on each property on this street before you can get a " + str(max(houses_list.values())) + "th house on ")
                                            time.sleep(delay)
                                            print("Currently, you own ", end = "", flush=True)
                                            for i in st_prop:
                                                print(str(database[name][2][i]) + " house(s) on " + locations[i] , end = "  ", flush=True)
                                            print("\n")
                                            time.sleep(delay*3)
                                        else:
                                            print("\n")
                                            pay(-(len(choice)*property[choice[0]][6][1]), name, '')
                                            print("\nCongratulations- you now own: ")
                                            time.sleep(delay)
                                            for i in houses_list:
                                                database[name][2][i] = houses_list[i]
                                                if database[name][2][i] == 5:
                                                    print("1 hotel on " + locations[i])
                                                else:
                                                    print(str(database[name][2][i]) + " house(s) on " + locations[i])
                                                time.sleep(delay)
                                            time.sleep(delay*2)
                                            break
                                                        
                                            
                                else:
                                    print("You don't have a completed " + st_colour + " street")
                                    time.sleep(delay*2)
                                    
                            else:
                                print("Invalid input")
                                
                        elif streets_house == "I":
                            info(name)
                            pass
                            
                        elif streets_house == "C":
                            print("\n")
                            time.sleep(delay*2)
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
                        time.sleep(delay)
                        for i in sell_houses:
                            print(string.ascii_uppercase[counter] + "- " + locations[i] + ":  " + str(owned_prop[i]) + " houses (£" + str(property[i][6][1] / 2) + " per house)")
                            counter += 1
                            time.sleep(delay)
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
                                    time.sleep(delay*2)
                                    
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
                                                    time.sleep(delay*2)
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
                                                    time.sleep(delay*2)
                                                    fail = 1
                                                    break
                                        if fail == 1:
                                            break
                                        
                                        
                                    if fail == 0 and price != 0:
                                        print("\n")
                                        pay(price, name, '')
                                        database[name][2] = owned_prop #FIX ISSUES WITH ACCIDENTLY STORING VALUES OF SELLIGN HOUSES WHEN IT'S NTO MEANT TO
                                        print("\nYou now own...")
                                        time.sleep(delay)
                                        for i in choice:
                                            print(str(owned_prop[i]) + " house(s) on " + locations[i])
                                            time.sleep(delay)
                                        time.sleep(delay*2)
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



def chance(p, a):
    '''
    p- player which gets the chance card
    a- chance action
    '''
    global chance_com_reroll, freePMon, delay
    
    if a == '':
        print("Drawing chance card", end = "", flush=True)
        for i in range(3):
            time.sleep(delay*2)
            print('.', end = '', flush=True)
        print("\n\n")
        time.sleep(delay*2)
        chance_deck.append(chance_deck[0])
        chance_deck.remove(chance_deck[0])
        chance(p, chance_deck[-1])
        
    
    elif a == 'go':
        database[p][0] = 0
        print("Advance to Go! (Collect $200)")
        time.sleep(delay*2)
        pay(200, p, '')
        
    elif a == 'jail':
        print("Go to Jail. (Go directly to jail)")
        database[p][0] = 10
        time.sleep(delay*2)
        jail(p)
            
    elif a == 'pall_mall':
        print("Advance to Pall Mall - If you pass Go, collect $200") # MAKE CORRECTIONS FOR REROLLING AFTER LANDING ON NEW PROP
        time.sleep(delay*2)
        chance_com_reroll = 1
        if database[p][0] <= 11:
            database[p][0] = 11
            print("You landed on... ", end = "", flush=True)
            time.sleep(delay*2)
            print(locations[database[p][0]], "!")
        elif database[p][0] > 11:
            database[p][0] = 11
            print("You land on... ", end = "", flush=True)
            time.sleep(delay*2)
            print(locations[database[p][0]], "!")
            time.sleep(delay*2)
            print("You also passed GO so $200 has been added to your account")
            pay(200, p, '')
        roll(p)
            
    elif a == 'trafalgar':
        print("Advance to Trafalgar Square – If you pass Go, collect $200")
        time.sleep(delay*2)
        chance_com_reroll = 1
        #database[p][6] = 1
        if database[p][0] <= 24:
            database[p][0] = 24
            print("You land on... ", end = "", flush=True)
            time.sleep(delay*2)
            print(locations[database[p][0]], "!")
        elif database[p][0] > 24:
            database[p][0] = 24
            print("You land on... ", end = "", flush=True)
            time.sleep(delay*2)
            print(locations[database[p][0]], "!")
            time.sleep(delay*2)
            print("You also passed GO so $200 has been added to your account")
            pay(200, p, '')
        roll(p)
        
    elif a == 'street_repairs':
        print("You are assessed for street repairs: $40 per house, $115 per hotel")
        time.sleep(delay*2)
        houses_hotels = (database[p][2][i] for i in database[p][2] if i not in [5, 15, 25, 35])
        num_houses = 0
        num_hotels = 0
        for i in houses_hotels:
            if i <5:
                num_houses += i
            elif i == 5:
                num_hotels += 1
        if num_houses + num_hotels == 0:
            print("Luckily you own 0 houses & hotels so don't have to pay anything")
        else:
            print("You own " + str(num_houses) + " houses and " + str(num_hotels) + " hotels so that's- " , end = "", flush=True)
            time.sleep(delay*2)
            print(str(num_houses) + " x £40 = £" + str(num_houses * 40) + " and " + str(num_hotels) + " x £115 = £" + str(num_hotels * 115))
            if delay == 0 and ((num_houses * 40) + (num_hotels * 115)) > 150:
                delay = 0.15
                time.sleep(2)
                print("\nSHEEEEEE " + p + " 'BOUT TO GET VIOLATED XDDDDD\n")
                time.sleep(2)
            pay(-((num_houses * 40) + (num_hotels * 115)), p, '')
            freePMon += ((num_houses * 40) + (num_hotels * 115))
        
    elif a == 'station':
        print("Take a trip to Marylebone Station- if you pass Go collect £200")
        time.sleep(delay*2)
        chance_com_reroll = 1
        if database[p][0] <= 15:
            database[p][0] = 15
            print("You land on... ", end = "", flush=True)
            time.sleep(delay*2)
            print(locations[database[p][0]], "!")
        elif database[p][0] > 15:
            database[p][0] = 15
            print("You land on... ", end = "", flush=True)
            time.sleep(delay*2)
            print(locations[database[p][0]], "!")
            time.sleep(delay*2)
            print("You also passed GO so $200 has been added to your account")
            pay(200, p, '')
        roll(p)
        
    elif a == 'dividend':
        print("Bank pays you dividend of $50")
        pay(50, p, '')
        
    elif a == 'jail_card':
        print("Get Out of Jail Free Card")
        time.sleep(delay*2)
        print("You may use it when you go to jail to get out without having to roll a double or pay.")
        database[p][5] += 1  
        
    elif a == 'back_3':
        print("You have been teleported back three spaces")
        time.sleep(delay*2)
        database[p][0] -= 3
        chance_com_reroll = 1
        roll(p)
        
    elif a == 'general_repairs':
        print("Make general repairs on all your property: $25 per house, $100 per hotel")
        time.sleep(delay*2)
        houses_hotels = (database[p][2][i] for i in database[p][2] if i not in [5, 15, 25, 35])
        num_houses = 0
        num_hotels = 0
        for i in houses_hotels:
            if i <5:
                num_houses += i
            elif i == 5:
                num_hotels += 1
        if num_houses + num_hotels == 0:
            print("Luckily you own 0 houses & hotels so don't have to pay anything")
        else:
            print("You own " + str(num_houses) + " houses and " + str(num_hotels) + " hotels so that's- " , end = "", flush=True)
            time.sleep(delay*2)
            print(str(num_houses) + " x £25 = £" + str(num_houses * 25) + " and " + str(num_hotels) + " x £100 = £" + str(num_hotels * 100))
            if delay == 0 and ((num_houses * 25) + (num_hotels * 100)) > 150:
                delay = 0.15
                time.sleep(2)
                print("\nSHEEEEEE " + p + " 'BOUT TO GET VIOLATED XDDDDD\n")
                time.sleep(2)
            pay(-((num_houses * 25) + (num_hotels * 100)), p, '')
            freePMon += ((num_houses * 25) + (num_hotels * 100))
        
    elif a == 'speeding':
        print("Speeding fine $15")
        pay(-15, p, '')
        freePMon += 15
        
    elif a == 'school':
        print("Pay school fees of $150")
        pay(-150, p, '')
        freePMon += 150
        
    elif a == 'drunk':
        print("Drunk in charge- fine $20")
        pay(-20, p, '')
        freePMon += 20
        
    elif a == 'loan_matures':
        print("Your building and loan matures — Collect $150")
        pay(150, p, '')
        
    elif a == 'crossword':
        print("You have won a crossword competition — Collect $100")
        pay(100, p, '')
        
    elif a == 'mayfair':
        print("Advance to Mayfair")
        time.sleep(delay*2)
        database[p][0] = 39
        chance_com_reroll = 1
        print("You have landed on... ", end = " ", flush=True)
        print(locations[database[p][0]], "!")
        roll(p)
        
    else:
        print ("error")
    


def community_chest(p, a):
    '''
    p- player which gets the community chest card
    a- community chest action
    '''
    global chance_com_reroll, freePMon, delay
    
    if a == '':
        print("Drawing community chest card", end = "", flush=True)
        for i in range(3):
            time.sleep(delay*2)
            print('.', end = '', flush=True)
        print("\n\n")
        time.sleep(delay*2)
        community_chest_deck.append(community_chest_deck[0])
        community_chest_deck.remove(community_chest_deck[0])
        community_chest(p, community_chest_deck[-1])
       
    elif a == 'bank_error':
        print("Bank error in your favor — Collect $200")
        pay(200, p, '')
    
    elif a =='doctor':
        print("Doctor's fee — Pay $50")
        pay(-50, p, '')
        freePMon += 50
        
    elif a == 'stock':
        print("From sale of stock you get $50")
        pay(50, p, '')
        
    elif a == 'old_kent':
        print("Go back to Old Kent Road")
        database[p][0] = 1
        chance_com_reroll = 1
        #database[p][6] = 1
        print("You land on... ", end = "", flush=True)
        time.sleep(delay*2)
        print(locations[database[p][0]], "!")
        roll(p)
        
    elif a == 'annuity':
        print("Annuity matures. Collect $100")
        pay(100, p, '')
        
    elif a == 'income':
        print("Income tax refund – Collect $20")
        pay(20, p, '')
        
    elif a == 'birthday':
        print("It is your birthday — Collect $10 from each player")
        tot_paid = 0
        for i in database:
            if i == p:
                pass
            else:
                database[i][1] -= 10
                tot_paid += 10
        time.sleep(delay*2)
        print(p + " gets £" + str(tot_paid) + " from everyone else.")
        pay(tot_paid, p, '')
        print("\n£10 has been deducted from everyone else's account: ")
        time.sleep(delay*2)
        for i in database:
            if i == p:
                pass
            else:
                print(i + " now has £" + str(database[i][1]))
        
    elif a == 'fine':
        while True:
            ans = input ("Pay a $10 fine (F) or take a Chance (C)-   ")
            if ans == 'F':
                pay(-10, p, '')
                freePMon += 10
                break
            elif ans == 'C':
                chance(p, '')
                break
            else:
                print("Invalid input.")
            
    elif a == 'hospital':
        print("Pay hospital fees of $100")
        pay(-100, p, '')
        freePMon += 100
        
    elif a == 'interest':
        print("Receive interest on 7% preference shares: $25")
        pay(25, p, '')
        
    elif a == 'insurance':
        print("Pay your insurance premium $50")
        pay(-50, p, '')
        freePMon += 50
        
    elif a == 'beauty':
        print("You have won second prize in a beauty contest – Collect $10")
        pay(10, p, '')
        
    elif a == 'inherit':
        print("You inherit $100")
        pay(100, p, '')



def info(a):
    '''
    a- key to database dictionary for player
    Gives option to look at bank account and property owned
    '''
    global delay
    
    time.sleep(delay)
    print("\nOptions:")
    time.sleep(delay)
    print("A- everyone's balance")
    time.sleep(delay)
    print("B- everyone's owned property")
    time.sleep(delay)
    print("C- rent data & prices for all properties")
    time.sleep(delay)
    print("D- back")
    time.sleep(delay)
    
    while True:
        ans = input("Choice:   ")
        time.sleep(delay*2)
        if ans == 'A':
            for player in database:
                time.sleep(delay)
                print(player + " has £" + str(database[player][1]))
            time.sleep(delay*2)
            
        elif ans == 'B':
            for player in database:
                time.sleep(delay)
                print('\n' + player + " owns:")
                if database[player][2] == {}:
                    print("No property.")
                else:
                    for i in database[player][2]:
                        if database[player][2][i] == 5:
                            print(locations[i] + " - 1 hotel  ,  ", end = "", flush=True)
                        else:
                            print(locations[i] + " - " + str(database[player][2][i]) + " house(s),  ", end = "", flush=True)
                    if database[player][3] == []:
                        print("and no streets.")
                    else:
                        print("and the ", end = "", flush=True)
                        for i in database[player][3]:
                            print(i, end = "", flush=True)
                        print(" street(s).")
            time.sleep(delay*3)
            
            
        elif ans == 'C':
            print("\nFormat- [rent for 0 houses, 1, 2, 3, 4, 1 hotel, [price of property, cost of house, mortgage]]")
            time.sleep(delay*7)
            for i in property:
                print("\n" + str(locations[i]) + "\n" + str(property[i]))
                time.sleep(delay)
            time.sleep(delay*2)
            
        elif ans == 'D':
            break
        
        else:
            print("Last time I checked, " + ans + " wasn't A, B, C or D.")
            time.sleep(delay*2)
            
        print("\n")


def intro():
    print("\n\n\n")
    intro = "WELCOME TO MONOPOLY!"
    for i in intro:
        print(i, end ="", flush=True)
        time.sleep(0.2)
        
    print("\n\nThis game has a maximum of 8 players.")
    time.sleep(0.5)
    print("\nPlease enter your ingame name (press enter when all players are registered):")
    time.sleep(0.5)
    for i in range(8):
        ans = input("Player " + str(i+1) + ":   ")
        if ans == "":
            for j in range(i,8):
                database.pop(j+1)
            break
        else:
            database[ans] = database.pop(i+1)
    print("\n\n")



def mortgage(p):
    '''
    p- player
    '''
    global delay
    
    print("Welcome to mortgaging.")
    time.sleep(delay*2)
    print("\nProperty can be mortgaged for half it's value, however all buildings on a property must be sold before it can be mortgaged.")
    time.sleep(delay*2)
    print("\nRent cannot be collect from mortgaged property. To repay mortgage, you must pay with 10% interest. \n\n")
    time.sleep(delay*2)
    
    while True:
        ans = input("\nDo you want to mortgage (A), unmortgage property (B) or exit (C)?   ")
        print("\n")
        if ans == 'A':
            owned_prop = [i for i in database[p][2] if isinstance(database[p][2][i], int) == True]
            if owned_prop == []:
                print("There are no available properties to mortgage.")
            else:
                print("\nOptions of property to mortage:")
                counter = 0
                time.sleep(delay)
                for i in owned_prop:
                    print(string.ascii_uppercase[counter] + "- " + locations[i] + " £" +  str(property[i][6][2]))
                    counter += 1
                    time.sleep(delay)
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
                            time.sleep(delay*2)
                        else:
                            choice = set(choice)
                            choice = [owned_prop[(ord(i.lower()) - 96) - 1] for i in choice]
                            print("\nChoice & money from mortgaging:" )
                            time.sleep(delay)
                            for i in choice:
                                print(locations[i] + ": £" +  str(property[i][6][2]))
                                time.sleep(delay)
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
                                        time.sleep(delay)
                                        for i in houses:
                                            print(locations[i] + ": " + str(houses[i]) + " house(s)")
                                            time.sleep(delay)
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
                                        pay(tot_price, p, "")
                                        print("\n")
                                        for i in choice:
                                            database[p][2][i] = 0.0
                                            if i == choice[-1]:
                                                print(locations[i], end = "", flush=True)
                                            else:
                                                print(locations[i] + ", ", end = "", flush=True)
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
                time.sleep(delay)
                for i in owned_prop:
                    print(string.ascii_uppercase[counter] + "- " + locations[i] + + " £" +  str(property[i][6][2]*1.1))
                    counter += 1
                    time.sleep(delay)
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
                            time.sleep(delay*2)
                        else:
                            choice = set(choice)
                            choice = [owned_prop[(ord(i.lower()) - 96) - 1] for i in choice]
                            print("Choice & price of unmortgaging:" )
                            time.sleep(delay)
                            for i in choice:
                                print(locations[i] + ": £" +  str(round(property[i][6][2]*1.1)))
                                time.sleep(delay)
                            while True:
                                ans = input("Finalise the unmortgage (F), edit (E) or cancel (C)?   ")
                                if ans == "F": 
                                    tot_price = 0
                                    [tot_price := tot_price + (property[i][6][2]*1.1) for i in choice]
                                    pay(-round(tot_price), p, "")
                                    for i in choice:
                                        database[p][2][i] = 0
                                        if i == choice[-1]:
                                            print(locations[i], end = "", flush=True)
                                        else:
                                            print(locations[i] + ", ", end = "", flush=True)
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
            
            
            
def jail(a):
    '''
    a- player sent to jail
    '''
    global roll_num, delay
    
    if database[a][4] == 0:
        print("\n\nWelcome to jail.")
        time.sleep(delay*2)
        print("To get out, you may choose to either pay £50 or try to roll a double to get out of jail.")
        time.sleep(delay*2)
        print("On the third missed turn, if you don't roll a double, you have to pay £50 to get out.")
        time.sleep(delay*2)
        database[a][4] += 1
        return
    
    if database[a][4] == 1:
        turn = "First"
    elif database[a][4] == 2:
        turn = "Second"
    elif database[a][4] == 3:
        turn = "Third"
    
    
    while True:
        if database[a][5] != 0:
            jail_choice = input(turn + " turn in jail - roll double (A), pay £50 (B) or use Get Out Of Jail Free Card (C)?   ")
        else:
            jail_choice = input(turn + " turn in jail - roll double (A) or pay £50 (B)?   ")
        if jail_choice == "A":
            print("You roll", end = '', flush=True)
            for i in range(3):
                time.sleep(delay*2)
                print('.', end = '', flush=True)
            time.sleep(delay*2)
            roll_1 = random.randint(1, 6)
            roll_2 = random.randint(1, 6)
            print(" ", roll_1, end = "", flush=True)
            time.sleep(delay*2)
            print(" and ", end = "", flush=True)
            time.sleep(delay*2)
            print(roll_2)
            time.sleep(delay*3)
            
            if roll_1 == roll_2:
                print("You rolled a double!!! You are now free.")
                database[a][4] = 0
                roll_num = roll_1 + roll_2
                time.sleep(delay*3)
            else:
                if database[a][4] == 3:
                    print("This is your third turn in jail and you didn't roll a double. To get out you have to pay £50.\n")
                    pay(-50, a, "")
                    database[a][4] = 0
                else:
                    print("Unlucky- you're still stuck in jail.")
                    database[a][4] += 1
            break
            
        elif jail_choice == "B":
            print("Paying your way out of jail huh? ^^")
            time.sleep(delay*2)
            pay(-50, a, "")
            database[a][4] = 0
            break
            
        elif jail_choice == "C" and database[a][5] != 0:
            print("Lucky guy...")
            time.sleep(delay*2)
            database[a][4] = 0
            database[a][5] -= 1
            break
        
        else:
            print("Invalid input.")
            time.sleep(delay*2)
        
        
    if database[a][4] == 0:
        print("\nWe hope you enjoyed your stay. ", end = "", flush=True)
        time.sleep(delay*2)
        print("pls consider leaving a 5 star review on Trip Advisor ", end = "", flush=True)
        time.sleep(delay*3)
        print(":)\n\n")
        time.sleep(delay*2)
        roll(a)
    
    
     
def pay(x, a, b):
    '''
    x- amount that needs to be transferred
    a- key to database dictionary for first player
    b- key to database dictionary for second player
    Transfers the money to/from that account (for 2 ppl interactions, use +ve value. From a to b)
    Prints value of player's account
    '''
    
    global database, delay 
    
    if (database[a][1] < 150 or abs(x) >= 150) and delay == 0:
        delay = 0.15
    
    if x < 0 and b == '':
        bankruptcy(-x, a, b, '')
    if x > 0 and b != '':
        bankruptcy(x, a, b, '')
    
    if x == 0 or a not in database:
        return
    
    print('Monies transferring  ', end = '', flush=True)
    for i in range(3):
        time.sleep(delay*2)
        print('$  ', end = '', flush=True)
    time.sleep(delay*2)
    
    if b == '':
        database[a][1] += x
        if x> 0:
            print("\n£" + str(x) + " has been transferred to your account. ", end = "", flush=True )
            time.sleep(delay*2)
            print("You've now got £" + str(database[a][1]) + " in your account now.")
            time.sleep(delay*2)
            print('Pogggg')
        elif x< 0:
            print("\n-£" + str(-x) + " has been transferred from your account. ", end = "", flush=True)
            time.sleep(delay*2)
            print("You've now got £" + str(database[a][1]) + " in your account now.")
            time.sleep(delay*2)
            print('Ummmmmm... worth???')
        else:
            print('\nGlitch in the matrix')
        time.sleep(delay*2)
    
    else:
        database[a][1] -= x
        database[b][1] += x
        print("\n£" + str(x) + " has been transferred from " + a + " to " + b)
        time.sleep(delay*2)
        print(a + " now has £" + str(database[a][1]))
        time.sleep(delay*2)
        print(b + " now has £" + str(database[b][1]))
        time.sleep(delay*2)
        print('Lmao finessed.')
        
    
    if delay == 0.15:
        while True:
            ans = input("Press ENTER to continue with TURBO on or X to exit TURBO   ")
            if ans == "":
                delay = 0
                break
            elif ans == "X":
                delay = 0.3
                print('Turning off TURBO', end = '', flush=True)
                for i in range(3):
                    time.sleep(0.5)
                    print('.', end = '', flush=True)
                time.sleep(0.5)
                print("\n\n\n\n")
                break
            else:
                print("Invalid input")
        
            
def rent(x, a):
    '''
    x- the index of the property
    a- the player that landed on the property
    '''
    global delay
    
    for player in database:
        if x in database[player][2]:
            number_houses = database[player][2][x]
            print ("You landed on " + player + "'s property- ", end = "", flush=True)
            time.sleep(delay*2)
            if isinstance(number_houses, float) == True:
                print("Noice. This property has been mortgaged so you don't have to pay rent.")
                return
            else:
                if x in [12, 28]:
                    if number_houses == 0:
                        print(player + " owns 1 utility ", end = "", flush=True)
                        print("and the rent costs £" + str(roll_num*4) + ".\n")
                        pay(roll_num*4, a, player)
                        return
                    elif number_houses == 1:
                        print(player + " owns 2 utilities ", end = "", flush=True)
                        print("and the rent costs £" + str(roll_num*10) + ".\n")
                        pay(roll_num*10, a, player)
                        return
                    time.sleep(delay*2)
                elif x in [5, 15, 25, 35]:
                    print(player + " owns " + str(database[player][2][x] + 1) + " station(s) ", end = "", flush=True)
                    time.sleep(delay*2)
                else:
                    print("this property has " + str(number_houses) + " house(s) ", end = "", flush=True)
                    time.sleep(delay*2)
                    
                if database[player][3] != []:
                    street_counter = 0
                    for owned_street in database[player][3]:
                        if x in streets[owned_street] and number_houses == 0:
                            print("and " + player + " owns " + owned_street +  " street so rent is doubled. Rent costs £" + str(property[x][number_houses]*2) + ".\n")
                            pay(property[x][number_houses]*2, a, player)
                            street_counter = 1
                            break
                        
                    if street_counter == 0:
                        if property[x][number_houses] >= 150 and delay == 0:
                            delay = 0.15
                            time.sleep(2)
                            print("\n\nSHEEEEEE " + a + " 'BOUT TO GET VIOLATED FRRRRRR\n")
                            time.sleep(2)
                        print("and the rent costs £" + str(property[x][number_houses]) + ".\n")
                        
                        pay(property[x][number_houses], a, player)
                        break
                            
                elif database[player][3] == []:
                    print("and the rent costs £" + str(property[x][number_houses]) + ".\n")
                    pay(property[x][number_houses], a, player)
    
    
    
def roll(p):
    '''
    p- player
    Executes one turn on the board.
    '''
    
    while True:
        global database, double, roll_num, chance_com_reroll, freePMon, delay
        
        if database[p][4] != 0:
            jail(p)
            break
        
        if database[p][4] == 0:
            if chance_com_reroll == 1:
                pass
            else:
                if int(roll_num) != 0:
                    pass
                else:
                    print('You start on ' + locations[database[p][0]], end = ' ')
                    print("and roll", end = '', flush=True)
                    for i in range(3):
                        time.sleep(delay*2)
                        print('.', end = '', flush=True)
                    time.sleep(delay*2)
                    roll_1 = random.randint(1, 6)
                    roll_2 = random.randint(1, 6)
                    roll_num  = roll_1 + roll_2
                    print(" ", roll_1, end = "", flush=True)
                    time.sleep(delay*2)
                    print(" and ", end = "", flush=True)
                    time.sleep(delay*2)
                    print(roll_2)
                    time.sleep(delay*2)
                    
                    if roll_1 == roll_2:
                        double += 1
                        if double == 3:
                            print("You rolled 3 doubles! Go to jail! ")
                            database[p][0] = 10
                            double = 0
                            roll_num = 0
                            chance_com_reroll = 0
                            jail(p)
                            break
                        else:
                            print("That's a double!")
                        time.sleep(delay*2)
                    else:
                        double =0
            
                    
                print("You advance", roll_num, "spaces", end = '', flush=True)
                time.sleep(delay*2)
                
                
                if database[p][0] + int(roll_num)> 39:
                    if database[p][0] + int(roll_num) == 40:
                        database[p][0] = (database[p][0] + roll_num) % 40
                        print(' and land on ' + locations[database[p][0]] + '!')
                        time.sleep(delay*3)
                    else:
                        print (", pass Go", end = "", flush=True )
                        database[p][0] = (database[p][0] + roll_num) % 40
                        print(' and land on ' + locations[database[p][0]] + '!')
                        time.sleep(delay*2)
                        print("\nCollect £200 for passing Go.")
                        time.sleep(delay*3)
                        pay(200, p, '')
                
                else:
                    database[p][0] = (database[p][0] + roll_num) % 40
                    print(' and land on ' + locations[database[p][0]] + '!')
                    time.sleep(delay*3)
                    
    
            if database[p][0] in database[p][2]:
                print('You already own this property')
                
            elif database[p][0] in owned_property:
                print("\nUnlucky buddy- you landed on someone else's property.")
                time.sleep(delay*3)
                rent(database[p][0], p)
                
            elif database[p][0] in [0, 2, 4, 7, 10, 17, 20, 22, 30, 33, 36, 38]:
                #print('\n')
                if database[p][0] == 2 or database[p][0] == 17 or database[p][0] == 33:
                    community_chest(p, '')
                elif database[p][0] == 7 or database[p][0] == 22 or database[p][0] == 36:
                    chance(p, '')
                elif database[p][0] == 0:
                    print('\nNoice. Landed on Go.')
                    time.sleep(delay*3)
                    pay(+200, p, '')
                elif database[p][0] == 4:
                    print('\nTake the L lel. Income tax- pay £200.')
                    time.sleep(delay*3)
                    pay(-200, p, '')
                    freePMon += 200
                elif database[p][0] == 10:
                    print ('\nJust visiting jail')
                elif database[p][0] == 20:
                    print ('\nNoice. Landed on free parking.')
                    if freePMon > 200 and delay == 0:
                        time.sleep(1.5)
                        print("\nSHEEEEEE " + p + " 'BOUT TO GET NICED FR\n")
                    pay(+freePMon, p, '')
                    freePMon = 0
                elif database[p][0] == 30:
                    database[p][0] = 10
                    double = 0
                    jail(p)
                elif database[p][0] == 38:
                    print ('\nHaha sucker! Super tax- £100')
                    pay(-100, p, '')
                    freePMon += 100
                else:
                    print('\nGlitch in the matrix')
                    time.sleep(delay*2)
                    
            else:
                while True:
                    decision = input("This property costs £" + str(property[database[p][0]][6][0]) + '. You have £' + str(database[p][1]) + ' in your account. Buy or auction? (Type B/A) \n')
                    if delay == 0:
                        delay = 0.15
                    if decision == 'B':
                        pay(-property[database[p][0]][6][0], p, '')
                        database[p][2][database[p][0]] = 0
                        print ('\nCongratulations! You now own ' + locations[database[p][0]])
                        time.sleep(delay*2)
                        break
                    elif decision == 'A':
                        auction(p, '')
                        break
                    else:
                        print ("\nYou didn't type B/A")
                    time.sleep(delay*2)
            
    
            if double == 0:
                roll_num = 0
                chance_com_reroll = 0
                break
            elif double == 1 or double ==2:
                roll_num = 0
                chance_com_reroll = 0
                
                if delay == 0.15:
                    while True:
                        ans = input("Press ENTER to continue with TURBO on or X to exit TURBO   ")
                        if ans == "":
                            delay = 0
                            break
                        elif ans == "X":
                            delay = 0.3
                            print('Turning off TURBO', end = '', flush=True)
                            for i in range(3):
                                time.sleep(0.5)
                                print('.', end = '', flush=True)
                            time.sleep(0.5)
                            print("\n\n\n\n")
                            break
                        else:
                            print("Invalid input")
                
                ans = input("\nPress enter to roll again. ")
                if ans == "":
                    pass
            else:
                print ("error & double = " + str(double))
    
       


def shuffle():
    '''
    Shuffles chance and community decks
    '''
    while True:
        time.sleep(0.5)
        decision = str(input("Would you like to shuffle the chance and community chest cards? (Y/N)   "))
        if  decision == "Y":
            time.sleep(0.5)
            print("Shuffling", end = "", flush=True)
            time.sleep(0.5)
            for i in range(3):
                print(".", end = "", flush=True)
                time.sleep(0.5)
            random.shuffle(community_chest_deck)    
            random.shuffle(chance_deck)
            print("\nYour cards have been shuffled... by Krammer.", end = "", flush=True)
            time.sleep(0.5)
            print(" Don't be surprised if he wins.")
            return chance_deck, community_chest_deck
            #return community_chest_deck
        elif decision == "N":
            time.sleep(0.5)
            print("Why u tryna cheat??? Sus. Fined £200 for cheating.", end ="", flush=True)
            time.sleep(1)
            print("jk ;)")
        else:
            time.sleep(0.5)
            print("Why you chatting WASS my G")



def street(a):
    '''
    a- player to check for street
    '''
    new_owned_streets = []
    stations_list = []
    property_list = [i for i in database[a][2] if isinstance(database[a][2][i], float) == False]
    #c = list(database[a][2].keys())
    
    for street in streets:
        prop_of_streets = streets[street]
        if all(item in property_list for item in prop_of_streets):
            new_owned_streets.append(street)
        else:
            pass
        
    if new_owned_streets != database[a][3]:
        if len(new_owned_streets) > len(database[a][3]):
            print ("Congratulations " + a + "! You now have completed the ", end = "", flush=True)
            for i in list(set(new_owned_streets) - set(database[a][3])):
                if i == list(set(new_owned_streets) - set(database[a][3]))[-1]:
                    print(i, end = "", flush=True)
                else:
                    print(i, end = " and ", flush=True)
            print(" street(s)", end = "- ", flush=True)
            time.sleep(delay*2)
            print("you may now purchase houses for this street(s).\n")
            time.sleep(delay*3)
            database[a][3] = new_owned_streets
        elif len(new_owned_streets) < len(database[a][3]):
            print("Unfortunately " + a + " you no longer own (a) completed, unmortgaged ", end = "", flush=True)
            for i in list(set(database[a][3]) - set(new_owned_streets)):
                if i == list(set(database[a][3]) - set(new_owned_streets))[-1]:
                    print(i, end = "", flush=True)
                else:
                    print(i, end = " and ", flush=True)
            print(" street(s)", end = "- ", flush=True)
            time.sleep(delay*2)
            print("you cannot buy houses for this street(s) any more.\n")
            time.sleep(delay*3)
            database[a][3] = new_owned_streets
    
    if all(item in property_list for item in [12, 28]):
        if database[a][2][12] != 1:
            database[a][2][12] = 1
            database[a][2][28] = 1
            print("Congratulations " + a + "! You now have 2 utilities", end = "- " , flush=True)
            time.sleep(delay*2)
            print(" now when people land on your utilities, rent is 10x the dice roll.\n")
            time.sleep(delay*5)
    elif 12 in property_list:
        if database[a][2][12] == 2:
            database[a][2][12] = 1
            print(a + " only has 1 utility now- rent is 4x dice roll \n")
            time.sleep(delay*2)
    elif 14 in property_list:
        if database[a][2][14] == 2:
            database[a][2][14] = 1
            print(a + " only has 1 utility now- rent is 4x dice roll \n")
            time.sleep(delay*2)
    
    
    counter = 0
    for station in [5, 15, 25, 35]:
        if station in property_list:
            counter += 1
            stations_list.append(station)
    if stations_list != []:
        if (counter-1) != database[a][2][stations_list[0]]:
            if (counter-1) > database[a][2][stations_list[0]]:
                print("Congratulations " + a + "! You now own " + str(counter) + " stations.\n")
                time.sleep(delay*2)
            elif (counter-1) < database[a][2][stations_list[0]]:
                print(a + " now has only got " + str(counter) + " rentable stations.\n")
                time.sleep(delay*2)
            for station in stations_list:
                database[a][2][station] = (counter-1)
            
    
    player_prop = {i : database[a][2][i] for i in sorted(list(database[a][2].keys()))}
    database[a][2] = player_prop
    
    print("\n")



def trading(p, a):
    '''
    p- player
    a- action to recall function 
    '''
    #global houses, choice
        
    if a == '':
        print("\nWelcome to trading. ")
        time.sleep(delay*2)
        print("\nYou may only trade undeveloped property- ", end = "", flush=True)
        time.sleep(delay*2)
        print("you must sell off all buildings from a street before you can trade property from that street.")
        time.sleep(delay*2)
        print("\nBuilding are sold at half the value. ")
        time.sleep(delay*2)
    
    trade = {'money1': 0,
             'prop1' : [],
             'money2': 0,
             'prop2' : []}
    choice = []
    houses = {}
    no_sell = 0
    
    while True:
        player2 = input("\n" + p + ", enter the Monopoly name of the player who you are trading with or stop trading (C):   ")
        
        if player2 in database:
            while True:
                if trade['money1'] != 0 or trade['prop1'] != [] or trade['money2'] != 0 or trade['prop2'] != []:
                    print("\n\n\nCurrently the trade is:")
                    time.sleep(delay)
                    print(p + ": £" + str(trade['money1']) + " & ", end = "", flush=True)
                    print( [locations[i] for i in trade['prop1']] )
                    time.sleep(delay)
                    print(player2 + ": £" + str(trade['money2']) + " & ", end = "", flush=True)
                    print( [locations[i] for i in trade['prop2']] )
                    time.sleep(delay)
                    
                    while True:
                        ans = input("Finalise the trade (F), edit the trade (E) or cancel the trade (C)?   ")
                        if ans == 'F':
                            if trade['money1'] == trade['money2']:  # SELL ALL HOUSES BEFORE TRANSFERRING MONEY
                                print("\n\nNo money is transferred in this trade.")
                                time.sleep(delay*2)
                                pass
                            elif trade['money1'] > trade['money2']:
                                print("\n\n")
                                amount = int(trade['money1']) - int(trade['money2'])
                                pay(amount, p, player2)
                            elif trade['money2'] > trade['money1']:
                                print("\n\n")
                                amount = int(trade['money2']) - int(trade['money1'])
                                pay(amount, player2, p)
                           
                                
                            if trade['prop1'] == []:
                                pass
                            else:
                                for i in database[p][3]:
                                    if len(set(streets[i]).intersection(set(trade['prop1']))) > 0:
                                        for j in streets[i]:
                                            houses[j] = database[p][2][j]
                                for i in trade['prop1']:
                                    if i not in list(houses) and i not in [5, 15, 25, 35]:
                                        houses[i] = database[p][2][i]
                                if sum(houses.values()) != 0:
                                    print("\n\n\n" + p + " has at least 1 house on streets where you want to trade property:")
                                    time.sleep(delay)
                                    for i in houses:
                                        print(locations[i] + ": " + str(houses[i]) + " house(s)")
                                        time.sleep(delay)
                                    while True:
                                        ans = input("Sell all houses on these properties so that you can trade them (Y/N)?   ")
                                        if ans == "Y":
                                            tot_price = 0
                                            for i in houses:
                                                tot_price += (houses[i] * property[i][6][1] / 2)
                                                database[p][2][i] = 0
                                            pay(tot_price, p, '')
                                            for i in trade['prop1']:
                                                if isinstance(database[p][2][i], float) == True:
                                                    database[player2][2][i] = 0.0
                                                else:
                                                    database[player2][2][i] = 0
                                                database[p][2].pop(i)
                                            print("\n")
                                            for i in trade['prop1']:
                                                if i == trade['prop1'][-1]:
                                                    print(locations[i], end = " ", flush=True)
                                                else:
                                                    print(locations[i], end = ", ", flush=True)
                                            print("has/ have been transferred from " + p + " to " + player2) 
                                            time.sleep(delay*2)
                                            no_sell = 0
                                            break
                                        elif ans == "N":
                                            no_sell = 1
                                            break
                                        else:
                                            print("Invalid input")
                                elif sum(houses.values()) == 0:
                                    for i in trade['prop1']:
                                        if isinstance(database[p][2][i], float) == True:
                                            database[player2][2][i] = 0.0
                                        else:
                                            database[player2][2][i] = 0
                                        database[p][2].pop(i)
                                    print("\n")
                                    for i in trade['prop1']:
                                        if i == trade['prop1'][-1]:
                                            print(locations[i], end = " ", flush=True)
                                        else:
                                            print(locations[i], end = ", ", flush=True)
                                    print("has/ have been transferred from " + p + " to " + player2) 
                                    time.sleep(delay*2)
                                    no_sell = 0
                                
                            houses = {}
                                        
                                        
                                
                            if trade['prop2'] == [] or no_sell == 1:
                                pass
                            else:
                                for i in database[player2][3]:
                                    if len(set(streets[i]).intersection(set(trade['prop2']))) > 0:
                                        for j in streets[i]:
                                            houses[j] = database[player2][2][j]
                                for i in trade['prop2']:
                                    if i not in list(houses) and i not in [5, 15, 25, 35]:
                                        houses[i] = database[player2][2][i]
                                if sum(houses.values()) != 0:
                                    print("\n\n\n" + player2 + " has at least 1 house on streets where you want to trade property:")
                                    time.sleep(delay)
                                    for i in houses:
                                        print(locations[i] + ": " + str(houses[i]) + " house(s)")
                                        time.sleep(delay)
                                    while True:
                                        ans = input("Sell all houses on these properties so that you can trade them (Y/N)?   ")
                                        if ans == "Y":
                                            tot_price = 0
                                            for i in houses:
                                                tot_price += (houses[i] * property[i][6][1] / 2)
                                                database[player2][2][i] = 0
                                            pay(tot_price, player2, '')
                                            for i in trade['prop2']:
                                                if isinstance(database[player2][2][i], float) == True:
                                                    database[p][2][i] = 0.0
                                                else:
                                                    database[p][2][i] = 0
                                                database[player2][2].pop(i)
                                            print("\n")
                                            for i in trade['prop2']:
                                                if i == trade['prop1'][-1]:
                                                    print(locations[i], end = " ", flush=True)
                                                else:
                                                    print(locations[i], end = ", ", flush=True)
                                            print("has/ have been transferred from " + player2 + " to " + p)
                                            time.sleep(delay*2)
                                            no_sell = 0
                                            break
                                        elif ans == "N":
                                            no_sell = 1
                                            break
                                        else:
                                            print("Invalid input")
                                elif sum(houses.values()) == 0:
                                    for i in trade['prop2']:
                                        if isinstance(database[player2][2][i], float) == True:
                                            database[p][2][i] = 0.0
                                        else:
                                            database[p][2][i] = 0
                                        database[player2][2].pop(i)
                                    print("\n")
                                    for i in trade['prop2']:
                                        if i == trade['prop2'][-1]:
                                            print(locations[i], end = " ", flush=True)
                                        else:
                                            print(locations[i], end = ", ", flush=True)
                                    print("has/ have been transferred from " + player2 + " to " + p) 
                                    time.sleep(delay*2)
                                    no_sell = 0
                            houses = {}
                            
                            
                            if no_sell == 1:
                                pass
                            else:
                                print("\n\nTrade has been completed!\n\n")
                                time.sleep(delay*2)
                                street(p)
                                street(player2)
                                trading(p, 1)
                                return
                             
                        elif ans == 'E':
                            time.sleep(delay*2)
                            break
                        
                        elif ans == 'C':
                            print("Cancelling", end = "", flush=True)
                            for i in range(3):
                                time.sleep(delay*2)
                                print('.', end = '', flush=True)
                            time.sleep(delay*2)
                            print("\n\n")
                            trading(p, 1) 
                            return
                        else:
                            print("Invalid input.")
                
                print("\n\n\n" + p + "'s part of the trade: ")
                while True:
                    time.sleep(delay)
                    ans = input("Money: ")
                    if ans.isnumeric():
                        if int(ans) < 0:
                            print("Invalid input")
                        trade['money1'] = ans
                        break
                    else:
                        print("Invalid input")
                while True:
                    counter = 0
                    owned_prop = list(database[p][2].keys())
                    #choice = []
                    print("\nOptions of property to trade: ")
                    time.sleep(delay)
                    for i in owned_prop:
                        print(string.ascii_uppercase[counter] + "- " + locations[i])
                        counter += 1
                        time.sleep(delay)
                    while True:
                        ans = input("Please list the properties you want to trade (enter in the format A,B,C) or enter Z to pass:   ")
                        if ans == 'Z':
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
                                time.sleep(delay*2)
                                
                            else:
                                #houses = {}
                                choice = set(choice)
                                choice = [owned_prop[(ord(i.lower()) - 96) - 1] for i in choice]
                                trade['prop1'] = choice
                                break
                    break
                            
                print("\n\n\n" + player2 + "'s part of the trade: ")
                while True:
                    time.sleep(delay*3)
                    ans = input("Money: ")
                    if ans.isnumeric():
                        if int(ans) < 0:
                            print("Invalid input")
                        trade['money2'] = ans
                        break
                    else:
                        print("Invalid input")
                while True:
                    counter = 0
                    owned_prop = list(database[player2][2].keys())
                    choice = []
                    print("\nOptions of property to trade: ")
                    time.sleep(delay)
                    for i in owned_prop:
                        print(string.ascii_uppercase[counter] + "- " + locations[i])
                        counter += 1
                        time.sleep(delay)
                    while True:
                        ans = input("Please list the properties you want to trade (enter in the format A,B,C) or enter Z to pass:   ")
                        if ans == 'Z':
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
                                time.sleep(delay*2)
                            else:
                                choice = set(choice)
                                choice = [owned_prop[(ord(i.lower()) - 96) - 1] for i in choice]
                                trade['prop2'] = choice 
                                break
                    break
            
            
        elif player2 == 'C':
            print("\n\n\n")
            return
        
        else:
            print("Invalid input.")


#trading('CHIN', '')



intro()

shuffle()


while True:
    database_copy = database.copy()
    for i in database_copy:
        while True:
            for prop in database:
                owned_property.extend(database[prop][2])
            time.sleep(1)
            street(i)
            if delay == 0:
                print("\n\n" + i + "'s turn.")
                roll(i)
                if i not in database:
                    break
                street(i)
                if delay == 0.15:
                    while True:
                        ans = input("Press ENTER to continue with TURBO on or X to exit TURBO   ")
                        if ans == "":
                            delay = 0
                            break
                        elif ans == "X":
                            delay = 0.3
                            print('Turning off TURBO', end = '', flush=True)
                            for i in range(3):
                                time.sleep(0.5)
                                print('.', end = '', flush=True)
                            time.sleep(0.5)
                            print("\n\n\n\n")
                            break
                        else:
                            print("Invalid input")
                break
            else:
                ans = input (i + "'s turn. Do you want to roll your die (ENTER), buy/ sell houses (H), trade (T), mortgage (M), get more information (I), turn on TURBO (TB) or exit (E) \n")
                if ans == '':
                    roll(i)
                    if i not in database:
                        break
                    street(i)
                    break
                elif ans == 'H':
                    buy_houses()
                elif ans == 'T':
                    trading(i, '')
                elif ans == 'M':
                    mortgage(i)
                elif ans == 'I':
                    info(i)
                elif ans == 'TB':
                    while True:
                        ans = input("Are you sure? You cannot turn off TURBO unless someone get's charged a large sum of money, someone is below £150 or someone gets new property. (Y/N)   ")
                        if ans == 'Y':
                            delay = 0
                            break
                        elif ans == 'N':
                            break
                        else:
                            print("Invalid input")
                elif ans == 'E':
                    break
                else:
                    print('Not one of the options. Try again')
                street(i)
        
    if ans == 'E':
        time.sleep(0.5)
        print("Thanks for playing!")
        break
# %%
