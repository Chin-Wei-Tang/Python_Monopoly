# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:42:22 2021

@author: 4664
"""

import time, string
tot_houses = 32
tot_hotels = 12
freePMon = 0
double = 0
roll_num = 0
chance_com_reroll = 0
choice = []
houses = {}



database = {'p1': [0, 1500, {1 : 2 , 3 : 3 , 21 : 0 , 29 : 0}, ['Brown'], 0, 1],
            'p2': [0, 1500, {5 : 0 , 18 : 1 , 39 : 1}, [], 0, 0],
            'p3': [0, 1500, {6 : 1 , 8 : 0 , 9 : 0 , 25 : 0}, ['Light Blue'], 0, 0],
            'p4': [0, 1500, {32 : 0 , 31 : 0 , 34 : 0}, ['Green'], 0, 0],
            'p5': [0, 1500, {}, [], 0, 0],
            'p6': [0, 1500, {}, [], 0, 0]}

streets = {'Brown':       [1, 3],
           'Light Blue':  [6, 8 , 9],
           'Pink':        [11, 13, 14],
           'Orange':      [16, 18, 19],
           'Red':         [21, 23, 24],
           'Yellow':      [26, 27, 29],
           'Green':       [31, 32, 34],
           'Dark Blue':   [37, 39]}

locations = ['Go', 'Old Kent Road (B)', 'Community chest', 'Whitechapel Road (B)', 'Income Tax',
          'Kings Cross Station', 'The Angel, Islington (LB)', 'Chance', 'Euston Road (LB)', 'Pentonville Road (LB)',
          'Jail', 'Pall Mall (P)', 'Electric Company', 'Whitehall (P)', 'Northumbland Avenue (P)',
          'Marylebone Station', 'Bow Street (O)', 'Community Chest', 'Marlborough Street (O)', 'Vine Street (O)',
          'Free Parking', 'Strand (R)', 'Chance', 'Fleet Street (R)', 'Trafalgar Square (R)', 
          'Frenchurch Station','Leicester Square (Y)','Coventry Street (Y)', 'Water Works','Piccadilly (Y)',
          'Go to Jail', 'Regent Street (G)', 'Oxford Street (G)', 'Community Chest', 'Bond Street (G)',
          'Liverpool St. Station', 'Chance', 'Park Lane (DB)', 'Super tax', 'Mayfair (DB)']

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


def street(a):
    pass



def pay(x, a, b):
    '''
    x- amount that needs to be transferred
    a- key to database dictionary for first player
    b- key to database dictionary for second player
    Transfers the money to/from that account (for 2 ppl interactions, use +ve value. From a to b)
    Prints value of player's account
    '''
    
    global database
    print('Monies transferring  ', end = '')
    for i in range(3):
        time.sleep(0.7)
        print('$  ', end = '')
    time.sleep(1)
    
    if b == '':
        database[a][1] += x
        if x> 0:
            print("\n£" + str(x) + " has been transferred to your account. ", end = "" )
            time.sleep(1)
            print("You've now got £" + str(database[a][1]) + " in your account now.")
            time.sleep(1)
            print('Pogggg')
        elif x<= 0:
            print("\n-£" + str(-x) + " has been transferred from your account. ", end = "")
            time.sleep(1)
            print("You've now got £" + str(database[a][1]) + " in your account now.")
            time.sleep(1)
            print('Ummmmmm... worth???')
        else:
            print('\nGlitch in the matrix')
        time.sleep(1)
    
    else:
        database[a][1] -= x
        database[b][1] += x
        print("\n£" + str(x) + " has been transferred from " + a + " to " + b)
        time.sleep(1)
        print(a + " now has £" + str(database[a][1]))
        time.sleep(1)
        print(b + " now has £" + str(database[b][1]))
        time.sleep(1)
        print('Lmao finessed.')



def trading(p, a):
    '''
    p- player
    a- action to recall function 
    '''
    global houses, choice
        
    if a == '':
        print("\nWelcome to trading. ")
        time.sleep(0.5)
        print("\nYou may only trade undeveloped property- ", end = "")
        time.sleep(0.5)
        print("you must sell off all buildings from a street before you can trade property from that street.")
        time.sleep(0.5)
        print("\nBuilding are sold at half the value. ")
        time.sleep(0.5)
    
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
                    time.sleep(0.3)
                    print(p + ": £" + str(trade['money1']) + " & ", end = "")
                    print( [locations[i] for i in trade['prop1']] )
                    time.sleep(0.3)
                    print(player2 + ": £" + str(trade['money2']) + " & ", end = "")
                    print( [locations[i] for i in trade['prop2']] )
                    time.sleep(0.3)
                    
                    while True:
                        ans = input("Finalise the trade (F), edit the trade (E) or cancel the trade (C)?   ")
                        if ans == 'F':
                            if trade['money1'] == trade['money2']:  # SELL ALL HOUSES BEFORE TRANSFERRING MONEY
                                print("\n\nNo money is transferred in this trade.")
                                time.sleep(0.5)
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
                                    time.sleep(0.3)
                                    for i in houses:
                                        print(locations[i] + ": " + str(houses[i]) + " house(s)")
                                        time.sleep(0.3)
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
                                                    print(locations[i], end = " ")
                                                else:
                                                    print(locations[i], end = ", ")
                                            print("has/ have been transferred from " + p + " to " + player2) 
                                            time.sleep(0.5)
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
                                            print(locations[i], end = " ")
                                        else:
                                            print(locations[i], end = ", ")
                                    print("has/ have been transferred from " + p + " to " + player2) 
                                    time.sleep(0.5)
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
                                    time.sleep(0.3)
                                    for i in houses:
                                        print(locations[i] + ": " + str(houses[i]) + " house(s)")
                                        time.sleep(0.3)
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
                                                    print(locations[i], end = " ")
                                                else:
                                                    print(locations[i], end = ", ")
                                            print("has/ have been transferred from " + player2 + " to " + p)
                                            time.sleep(0.5)
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
                                            print(locations[i], end = " ")
                                        else:
                                            print(locations[i], end = ", ")
                                    print("has/ have been transferred from " + player2 + " to " + p) 
                                    time.sleep(0.5)
                                    no_sell = 0
                            houses = {}
                            
                            
                            if no_sell == 1:
                                pass
                            else:
                                print("\n\nTrade has been completed!\n\n")
                                time.sleep(0.5)
                                street(p)
                                street(player2)
                                trading(p, 1)
                                return
                             
                        elif ans == 'E':
                            time.sleep(0.5)
                            break
                        
                        elif ans == 'C':
                            print("Cancelling", end = "")
                            for i in range(3):
                                time.sleep(0.5)
                                print('.', end = '')
                            time.sleep(0.5)
                            print("\n\n")
                            trading(p, 1) 
                            return
                        else:
                            print("Invalid input.")
                
                print("\n\n\n" + p + "'s part of the trade: ")
                while True:
                    time.sleep(0.3)
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
                    time.sleep(0.3)
                    for i in owned_prop:
                        print(string.ascii_uppercase[counter] + "- " + locations[i])
                        counter += 1
                        time.sleep(0.3)
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
                                time.sleep(0.5)
                                
                            else:
                                #houses = {}
                                choice = set(choice)
                                choice = [owned_prop[(ord(i.lower()) - 96) - 1] for i in choice]
                                trade['prop1'] = choice
                                break
                    break
                            
                print("\n\n\n" + player2 + "'s part of the trade: ")
                while True:
                    time.sleep(1)
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
                    time.sleep(0.3)
                    for i in owned_prop:
                        print(string.ascii_uppercase[counter] + "- " + locations[i])
                        counter += 1
                        time.sleep(0.3)
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
                                time.sleep(0.5)
                            else:
                                choice = set(choice)
                                choice = [owned_prop[(ord(i.lower()) - 96) - 1] for i in choice]
                                trade['prop2'] = choice 
                                break
                    break
            
            
        elif player2 == 'C':
            print("\n\n\n")
            return
            break
        
        else:
            print("Invalid input.")
            
            
            
trading('p1', '')