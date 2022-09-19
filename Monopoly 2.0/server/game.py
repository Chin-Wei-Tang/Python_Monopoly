import time, random, string, threading, pickle

from player import Player
from round import Round

class Game:
    
    #choice = [] TODO MIGHT BREAK THE TRADING METHOD
    #houses = {}

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

    

    
    def __init__(self, name): #TODO SORT OUT PRINT STATEMENTS
        self.name = name
        self.players = []   # player's go is always the first person
        self.round = None
        self.board = None
        self.num_turns = 0
        self.tot_houses = 32
        self.tot_hotels = 12
        self.freePMon = 0
        self.double = 0
        self.rolling = False
        self.roll_num = 0
        self.roll1 = None
        self.roll2 = None
        self.chance_com_reroll = 0
        self.delay = 0.25
        self.owned_property = []
        self.chance_deck = ['go', 'jail', 'pall_mall', 'trafalgar', 'street_repairs', 'station', 'dividend', 'jail_card', 'back_3', 
                'general_repairs', 'speeding', 'school', 'drunk', 'loan_matures', 'crossword', 'mayfair']
        self.community_chest_deck = ['bank_error', 'doctor', 'stock', 'old_kent', 'annuity', 'income', 'birthday', 'fine', 'hospital',
                            'interest', 'insurance', 'beauty', 'inherit']
        self.buttons = ['Roll', 'Houses', 'Trade', 'Mortgage']
        self.button_pressed = ''
        self.msg = 'Welcome to Monopoly'
        self.morg_property = []
        self.houseable_property = []
        self.num_voted_turbo = 0
        self.player_buying_houses = None
        self.intro()
        #self.shuffle()
        

    def get_name(self):
        return self.name

    def get_players(self):
        return self.players

    def add_player(self, player):
        if len(self.players) < 8:
            self.players.append(player)
            return True
        return False

    def get_round(self):
        return self.round

    def get_delay(self):
        return self.delay

    def set_delay(self, number):
        self.delay = number

    def get_roll1(self):
        return self.roll1

    def get_roll2(self):
        return self.roll2

    def get_roll_num(self):
        return self.roll_num

    def get_rolling(self):
        return self.rolling

    def get_buttons(self):
        return self.buttons

    def set_buttons(self, buttons):
        '''
        input: buttons - list (of choices e.g ['Yes' , 'No']) or str
        '''
        self.buttons = buttons

    def get_button_pressed(self):
        return self.button_pressed

    def set_button_pressed(self, button):
        self.button_pressed = button

    def get_msg(self):
        return self.msg

    def set_msg(self, msg):
        self.msg = msg

    def get_morg_property(self):
        return self.morg_property

    def get_houseable_property(self):
        return self.houseable_property

    def get_num_voted_turbo(self):
        return self.num_voted_turbo

    def set_num_voted_turbo(self, num):
        self.num_voted_turbo += num
        if self.num_voted_turbo == len(self.players):
            self.delay = 0
            self.num_voted_turbo = 0
            print("set delay to 0")
            self.msg = 'TURBO TURNED ON'
            # for i in range(3):
            #     time.sleep(0.5)
            #     self.msg += '. '
            #     print(self.msg)
            time.sleep(1)

    def get_player_buying_houses(self):
        return self.player_buying_houses

    def set_player_buying_houses(self, player):
        if self.player_buying_houses == None:
            self.player_buying_houses = player

    def get_houses(self):
        return self.tot_houses

    def get_hotels(self):
        return self.tot_hotels

    def get_freePMon(self):
        return self.freePMon

    def choice_lock(self, choice, msg = ""):
        '''
        locks the game until a buttons is pressed on the gui, option to display message
        input:
            choice - list or str
            msg - str
        '''
        self.button_pressed = ''
        while self.button_pressed == '' and self.round.get_round_ended() != True:
            self.msg = msg
            self.buttons = choice
        self.msg = ''

    def save_game(self):
        '''
        saves game in a file
        '''
        with open('data.pkl', 'wb') as wf:
            pickle.dump(self, wf)
            #fprint('loaded data')

    def start_game(self):
        while len(self.players) > 0: # TODO CHANGE BACK TO 1
            self.msg = self.players[0].get_name() + "'s turn"
            self.round = Round(self, self.players[0])
            self.round.start_round()
            self.players.append(self.players[0])
            self.players.remove(self.players[0])
            self.player_buying_houses = None
            self.save_game()
            self.num_turns += 1
            print("\n")

    def add_owned_property(self, property):
        self.owned_property.extend(property)
        return

    def auction(self, player, property):
        '''
        input: player - object ; property - int
        returns: None
        '''

        bid = 1
        players = {key:1 for key in self.players if key != player}

        time.sleep(0.5)

        if self.delay == 0:
            self.delay = 0.15

        if property == '':
            #print("\n\nAuction starts at £1. Type enter to pass or a number to place bet.")
            self.msg = "Auction starts at £1. Pass or place a bet."
        else:
            #print("\n\n\n\nAuctioning off " + Game.locations[property] + ". Auction starts at £1. Type enter to pass or a number to place bet.")
            self.msg = "Auctioning off " + Game.locations[property] + ". Auction starts at £1. Type enter to pass or a number to place bet."
            time.sleep(0.5)
            if isinstance(player.get_property(property), float) == True:
                #print("\nThis is property is mortgaged and will go to the new player as mortgaged.")
                self.msg = "This is property is mortgaged and will go to the new player as mortgaged."
        
        while True:
            if sum(players.values()) == 1:
                for keys in players:
                    if players.get(keys) == 1:
                        #print("Congrats- " + str(keys.get_name()) + " wins this auction!")
                        self.msg = "Congrats- " + str(keys.get_name()) + " wins this auction!"
                        self.pay(-bid, keys, "")
                        if property == '':
                            keys.set_property(player.get_position(), 0, '')
                        else:
                            if isinstance(player.get_property(property), float) == True:
                                keys.set_property(property, 0.0, '')
                            else:
                                keys.set_property(property, 0, '')
                            player.remove_property(property)
                break
            else:
                for keys in players:
                    time.sleep(0.5)
                    if sum(players.values()) == 1:
                        break
                    elif players[keys] == 0:
                        pass
                    else:
                        while True:
                            #ans = input(keys.get_name() + "'s turn to place bid-   £")
                            self.choice_lock(['Bid', 'Pass'], ) #TODO AUCTION BID AUTO PASS WHEN ROUND OVER
                            time.sleep(0.5)
                            if self.button_pressed == "":
                                #print("You passed. You will not be able to participate for the rest of the auction.\n")
                                self.msg = "You passed. You will not be able to participate for the rest of the auction."
                                players[keys] = 0
                                break
                            elif int(self.button_pressed) > bid:
                                #print("You have placed the highest bid so far. \n")
                                self.msg = "You have placed the highest bid so far"
                                bid = int(ans)
                                break
                            elif int(self.button_pressed) <= bid:
                                #print("Your bid isn't high enough. Try again.")
                                self.msg = "Your bid isn't high enough. Try again."
                            else:
                                #print("Your input isn't valid.")
                                self.msg = "Your input isn't valid"



    def bankruptcy(self, amount, player1, player2, recall):
        '''
        checks if someone is going to go bankrupt. sorts out what happens to a bankrupt player. player1 in the player that owes the money, player2 in the player that is owed money. player2 is left '' for bank.
        input: amount- int ; player1- object ; player2- object ; recall-any
        returns: None
        '''
        
        if amount > player1.get_money():
            if recall == '':
                #print(player1.get_name() + " is about to go bankrupt!!!")
                self.msg = player1.get_name() + " is about to go bankrupt!!!"
                time.sleep(0.5)
                #print("\nThe money that you have to pay is more than what you have in your account.")
                self.msg = "The money that you have to pay is more than what you have in your account."
                time.sleep(0.5)
                #print("\nYou have to pay £" + str(amount) + " and you only have £" + str(player1.get_money()))
                self.msg = "You have to pay £" + str(amount) + " and you only have £" + str(player1.get_money())
                time.sleep(0.5)
            while True:
                #ans = input("\n\nDo you want to sell houses (H), mortgage (M), trade (T) or declare bankrupcy (D)?   ")
                self.choice_lock(['Sell houses', 'Mortgage', 'Trade', 'Bankruptcy'], )
                print("\n")
                if self.button_pressed == 'Sell houses':
                    self.buy_houses()
                    self.bankruptcy(amount, player1, player2, 1)
                    return
                elif self.button_pressed == 'Mortgage':
                    self.mortgage(player1)
                    self.bankruptcy(amount, player1, player2, 1)
                    return
                elif self.button_pressed == 'Trade':
                    self.trading(player1, '')
                    self.bankruptcy(amount, player1, player2, 1)
                    return
                elif self.button_pressed == 'Bankruptcy' or self.round.get_round.ended():
                    self.choice_lock(['Yes', 'No'], "Are you sure?")
                    if self.button_pressed == 'No':
                        pass
                    elif self.button_pressed == 'Yes' or self.round.get_round.ended():
                        price = 0
                        owned_prop = player1.get_property('').copy()
                        #print("\nSelling all houses", end = "")
                        self.msg = "Selling all houses..."
                        time.sleep(1)
                        for i in range(3):
                            time.sleep(0.5)
                            print('.', end = '')
                        time.sleep(0.5)
                        print("\n")
                        
                        for i in owned_prop:
                            if player1.get_property(i) != 0:
                                price += player1.get_property(i) * self.property[i][6][1]
                                player1.set_property(i, 0, '')
                        self.pay(price, player1, '')
                        
                        if player2 == '':
                            for i in owned_prop:
                                self.auction(player1, i)
                        else:
                            print("\n")
                            self.pay(player1.get_money(), player1, player2)
                            #print("\nTransferring properties", end = "")
                            self.msg = "Transferring properties..."
                            time.sleep(1)
                            for i in range(3):
                                time.sleep(0.5)
                                if i == 2:
                                    print('.')
                                else:
                                    print('.', end = '')
                            time.sleep(0.5)
                            self.msg = ''
                            for i in owned_prop:
                                if isinstance(player1.get_property(i), float) == True:
                                    player2.set_property(i, 0.0, '')
                                    if i == list(player1.get_property(''))[-1]:
                                        #print(self.locations[i] + " (mortgaged)", end = " ")
                                        self.msg += self.locations[i] + " (mortgaged) "
                                    else:
                                        #print(self.locations[i] + " (mortgaged)", end = ", ")
                                        self.msg += self.locations[i] + " (mortgaged), "
                                else:
                                    player2.set_property(i, 0, '')
                                    if i == list(player1.get_property(''))[-1]:
                                        #print(self.locations[i], end = " ")
                                        self.msg += self.locations[i] + " "
                                    else:
                                        #print(self.locations[i], end = ", ")
                                        self.msg += self.locations[i] + ", "
                                player1.remove_property(i)
                                
                            #print("has/ have been transferred from " + player1.get_name() + " to " + player2.get_name()) 
                            self.msg += "has/ have been transferred from " + player1.get_name() + " to " + player2.get_name()
                        self.double = 0
                        self.roll_num = 0
                        self.chance_com_reroll = 0
                        self.players.remove(player1)
                        time.sleep(1)
                        self.msg = "Aight " + player1.get_name() + "..."
                        time.sleep(1)
                        self.msg = "Sry to break it to u but ur kinda dog at this game."
                        time.sleep(1)
                        self.msg = "Better luck next time!"
                        time.sleep(1.5)
                        self.msg = "\nI appreciate u playing anyways :p"
                        time.sleep(1)
                        break
                else:
                    #print("Invalid input")
                    self.msg = "Invalid input"



    def buy_houses(self):   #TODO SORT OUT TIMING FOR BUYING HOUSES & ALL OF BUYING HOUSES OPTIONS
        '''
        houses
        '''
        #while True:
        streets_list = list(Game.streets.keys())
        #name = input("Please enter your Monopoly name to buy/ sell houses or C to cancel:   ")
        #self.choice_lock(['Name', 'Cancel'], )
        for player in self.players:
            if player.get_name() == self.player_buying_houses.get_name():
                name = player

        while True:
            self.choice_lock(['Choose street', 'Exit'], 'Choose street')

            if self.button_pressed == 'Exit':
                self.player_buying_houses = None
                break
            # self.msg = "Options:"
            # time.sleep(self.delay)
            # for st_index in range(8):
            #     print(str(st_index+1) + "- " + streets_list[st_index])
            #     time.sleep(self.delay)
            # print("I- more information")
            # time.sleep(self.delay)
            # print("C- Cancel")
            # time.sleep(self.delay)
            
            #while True:
                #streets_house = input("\n\nChoose which street you want to buy houses/ hotels for:   ")
            self.choice_lock(['Buy/ sell houses', 'Cancel'])

            if self.button_pressed == 'Cancel':
                break

            time.sleep(self.delay*2)
            if streets_house.isnumeric():
                if int(streets_house) in range(1, 9):
                    st_colour = streets_list[int(streets_house )-1]
                    st_prop = Game.streets[st_colour]
                    
                    if st_colour in name.get_streets():
                        houses_list = {index: name.get_property(index) for index in st_prop}
                        self.msg = "Options:"
                        time.sleep(self.delay)
                        counter = 1
                        for prop_index in st_prop:
                            if name.get_property(prop_index) == 5:
                                print(str(counter) + "- " + Game.locations[prop_index] + ": 1 hotel")
                            else:
                                print(str(counter) + "- " + Game.locations[prop_index] + ": " + str(name.get_property(prop_index)) + " houses")
                            counter += 1
                            time.sleep(self.delay)
                        print("C- Cancel")
                        #time.sleep(self.delay*3)
                        
                        
                        while True:
                            houses_list = {index: name.get_property(index) for index in st_prop}
                            on = 0
                            choice = []
                            
                            #ans = input("Enter the properties you want to buy houses/ hotels for (in the format 1,2,3) or cancel (C)-   ")
                            self.choice_lock(['Cancel'], "Choose the properties you want to buy houses/ hotels for") #TODO CHOOSE PROPERTIES & NUMBER OF HOUSES AT SAME TIME
                            if self.button_pressed == 'Cancel':
                                break
                            '''
                            for i in ans:
                                if i.isnumeric():
                                    if on == 1:
                                        print("You have to separate numbers with ,")
                                        time.sleep(self.delay)
                                        choice = []
                                        break
                                    elif on > len(st_prop):
                                        print("Invalid input")
                                        time.sleep(self.delay)
                                        choice = []
                                        break
                                    on = 1
                                    choice.append(i)
                                elif i == ",":
                                    if on == 0:
                                        print("Invalid input")
                                        time.sleep(self.delay)
                                        choice = []
                                        break
                                    on = 0
                                elif i == " ":
                                    pass
                                else:
                                    print("Invalid input")
                                    time.sleep(self.delay)
                                    choice = []
                                    break
                            '''
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
                            elif num_houses > self.tot_houses:
                                if self.tot_houses == 0:
                                    self.msg = "Sorry! All 32 houses have been bought. Please wait till there are houses available."
                                    time.sleep(self.delay)
                                else:
                                    self.msg = "Sorry! There are only " + str(self.tot_houses) + " left to buy."
                                    time.sleep(self.delay)
                            elif num_hotels > self.tot_hotels:
                                if self.tot_hotels == 0:
                                    self.msg = "Sorry! All 12 hotels have been bought. Please wait till there are hotels available."
                                    time.sleep(self.delay)
                                else:
                                    self.msg = "Sorry! There are only " + str(self.tot_hotels) + " left to buy."
                                    time.sleep(self.delay)
                            elif all(i < 6 for i in list(houses_list.values())) == False:
                                self.msg = "You cannot get more than 1 hotel per property! Don't be greedy! xd"
                                time.sleep(self.delay)
                            elif max(houses_list.values()) - min(houses_list.values()) > 1:
                                self.msg = "You cannot buy a house on this property now-"
                                time.sleep(self.delay)
                                self.msg += " you must have " + str(min(houses_list.values()) + 1) + " houses on each property on this street before you can get a " + str(max(houses_list.values())) + "th house on "
                                time.sleep(self.delay)
                                '''
                                print("Currently, you own ", end = "")
                                for i in st_prop:
                                    print(str(name.get_property(i)) + " house(s) on " + Game.locations[i] , end = "  ")
                                print("\n")
                                time.sleep(self.delay*3)
                                '''
                            else:
                                print("\n")
                                self.pay(-(len(choice)*Game.property[choice[0]][6][1]), name, '')
                                self.tot_houses -= num_houses
                                self.tot_hotels -= num_hotels
                                
                                #print("\nCongratulations- you now own: ")
                                time.sleep(self.delay)
                                for i in set(choice):
                                    num_houses_before = name.get_property(i) #TODO PROPERTIE CARDS TO SHOW HOW 
                                    name.set_property(i, houses_list[i], '')
                                    num_houses_after = name.get_property(i)
                                    '''
                                    if name.get_property(i) == 5:
                                        print("1 hotel on " + Game.locations[i]  + "- rent went from £" + str(Game.property[i][num_houses_before]) + " to £" + str(Game.property[i][num_houses_after]))
                                    else:
                                        print(str(num_houses_after) + " house(s) on " + Game.locations[i] + "- rent went from £" + str(Game.property[i][num_houses_before]) + " to £" + str(Game.property[i][num_houses_after]))
                                    time.sleep(self.delay)
                                    '''
                                time.sleep(self.delay*2)
                                
                                break
                                            
                                
                    else:
                        print("You don't have a completed " + st_colour + " street") #TODO SORT OUT ON THE CLIENT SIDE WHETHER YOU CAN CHOOSE THAT PROPERTY
                        time.sleep(self.delay*2)
                        
                else:
                    print("Invalid input")

                
                
                
            # elif self.button_pressed == "Sell":
            #     owned_prop = name.get_property('').copy()
            #     sell_houses = [i for i in owned_prop if owned_prop[i] != 0]
            #     if sell_houses == []:
            #         self.msg = "There are no available properties to sell houses for."
            #     else:
            #         self.msg = "Options:"
            #         counter = 0
            #         time.sleep(self.delay)
            #         '''
            #         for i in sell_houses:
            #             if owned_prop[i] == 5:
            #                 print(string.ascii_uppercase[counter] + "- " + Game.locations[i] + ":  1 hotel (£" + str(Game.property[i][6][1] / 2) + " per house)")
            #             else:
            #                 print(string.ascii_uppercase[counter] + "- " + Game.locations[i] + ":  " + str(owned_prop[i]) + " houses (£" + str(Game.property[i][6][1] / 2) + " per house)")
            #             counter += 1
            #             time.sleep(self.delay)
            #         '''
            #         while True:
            #             choice = []
            #             owned_prop = name.get_property('').copy()
            #             sell_houses = [i for i in owned_prop if owned_prop[i] != 0]
                        
            #             #ans = input("\n\nPlease list the properties you want to sell houses for (enter in the format A,B,C) or enter Z to cancel:   ")
            #             self.choice_lock(['Cancel'], "Choose the properties you want to sell houses for")
            #             if self.button_pressed == "Cancel":
            #                 break
            #             else:
            #                 for i in ans:
            #                     if i.isalpha():
            #                         if i in string.ascii_uppercase[0:int(len(sell_houses))]:
            #                             choice.append(i)
            #                         else:
            #                             print(i + " is an invalid input.")
            #                     if i.isnumeric():
            #                         print(i + " is an invalid input.")
                                    
            #                 if choice == []:
            #                     print("You didn't enter any valid property options.")
            #                     time.sleep(self.delay*2)
                                
            #                 else:
            #                     choice = set(choice)
            #                     choice = [sell_houses[(ord(i.lower()) - 96) - 1] for i in choice]
            #                     num_houses = 0
            #                     num_hotels = 0
            #                     price = 0
            #                     for i in choice:
            #                         while True:
            #                             ans = input("Enter number of houses to sell from " + Game.locations[i] + " or pass (P)-   ")
            #                             if ans.isnumeric():
            #                                 if int(ans) > owned_prop[i]:
            #                                     print("You cannot sell " + str(ans) + " houses- you only own " + str(owned_prop[i]) + " on this property.")
            #                                     time.sleep(self.delay*2)
            #                                 else:
            #                                     print(ans)
            #                                     print(owned_prop[i])
            #                                     if owned_prop[i] == 5 and int(ans) > 0:
            #                                         num_hotels += 1
            #                                         num_houses += (int(ans) -1)
            #                                     else:
            #                                         num_houses += int(ans)
            #                                     owned_prop[i] -= int(ans)
            #                                     price += int(ans) * (Game.property[i][6][1] / 2)
            #                                     break
            #                             elif ans == "P":
            #                                 break
            #                             else:
            #                                 print("Invalid input.")
                                        
            #                     fail = 0
            #                     for i in choice:
            #                         for colour in Game.streets:
            #                             if i in Game.streets[colour]:
            #                                 streets_houses = {j: owned_prop[j] for j in Game.streets[colour]}
            #                                 if max(streets_houses.values()) - min(streets_houses.values()) > 1:
            #                                     self.msg = "Sell houses evenly- you must have at most " + str(max(streets_houses.values())-1) + " on every property on " + colour + " street before you can sell more houses."
            #                                     time.sleep(self.delay*2)
            #                                     fail = 1
            #                                     break
            #                         if fail == 1:
            #                             break
                                    
                                    
            #                     if fail == 0 and price != 0:
            #                         print("\n")
            #                         self.pay(price, name, '')
            #                         self.tot_houses += num_houses
            #                         self.tot_hotels += num_hotels
            #                         owned_prop_before = name.get_property('').copy()
            #                         name.set_property('', '', owned_prop)
            #                         print("\nYou now own...")
            #                         time.sleep(self.delay)
            #                         for i in choice:
            #                             num_houses_after = owned_prop[i]
            #                             num_houses_before = owned_prop_before[i]
            #                             if num_houses_after == 5:
            #                                 print("1 hotel on " + Game.locations[i] + "- rent went from £" + str(Game.property[i][num_houses_before]) + " to £" + str(Game.property[i][num_houses_after]))
            #                             else:
            #                                 print(str(num_houses_after) + " house(s) on " + Game.locations[i] + "- rent went from £" + str(Game.property[i][num_houses_before]) + " to £" + str(Game.property[i][num_houses_after]))
            #                             time.sleep(self.delay)
            #                         time.sleep(self.delay*2)
            #                         print("\n")
            #                         break
                                    
            elif self.button_pressed == "Cancel":
                self.player_buying_houses = None
                break
            
            '''
            else:
                print("\nNot a valid Monopoly name.")

            print("\n")
            '''



    def chance(self, player, action): #TODO SORT OUT CHANCE AND COMMUNITY CHANCE ANIMATIONS
        '''
        draws a chance card
        input: player- object ; action- str
        returns: None
        '''
        
        if action == '':
            self.msg = "Drawing chance card"
            for i in range(3):
                time.sleep(self.delay*2)
                self.msg += '.'
            print("\n\n")
            time.sleep(self.delay*2)
            self.chance_deck.append(self.chance_deck[0])
            self.chance_deck.remove(self.chance_deck[0])
            self.chance(player, self.chance_deck[-1])
            
        
        elif action == 'go':
            player.set_position(0)
            self.msg = "Advance to Go! (Collect $200)"
            time.sleep(self.delay*2)
            self.pay(200, player, '')
            
        elif action == 'jail':
            self.msg = "Go to Jail. (Go directly to jail)"
            player.set_position(10)
            time.sleep(self.delay*2)
            self.jail(player)
                
        elif action == 'pall_mall':
            self.msg = "Advance to Pall Mall - If you pass Go, collect $200"
            time.sleep(self.delay*2)
            self.chance_com_reroll = 1
            player.set_position(11)
            self.msg = "You land on... "
            time.sleep(self.delay*2)
            self.msg += self.locations[player.get_position()] + "!"
            if player.get_position() > 11:
                time.sleep(self.delay*2)
                self.msg = "You also passed GO so $200 has been added to your account"
                self.pay(200, player, '')
            self.roll(player)
                
        elif action == 'trafalgar':
            self.msg = "Advance to Trafalgar Square – If you pass Go, collect $200"
            time.sleep(self.delay*2)
            self.chance_com_reroll = 1
            player.set_position(24) 
            self.msg = "You land on... "
            time.sleep(self.delay*2)
            self.msg += self.locations[player.get_position()] + "!"
            if player.get_position() > 24:
                time.sleep(self.delay*2)
                self.msg = "You also passed GO so $200 has been added to your account"
                self.pay(200, player, '')
            self.roll(player)
            
        elif action == 'street_repairs':
            self.msg = "You are assessed for street repairs: $40 per house, $115 per hotel"
            time.sleep(self.delay*2)
            houses_hotels = (player.get_property(i) for i in player.get_property('') if i not in [5, 15, 25, 35])
            num_houses = 0
            num_hotels = 0
            for i in houses_hotels:
                if i <5:
                    num_houses += i
                elif i == 5:
                    num_hotels += 1
            if num_houses + num_hotels == 0:
                self.msg = "Luckily you own 0 houses & hotels so don't have to pay anything"
            else:
                self.msg = "You own " + str(num_houses) + " houses and " + str(num_hotels) + " hotels so that's- "
                time.sleep(self.delay*2)
                self.msg += str(num_houses) + " x £40 = £" + str(num_houses * 40) + " and " + str(num_hotels) + " x £115 = £" + str(num_hotels * 115)
                if self.delay == 0 and ((num_houses * 40) + (num_hotels * 115)) > 150:
                    self.delay = 0.15
                    time.sleep(2)
                    self.msg = "SHEEEEEE " + player + " 'BOUT TO GET VIOLATED XDDDDD"
                    time.sleep(2)
                self.pay(-((num_houses * 40) + (num_hotels * 115)), player, '')
                self.freePMon += ((num_houses * 40) + (num_hotels * 115))
            
        elif action == 'station':
            self.msg = "Take a trip to Marylebone Station- if you pass Go collect £200"
            time.sleep(self.delay*2)
            self.chance_com_reroll = 1
            player.set_position(15)
            self.msg = "You land on... "
            time.sleep(self.delay*2)
            self.msg += self.locations[player.get_position()] + "!"
            if player.get_position() > 15:
                time.sleep(self.delay*2)
                self.msg = "You also passed GO so $200 has been added to your account"
                self.pay(200, player, '')
            self.roll(player)
            
        elif action == 'dividend':
            self.msg = "Bank pays you dividend of $50"
            self.pay(50, player, '')
            
        elif action == 'jail_card':
            self.msg = "Get Out of Jail Free Card"
            time.sleep(self.delay*2)
            self.msg = "You may use it when you go to jail to get out without having to roll a double or pay."
            player.set_jail_card(1)
            
        elif action == 'back_3':
            self.msg = "You have been teleported back three spaces"
            time.sleep(self.delay*2)
            player.set_position(player.get_position() - 3)
            self.chance_com_reroll = 1
            self.roll(player)
            
        elif action == 'general_repairs':
            self.msg = "Make general repairs on all your property: $25 per house, $100 per hotel"
            time.sleep(self.delay*2)
            houses_hotels = (player.get_property(i) for i in player.get_property('') if i not in [5, 15, 25, 35])
            num_houses = 0
            num_hotels = 0
            for i in houses_hotels:
                if i <5:
                    num_houses += i
                elif i == 5:
                    num_hotels += 1
            if num_houses + num_hotels == 0:
                self.msg = "Luckily you own 0 houses & hotels so don't have to pay anything"
            else:
                self.msg = "You own " + str(num_houses) + " houses and " + str(num_hotels) + " hotels so that's- "
                time.sleep(self.delay*2)
                self.msg += str(num_houses) + " x £25 = £" + str(num_houses * 25) + " and " + str(num_hotels) + " x £100 = £" + str(num_hotels * 100)
                if self.delay == 0 and ((num_houses * 25) + (num_hotels * 100)) > 150:
                    self.delay = 0.15
                    time.sleep(2)
                    self.msg = "SHEEEEEE " + player + " 'BOUT TO GET VIOLATED XDDDDD"
                    time.sleep(2)
                self.pay(-((num_houses * 25) + (num_hotels * 100)), player, '')
                self.freePMon += ((num_houses * 25) + (num_hotels * 100))
            
        elif action == 'speeding':
            self.msg = "Speeding fine $15"
            self.pay(-15, player, '')
            self.freePMon += 15
            
        elif action == 'school':
            self.msg = "Pay school fees of $150"
            self.pay(-150, player, '')
            self.freePMon += 150
            
        elif action == 'drunk':
            self.msg = "Drunk in charge- fine $20"
            self.pay(-20, player, '')
            self.freePMon += 20
            
        elif action == 'loan_matures':
            self.msg = "Your building and loan matures — Collect $150"
            self.pay(150, player, '')
            
        elif action == 'crossword':
            self.msg = "You have won a crossword competition — Collect $100"
            self.pay(100, player, '')
            
        elif action == 'mayfair':
            self.msg = "Advance to Mayfair"
            time.sleep(self.delay*2)
            player.set_position(39)
            self.chance_com_reroll = 1
            self.msg = "You have landed on... "
            self.msg += self.locations[player.get_position()] + "!"
            self.roll(player)
            
        else:
            print ("error")



    def community_chest(self, player, action):
        '''
        p- player which gets the community chest card
        a- community chest action
        '''
        global chance_com_reroll, freePMon, delay
        
        if action == '':
            self.msg = "Drawing community chest card"
            for i in range(3):
                time.sleep(self.delay*2)
                self.msg += '.'
            time.sleep(self.delay*2)
            self.community_chest_deck.append(self.community_chest_deck[0])
            self.community_chest_deck.remove(self.community_chest_deck[0])
            self.community_chest(player, self.community_chest_deck[-1])
        
        elif action == 'bank_error':
            self.msg = "Bank error in your favor — Collect $200"
            self.pay(200, player, '')
        
        elif action =='doctor':
            self.msg = "Doctor's fee — Pay $50"
            self.pay(-50, player, '')
            self.freePMon += 50
            
        elif action == 'stock':
            self.msg = "From sale of stock you get $50"
            self.pay(50, player, '')
            
        elif action == 'old_kent':
            self.msg = "Go back to Old Kent Road"
            time.sleep(self.delay*2)
            player.set_position(1)
            self.chance_com_reroll = 1
            self.msg = "You land on... "
            time.sleep(self.delay*2)
            self.msg += self.locations[player.get_position()] + "!"
            self.roll(player)
            
        elif action == 'annuity':
            self.msg = "Annuity matures. Collect $100"
            self.pay(100, player, '')
            
        elif action == 'income':
            self.msg = "Income tax refund – Collect $20"
            self.pay(20, player, '')
            
        elif action == 'birthday':
            self.msg = "It is your birthday — Collect $10 from each player"
            tot_paid = 0
            for i in self.players:
                if i == player:
                    pass
                else:
                    i.change_money(-10)
                    tot_paid += 10
            time.sleep(self.delay*2)
            self.msg = player.get_name() + " gets £" + str(tot_paid) + " from everyone else."
            self.pay(tot_paid, player, '')
            self.msg = "£10 has been deducted from everyone else's account"
            time.sleep(self.delay*2)
            
        elif action == 'fine':
            while True:
                #ans = input ("Pay a $10 fine (F) or take a Chance (C)-   ")
                self.choice_lock(['$10 fine', 'Chance'], )
                if self.button_pressed == '$10 fine':
                    self.pay(-10, player, '')
                    self.freePMon += 10
                    break
                elif self.button_pressed == 'Chance' or self.round.get_round_ended():
                    self.chance(player, '')
                    break
                else:
                    #print("Invalid input.")
                    self.msg = "Invalid input"
                
        elif action == 'hospital':
            self.msg = "Pay hospital fees of $100"
            self.pay(-100, player, '')
            self.freePMon += 100
            
        elif action == 'interest':
            self.msg = "Receive interest on 7% preference shares: $25"
            self.pay(25, player, '')
            
        elif action == 'insurance':
            self.msg = "Pay your insurance premium $50"
            self.pay(-50, player, '')
            self.freePMon += 50
            
        elif action == 'beauty':
            self.msg = "You have won second prize in a beauty contest – Collect $10"
            self.pay(10, player, '')
            
        elif action == 'inherit':
            self.msg = "You inherit $100"
            self.pay(100, player, '')



    def info(self): #TODO DON'T NEED INFO -> have property rent cards
        '''
        Gives option to look at bank account and property owned
        '''
        
        time.sleep(self.delay)
        print("\nOptions:")
        time.sleep(self.delay)
        print("A- everyone's balance")
        time.sleep(self.delay)
        print("B- everyone's owned property")
        time.sleep(self.delay)
        print("C- rent data & prices for all properties")
        time.sleep(self.delay)
        print("D- back")
        time.sleep(self.delay)
        
        self.choice_lock(["Everyone's balance", "Everyone's property", ""])

        while True:
            ans = input("Choice:   ")
            time.sleep(self.delay*2)
            if ans == 'A':
                for player in self.players:
                    time.sleep(self.delay)
                    print(player.get_name() + " has £" + str(player.get_money()))
                time.sleep(self.delay*2)
                
            elif ans == 'B':
                for player in self.players:
                    time.sleep(self.delay)
                    print('\n' + player.get_name() + " owns:")
                    if player.get_property('') == {}:
                        print("No property.")
                    else:
                        for i in player.get_property(''):
                            if player.get_property(i) == 5:
                                print(Game.locations[i] + " - 1 hotel  ,  ", end = "")
                            else:
                                print(Game.locations[i] + " - " + str(player.get_property(i)) + " house(s),  ", end = "")
                        if player.get_streets() == []:
                            print("and no streets.")
                        else:
                            print("and the ", end = "")
                            for i in player.get_streets():
                                if i == player.get_streets()[-1]:
                                    print(i, end = " ")
                                else:
                                    print(i, end = ", ")
                            print("street(s).")
                time.sleep(self.delay*3)
                
                
            elif ans == 'C':
                print("\nFormat- [rent for 0 houses, 1, 2, 3, 4, 1 hotel, [price of property, cost of house, mortgage]]")
                time.sleep(self.delay*7)
                for i in property:
                    print("\n" + str(Game.locations[i]) + "\n" + str(property[i]))
                    time.sleep(self.delay)
                time.sleep(self.delay*2)
                
            elif ans == 'D':
                break
            
            else:
                print("Last time I checked, " + ans + " wasn't A, B, C or D.")
                time.sleep(self.delay*2)
                
            print("\n")



    def intro(self):
        print("\n\n\n")
        intro = "WELCOME TO MONOPOLY!"
        for i in intro:
            print(i, end ="")
            time.sleep(0.2)

        print("\n\nThis game has a maximum of 8 players.")
        time.sleep(0.5)
        print("\nPlease enter your ingame name (press enter when all players are registered):")
        time.sleep(0.5)
        for i in range(8):
            ans = input("Player " + str(i+1) + ":   ")
            if ans == "":
                break
            else:
                ans = Player(ans, 0, 1500)
                self.add_player(ans)
        print("\n\n")


    def jail(self, player):
        
        if player.get_jail_turns() == 0:
            self.msg = "Welcome to jail."
            time.sleep(self.delay*3)
            self.msg = "To get out, choose to pay £50 or roll a double"
            time.sleep(self.delay*3)
            # self.msg = "On the third missed turn, if you don't roll a double, you have to pay £50"
            # time.sleep(self.delay*2)
            player.set_jail_turns(player.get_jail_turns() + 1)
            return
        
        if player.get_jail_turns() == 1:
            turn = "First"
        elif player.get_jail_turns() == 2:
            turn = "Second"
        elif player.get_jail_turns() == 3:
            turn = "Third"
        
        
        while True:
            if player.get_jail_card() != 0:
                #jail_choice = input("\n" + turn + " turn in jail - roll double (A), pay £50 (B) or use Get Out Of Jail Free Card (C)?   ")
                self.choice_lock(['Roll double', 'Pay £50', 'Use Jail Card'], )
            else:
                #jail_choice = input("\n" + turn + " turn in jail - roll double (A) or pay £50 (B)?   ")
                self.choice_lock(['Roll double', 'Pay £50'], )
            if self.button_pressed == "Roll double" or self.round.get_round_ended():
                self.rolling = True
                self.msg = "You roll"
                for i in range(3):
                    time.sleep(self.delay*2)
                    self.msg += '.'
                time.sleep(self.delay*2)
                roll_1 = random.randint(1, 6)
                roll_2 = random.randint(1, 6)
                self.msg += " " + str(roll_1)
                self.roll1 = roll_1
                time.sleep(self.delay*2)
                self.msg += " and "
                time.sleep(self.delay*2)
                self.msg += str(roll_2)
                self.roll2 = roll_2
                time.sleep(self.delay*3)
                self.rolling = False
                self.roll1 = None
                self.roll2 = None
                
                if roll_1 == roll_2:
                    self.msg = "You rolled a double!!! You are now free."
                    player.set_jail_turns(0)
                    self.roll_num = roll_1 + roll_2
                    time.sleep(self.delay*3)
                else:
                    if player.get_jail_turns() == 3:
                        self.msg = "This is your third turn in jail and you didn't roll a double. To get out you have to pay £50."
                        self.pay(-50, player, "")
                        player.set_jail_turns(0)
                    else:
                        self.msg = "Unlucky- you're still stuck in jail."
                        player.set_jail_turns(player.get_jail_turns() + 1)
                break
                
            elif self.button_pressed== "Pay £50":
                #print("Paying your way out of jail huh? ^^")
                self.msg = "Paying your way out of jail huh? ^^"
                time.sleep(self.delay*2)
                self.pay(-50, player, "")
                player.set_jail_turns(0)
                break
                
            elif self.button_pressed == "Use Jail Card" and player.get_jail_card() != 0:
                #print("Lucky guy...")
                self.msg = "Lucky guy..."
                time.sleep(self.delay*2)
                player.set_jail_turns(0)
                player.set_jail_card(player.get_jail_card() - 1)
                break
            
            else:
                #print("Invalid input.")
                self.msg = "Invalid input"
                time.sleep(self.delay*2)
            
            
        if player.get_jail_turns() == 0:
            self.msg = "We hope you enjoyed your stay. "
            time.sleep(self.delay*2)
            self.msg = "pls consider leaving a 5 star review on Trip Advisor "
            time.sleep(self.delay*3)
            self.msg += ":)"
            time.sleep(self.delay*2)
            self.roll(player)



    def mortgage(self, player):
        self.msg = "Welcome to mortgaging."
        time.sleep(self.delay*2)
        self.msg = "Property can be mortgaged for half it's value."
        time.sleep(self.delay*2)
        self.msg = "Rent cannot be collect from mortgaged property."
        time.sleep(self.delay*2)
        
        while True:
            self.choice_lock(['Mortgage', 'Unmortgage', 'Exit'], )
            if self.button_pressed == 'Mortgage':
                owned_prop = [i for i in player.get_property('') if isinstance(player.get_property(i), int) == True]
                print("properties that can be mortgaged - " + str(owned_prop))
                if owned_prop == []:
                    self.msg = "There are no available properties to mortgage."
                    print(self.msg)
                else:
                    self.morg_property = owned_prop
                    counter = 0
                    time.sleep(self.delay)
                    while True:
                        choice = []
                        houses = {}
                        self.choice_lock(['Choose properties', 'Confirm mortgage', 'Cancel'], "Choose the properties you want to mortgage")
                        if self.button_pressed == "Cancel":
                            break
                        else:
                            choice = self.button_pressed
                                    
                            if choice == 'no prop':
                                self.msg = "You didn't choose any properties"
                                time.sleep(self.delay*3)
                            else:
                                #if self.button_pressed == "Finalise mortgage": 
                                for i in player.get_streets():
                                    if len(set(self.streets[i]).intersection(set(choice))) > 0:
                                        for j in self.streets[i]:
                                            houses[j] = player.get_property(j)
                                for i in choice:
                                    if i not in list(houses) and i not in [5, 15, 25, 35]:
                                        houses[i] = player.get_property(i)
                                if sum(houses.values()) != 0:
                                    #print("\n" + player.get_name() + " has at least 1 house on streets where you want to mortgage property:")
                                    self.msg = "You have houses on streets that you want to mortgage property on"
                                    time.sleep(self.delay)# TODO HIGHLIGHT THE PROPERTIES THAT YOU NEED TO SELL HOUSES ON
                                    self.choice_lock(['Yes', 'No'], "Sell all houses on these properties so that you can mortgage?")
                                    if self.button_pressed == "Yes":
                                        tot_price = 0
                                        for i in houses:
                                            tot_price += (houses[i] * self.property[i][6][1] / 2)
                                            player.set_property(i, 0, '')
                                        self.pay(tot_price, player, '')
                                    elif self.button_pressed == "No":
                                        pass
                                
                                if self.button_pressed != "No":
                                    tot_price = 0
                                    [tot_price := tot_price + self.property[i][6][2] for i in choice]
                                    self.pay(tot_price, player, "")
                                    for i in choice:
                                        player.set_property(i, 0.0, '')
                                        if i == choice[-1]:
                                            print(self.locations[i], end = "")
                                        else:
                                            print(self.locations[i] + ", ", end = "")
                                    print(" has/ have been mortgaged.")
                                    break
                                
                        
                    
            elif self.button_pressed == 'Unmortgage':
                owned_prop = [i for i in player.get_property('') if isinstance(player.get_property(i), float) == True]
                if owned_prop == []:
                    #print("There are no available properties to unmortgage.")
                    self.msg = "There are no available properties to unmortgage."
                else:
                    #print("Options of property to unmortage:")
                    self.morg_property = owned_prop
                    counter = 0
                    time.sleep(self.delay)
                    while True:
                        choice = []
                        houses = {}
                        self.choice_lock(['Choose properties', 'Confirm unmortgage', 'Cancel'], "Choose the properties you want to unmortgage")
                        if self.button_pressed == "Cancel":
                            break
                        else:
                            choice = self.button_pressed
                                    
                            if choice == 'no prop':
                                self.msg = "You didn't enter any valid property options."
                                time.sleep(self.delay*2)
                            else:
                                # choice = set(choice)
                                # choice = [owned_prop[(ord(i.lower()) - 96) - 1] for i in choice]
                                # print("Choice & price of unmortgaging:" )
                                # time.sleep(self.delay)
                                # for i in choice:
                                #     print(self.locations[i] + ": £" +  str(round(self.property[i][6][2]*1.1)))
                                #     time.sleep(self.delay)
                                #while True:
                                    #ans = input("Finalise the unmortgage (F), edit (E) or cancel (C)?   ")
                                    # self.choice_lock(['Finalise', 'Edit', 'Cancel'], '')
                                    # if self.button_pressed == "Finalise": 
                                tot_price = 0
                                [tot_price := tot_price + (self.property[i][6][2]*1.1) for i in choice]
                                self.pay(-round(tot_price), player, "")
                                for i in choice:
                                    player.set_property(i, 0, '')
                                    if i == choice[-1]:
                                        print(self.locations[i], end = "")
                                    else:
                                        print(self.locations[i] + ", ", end = "")
                                print(" has/ have been unmortgaged.")
                                break
                                        
                                    # elif self.button_pressed == "Edit":
                                    #     break
                                    # elif self.button_pressed == "Cancel":
                                    #     break
                                    # else:
                                    #     #print("Invalid input.")
                                    #     self.msg = "Invalid input"
                                # if self.button_pressed == "Edit":
                                #     pass
                                # elif self.button_pressed == "Cancel":
                                #     break
                                # else:
                                #     break
                            
            elif self.button_pressed == 'Exit':
                break
            
            else:
                #self.msg = "Invalid input.")
                self.msg = "Invalid input"



    def pay(self, amount, player1, player2):
        '''
        Transfers the money to/from that account (for 2 ppl interactions, use +ve value. From player1 to player2)
        input: amount- int, player1- object, player2- object
        returns: None
        '''

        # TODO- FIX time.sleep
        if (player1.get_money() < 150 or abs(amount) >= 150) and self.delay == 0:
            self.delay = 0.15
        
        # if amount < 0 and player2 == '': TODO CHANGE BACK
        #     self.bankruptcy(-amount, player1, player2, '')
        # if amount > 0 and player2 != '':
        #     self.bankruptcy(amount, player1, player2, '')
        
        if amount == 0 or player1 not in self.players:
            return

        self.msg = 'Monies transferring '
        for i in range(3):
            time.sleep(self.delay*2)
            self.msg += '$  '
        time.sleep(self.delay*2)

        if player2 == '':
            player1.change_money(amount)
            if amount> 0:
                self.msg = "£" + str(amount) + " has been transferred to your account."
                time.sleep(self.delay*2)
                self.msg = "You've now got £" + str(player1.get_money()) + " in your account now."
                time.sleep(self.delay*2)
                self.msg = 'Pogggg'
            elif amount< 0:
                self.msg = "-£" + str(-amount) + " has been transferred from your account."
                time.sleep(self.delay*2)
                self.msg = "You've now got £" + str(player1.get_money()) + " in your account now."
                time.sleep(self.delay*2)
                self.msg = 'Ummmmmm... worth???'
            else:
                self.msg = 'Glitch in the matrix'
            time.sleep(self.delay*2)

        else:
            player1.change_money(-amount)
            player2.change_money(amount)
            self.msg = "£" + str(amount) + " has been transferred from " + str(player1.get_name()) + " to " + str(player2.get_name())
            time.sleep(self.delay*2)
            self.msg = str(player1.get_name()) + " now has £" + str(player1.get_money())
            time.sleep(self.delay*2)
            self.msg = str(player2.get_name()) + " now has £" + str(player2.get_money())
            time.sleep(self.delay*2)
            self.msg = 'Lmao finessed.'



    def rent(self, property, player):
        '''
        charges rent when a player land on someone else's property
        input: property- int ; player- object
        returns: None
        x- the index of the property
        a- the player that landed on the property
        '''
        
        for p in self.players:
            if property in p.get_property(''):
                number_houses = p.get_property(property)
                self.msg = "You landed on " + p.get_name() + "'s property- "
                time.sleep(self.delay*2)
                if isinstance(number_houses, float) == True:
                    self.msg = "Noice. This property has been mortgaged so you don't have to pay rent."
                    return
                else:
                    if property in [12, 28]:
                        if number_houses == 0:
                            self.msg += p.get_name() + " owns 1 utility "
                            self.msg += "and the rent costs £" + str(self.roll_num*4)
                            self.pay(self.roll_num*4, player, p)
                            return
                        elif number_houses == 1:
                            self.msg += p.get_name() + " owns 2 utilities "
                            self.msg += "and the rent costs £" + str(self.roll_num*10)
                            self.pay(self.roll_num*10, player, p)
                            return
                        time.sleep(self.delay*2)
                    elif property in [5, 15, 25, 35]:
                        self.msg += p.get_name() + " owns " + str(p.get_property(property) + 1) + " station(s) "
                        time.sleep(self.delay*2)
                    else:
                        self.msg += "this property has " + str(number_houses) + " house(s) "
                        time.sleep(self.delay*2)
                        
                    if p.get_streets() != []:
                        street_counter = 0
                        for owned_street in p.get_streets():
                            if property in Game.streets[owned_street] and number_houses == 0:
                                self.msg += "and " + p.get_name() + " owns " + owned_street +  " street so rent is doubled. Rent costs £" + str(Game.property[property][number_houses]*2)
                                self.pay(Game.property[property][number_houses]*2, player, p)
                                street_counter = 1
                                break
                            
                        if street_counter == 0:
                            if Game.property[property][number_houses] >= 150 and self.delay == 0:
                                self.delay = 0.15
                                time.sleep(2)
                                self.msg = "SHEEEEEE " + player.get_name() + " 'BOUT TO GET VIOLATED FRRRRRR"
                                time.sleep(2)
                            self.msg += "and the rent costs £" + str(Game.property[property][number_houses])
                            
                            self.pay(Game.property[property][number_houses], player, p)
                            break
                                
                    elif p.get_streets() == []:
                        self.msg += "and the rent costs £" + str(Game.property[property][number_houses])
                        self.pay(Game.property[property][number_houses], player, p)



    def roll(self, player):
        
        while True:
            for prop in self.players:
                self.owned_property.extend(prop.get_property(''))

            if player.get_jail_turns() != 0:
                self.jail(player)
                break
            
            if player.get_jail_turns() == 0:
                if self.chance_com_reroll == 1:
                    pass
                else:
                    if int(self.roll_num) != 0:
                        pass
                    else:
                        self.rolling = True
                        self.msg = 'You start on ' + Game.locations[player.get_position()] + " and roll"
                        for i in range(3):
                            time.sleep(self.delay*2)
                            self.msg += '.'
                        time.sleep(self.delay*2)
                        roll_1 = random.randint(1, 6)
                        roll_2 = random.randint(1, 6)
                        self.roll_num  = roll_1 + roll_2
                        self.msg += " " + str(roll_1)
                        self.roll1 = roll_1
                        time.sleep(self.delay*2)
                        self.msg += " and "
                        time.sleep(self.delay*2)
                        self.msg += str(roll_2)
                        self.roll2 = roll_2
                        time.sleep(self.delay*2)
                        self.rolling = False
                        self.roll1 = None
                        self.roll2 = None
                        
                        if roll_1 == roll_2:
                            self.double += 1
                            if self.double == 3:
                                self.msg = "You rolled 3 doubles! Go to jail! "
                                player.set_position(10)
                                self.double = 0
                                self.roll_num = 0
                                self.chance_com_reroll = 0
                                self.jail(player)
                                break
                            else:
                                self.msg = "That's a double!"
                            time.sleep(self.delay*2)
                        else:
                            self.double = 0
                
                    self.msg = "You advance " + str(self.roll_num) + " spaces"
                    
                    
                    if player.get_position() + int(self.roll_num)> 39:
                        if player.get_position() + int(self.roll_num) == 40:
                            player.set_position((player.get_position() + self.roll_num) % 40)
                            time.sleep(0.2*(self.roll_num + 2))
                            self.msg += ' and land on ' + Game.locations[player.get_position()] + '!'
                            time.sleep(self.delay*3)
                        else:
                            player.set_position((player.get_position() + self.roll_num) % 40)
                            self.msg += ", pass Go"
                            time.sleep(0.2*(self.roll_num + 2))
                            self.msg += ' and land on ' + Game.locations[player.get_position()] + '!'
                            time.sleep(self.delay*2)
                            self.msg = "Collect £200 for passing Go."
                            time.sleep(self.delay*3)
                            self.pay(200, player, '')
                    
                    else:
                        player.set_position((player.get_position() + self.roll_num) % 40)
                        time.sleep(0.2*(self.roll_num + 2))
                        self.msg += ' and land on ' + Game.locations[player.get_position()] + '!'
                        time.sleep(self.delay*3)

                        
        
                if player.get_position() in player.get_property(''):
                    self.msg = 'You already own this property'
                    
                elif player.get_position() in self.owned_property:
                    self.msg = "Unlucky buddy- you landed on someone else's property."
                    time.sleep(self.delay*3)
                    self.rent(player.get_position(), player)
                    
                elif player.get_position() in [0, 2, 4, 7, 10, 17, 20, 22, 30, 33, 36, 38]:
                    if player.get_position() == 2 or player.get_position() == 17 or player.get_position() == 33:
                        self.community_chest(player, '')
                    elif player.get_position() == 7 or player.get_position() == 22 or player.get_position() == 36:
                        self.chance(player, '')
                    elif player.get_position() == 0:
                        self.msg = 'Noice. Landed on Go.'
                        time.sleep(self.delay*3)
                        self.pay(+200, player, '')
                    elif player.get_position() == 4:
                        self.msg = 'Take the L lel. Income tax- pay £200.'
                        time.sleep(self.delay*3)
                        self.pay(-200, player, '')
                        self.freePMon += 200
                    elif player.get_position() == 10:
                        self.msg = 'Just visiting jail'
                    elif player.get_position() == 20:
                        self.msg = 'Noice. Landed on free parking.'
                        if self.freePMon > 200 and self.delay == 0:
                            time.sleep(1.5)
                            self.msg = "SHEEEEEE " + player.get_name() + " 'BOUT TO GET NICED FR"
                        self.pay(+self.freePMon, player, '')
                        self.freePMon = 0
                    elif player.get_position() == 30:
                        player.set_position(10)
                        self.double = 0
                        self.jail(player)
                    elif player.get_position() == 38:
                        print ('\nHaha sucker! Super tax- £100')
                        self.pay(-100, player, '')
                        self.freePMon += 100
                    else:
                        self.msg = 'Glitch in the matrix'
                        time.sleep(self.delay*2)
                        
                else:
                    while True:
                        #decision = input("This property costs £" + str(self.property[player.get_position()][6][0]) + '. You have £' + str(player.get_money()) + ' in your account. Buy or auction? (Type B/A) \n')
                        self.choice_lock(['Buy', 'Auction'], '')
                        if self.delay == 0:
                            self.delay = 0.15
                        if self.button_pressed == 'Buy' or self.round.get_round_ended():
                            self.pay(-self.property[player.get_position()][6][0], player, '')
                            player.set_property(player.get_position(), 0, '')
                            #print ('\nCongratulations! You now own ' + Game.locations[player.get_position()])
                            self.msg = 'Congratulations! You now own ' + Game.locations[player.get_position()]
                            time.sleep(self.delay*2)
                            break
                        elif self.button_pressed == 'Action':
                            self.auction(player, '')
                            break
                        else:
                            #print ("\nYou didn't type B/A")
                            self.msg = "You didn't type B/A"
                        time.sleep(self.delay*2)
                
        
                if self.double == 0:
                    self.roll_num = 0
                    self.chance_com_reroll = 0
                    break
                elif self.double == 1 or self.double ==2:
                    self.roll_num = 0
                    self.chance_com_reroll = 0
                    
                    #ans = input("\nPress enter to roll again. ")
                    self.choice_lock(["Roll again"], '')

                else:
                    #print ("error & double = " + str(self.double))
                    self.msg = "error & double = " + str(self.double)


    def shuffle(self):
        '''
        Shuffles chance and community decks
        '''
        while True:
            time.sleep(0.5)
            #decision = str(input("Would you like to shuffle the chance and community chest cards? (Y/N)   "))
            self.choice_lock(['Yes', 'No'], "Would you like to shuffle the chance and community chest cards?")
            if self.button_pressed == "Yes":
                time.sleep(0.5)
                self.msg = "Shuffling"
                time.sleep(0.5)
                for _ in range(3):
                    self.msg += "."
                    time.sleep(0.5)
                random.shuffle(self.community_chest_deck)    
                random.shuffle(self.chance_deck)
                self.msg = "Your cards have been shuffled... by Krammer"
                time.sleep(0.5)
                self.msg += " Don't be surprised if he wins."
                return self.chance_deck, self.community_chest_deck
                #return community_chest_deck
            elif self.button_pressed == "No":
                time.sleep(0.5)
                self.msg = "Why u tryna cheat??? Sus. Fined £200 for cheating."
                time.sleep(1)
                self.msg += "jk ;)"
            else:
                time.sleep(0.5)
                #print("Why you chatting WASS my G")
                self.msg = "Why you chatting WASS my G"


    def street(self, player):
        new_owned_streets = []
        stations_list = []
        property_list = [i for i in player.get_property('') if isinstance(player.get_property(i), float) == False]
        
        for street in self.streets:
            prop_of_streets = self.streets[street]
            if all(item in property_list for item in prop_of_streets):
                new_owned_streets.append(street)
            else:
                pass
            
        if new_owned_streets != player.get_streets():
            if len(new_owned_streets) > len(player.get_streets()):
                self.msg = "Congratulations " + player.get_name() + "! You now have completed the "
                for i in list(set(new_owned_streets) - set(player.get_streets())):
                    if i == list(set(new_owned_streets) - set(player.get_streets()))[-1]:
                        self.msg += i
                    else:
                        self.msg += i + " and "
                self.msg += " street(s)"
                time.sleep(self.delay*2)
                self.msg = "You may now purchase houses for this street(s)."
                time.sleep(self.delay*3)
                player.set_streets('', new_owned_streets)
            elif len(new_owned_streets) < len(player.get_streets()):
                self.msg = "Unfortunately " + player.get_name() + " you no longer own (a) completed, unmortgaged "
                for i in list(set(player.get_streets()) - set(new_owned_streets)):
                    if i == list(set(player.get_streets()) - set(new_owned_streets))[-1]:
                        self.msg += i
                    else:
                        self.msg += i + " and "
                self.msg += " street(s)"
                time.sleep(self.delay*2)
                self.msg = "You cannot buy houses for this street(s) any more."
                time.sleep(self.delay*3)
                player.set_streets('', new_owned_streets)
        
        if all(item in property_list for item in [12, 28]):
            if player.get_property(12) != 1:
                player.set_property(12, 1, '')
                player.set_property(28, 1, '')
                self.msg = "Congratulations " + player.get_name() + "! You now have 2 utilities."
                time.sleep(self.delay*2)
                self.msg = "Now when people land on your utilities, rent is 10x the dice roll."
                time.sleep(self.delay*5)
        elif 12 in property_list:
            if player.get_property(12) == 1:
                player.set_property(12, 0, '')
                self.msg = player.get_name() + " only has 1 utility now- rent is 4x dice roll"
                time.sleep(self.delay*2)
        elif 14 in property_list:
            if player.get_property(14) == 1:
                player.set_property(14, 0, '')
                self.msg = player.get_name() + " only has 1 utility now- rent is 4x dice roll"
                time.sleep(self.delay*2)
        
        
        counter = 0
        for station in [5, 15, 25, 35]:
            if station in property_list:
                counter += 1
                stations_list.append(station)
        if stations_list != []:
            if (counter-1) != player.get_property(stations_list[0]):
                if (counter-1) > player.get_property(stations_list[0]):
                    self.msg = "Congratulations " + player.get_name() + "! You now own " + str(counter) + " stations."
                    time.sleep(self.delay*2)
                elif (counter-1) < player.get_property(stations_list[0]):
                    self.msg = player.get_name() + " now has only got " + str(counter) + " rentable stations."
                    time.sleep(self.delay*2)
                for station in stations_list:
                    player.set_property(station, (counter-1), '')
                
        
        player_prop = {i : player.get_property(i) for i in sorted(list(player.get_property('').keys()))}
        player.set_property('', '', player_prop)
        



    def trading(self, player, action):
        '''
        for trading property and money between players
        input: player- object ; action- any
        returns: None
        '''
        if action == '':
            self.msg = "Welcome to trading. "
            time.sleep(self.delay*2)
            self.msg = "You may only trade undeveloped property."
            time.sleep(self.delay*2)
            '''
            print("you must sell off all buildings from a street before you can trade property from that street.")
            time.sleep(self.delay*2)
            print("\nBuilding are sold at half the value. ")
            time.sleep(self.delay*2)
            '''
        
        trade = {'money1': 0,
                'prop1' : [],
                'money2': 0,
                'prop2' : []}
        choice = []
        houses = {}
        no_sell = 0
        
        while True:
            #player2 = input("\n" + player.get_name() + ", enter the Monopoly name of the player who you are trading with or stop trading (C):   ")
            self.choice_lock(['Stop trading'], "Choose the player who you are trading with") # TODO FIX TRADING

            if self.button_pressed == 'Stop trading':
                return 


            while True:
                if trade['money1'] != 0 or trade['prop1'] != [] or trade['money2'] != 0 or trade['prop2'] != []: #TODO TRADE PICTURES
                    print("\n\n\nCurrently the trade is:")
                    time.sleep(self.delay)
                    print(player.get_name() + ": £" + str(trade['money1']) + " & ", end = "")
                    print( [Game.locations[i] for i in trade['prop1']] )
                    time.sleep(self.delay)
                    print(player2.get_name() + ": £" + str(trade['money2']) + " & ", end = "")
                    print( [Game.locations[i] for i in trade['prop2']] )
                    time.sleep(self.delay)
                    
                    while True:
                        #ans = input("Finalise the trade (F), edit the trade (E) or cancel the trade (C)?   ")
                        self.choice_lock(["Finalise trade", "Edit trade", 'Cancel'], )
                        if self.button_pressed == 'Finalise trade':
                            if trade['money1'] == trade['money2']: 
                                #print("\n\nNo money is transferred in this trade.")
                                self.msg = "No money is transferred in this trade."
                                time.sleep(self.delay*2)
                                pass
                            elif trade['money1'] > trade['money2']:
                                print("\n\n")
                                amount = int(trade['money1']) - int(trade['money2'])
                                self.pay(amount, player, player2)
                            elif trade['money2'] > trade['money1']:
                                print("\n\n")
                                amount = int(trade['money2']) - int(trade['money1'])
                                self.pay(amount, player2, player)
                        
                                
                            if trade['prop1'] == []:
                                pass
                            else:
                                for i in player.get_streets():
                                    if len(set(Game.streets[i]).intersection(set(trade['prop1']))) > 0:
                                        for j in Game.streets[i]:
                                            houses[j] = player.get_property(j)
                                for i in trade['prop1']:
                                    if i not in list(houses) and i not in [5, 15, 25, 35]:
                                        houses[i] = player.get_property(i)
                                if sum(houses.values()) != 0:
                                    self.msg = player.get_name() + " has at least 1 house on streets where you want to trade property" #TODO SORT OUT SHOWING PROPERTIES TO SELL HOUSES
                                    time.sleep(self.delay)
                                    for i in houses:
                                        print(Game.locations[i] + ": " + str(houses[i]) + " house(s)")
                                        time.sleep(self.delay)
                                    while True:
                                        #ans = input("Sell all houses on these properties so that you can trade them (Y/N)?   ")
                                        self.choice_lock(['Yes', 'No'], "Sell all houses on these properties so that you can trade them")
                                        if self.button_pressed == "Yes" or self.round.get_round_ended():
                                            tot_price = 0
                                            for i in houses:
                                                tot_price += (houses[i] * Game.property[i][6][1] / 2)
                                                player.set_property(i, 0, '')
                                            self.pay(tot_price, player, '')
                                            for i in trade['prop1']:
                                                if isinstance(player.get_property(i), float) == True:
                                                    player2.set_property(i, 0.0, '')
                                                else:
                                                    player2.set_property(i, 0, '')
                                                player.remove_property(i)
                                            print("\n")
                                            for i in trade['prop1']:
                                                if i == trade['prop1'][-1]:
                                                    print(Game.locations[i], end = " ")
                                                else:
                                                    print(Game.locations[i], end = ", ")
                                            print("has/ have been transferred from " + player.get_name() + " to " + player2.get_name()) 
                                            time.sleep(self.delay*2)
                                            no_sell = 0
                                            break
                                        elif self.button_pressed == "No":
                                            no_sell = 1
                                            break
                                        else:
                                            #print("Invalid input")
                                            self.msg = "Invalid input"
                                elif sum(houses.values()) == 0:
                                    for i in trade['prop1']:
                                        if isinstance(player.get_property(i), float) == True:
                                            player2.set_property(i, 0.0, '')
                                        else:
                                            player2.set_property(i, 0, '')
                                        player.remove_property(i)
                                    print("\n")
                                    for i in trade['prop1']:
                                        if i == trade['prop1'][-1]:
                                            print(Game.locations[i], end = " ")
                                        else:
                                            print(Game.locations[i], end = ", ")
                                    print("has/ have been transferred from " + player.get_name() + " to " + player2.get_name()) 
                                    time.sleep(self.delay*2)
                                    no_sell = 0
                                
                            houses = {}
                                        
                                        
                                
                            if trade['prop2'] == [] or no_sell == 1:
                                pass
                            else:
                                for i in player2.get_streets():
                                    if len(set(Game.streets[i]).intersection(set(trade['prop2']))) > 0:
                                        for j in Game.streets[i]:
                                            houses[j] = player2.get_property(j)
                                for i in trade['prop2']:
                                    if i not in list(houses) and i not in [5, 15, 25, 35]:
                                        houses[i] = player2.get_property(i)
                                if sum(houses.values()) != 0:
                                    print("\n\n\n" + player2.get_name() + " has at least 1 house on streets where you want to trade property:")
                                    time.sleep(self.delay)
                                    for i in houses:
                                        print(Game.locations[i] + ": " + str(houses[i]) + " house(s)")
                                        time.sleep(self.delay)
                                    while True:
                                        #ans = input("Sell all houses on these properties so that you can trade them (Y/N)?   ")
                                        self.choice_lock(['Yes', 'No'], "Sell all houses on these properties so that you can trade them")
                                        if self.button_pressed == "Yes":
                                            tot_price = 0
                                            for i in houses:
                                                tot_price += (houses[i] * Game.property[i][6][1] / 2)
                                                player2.set_property(i, 0, '')
                                            self.pay(tot_price, player2, '')
                                            for i in trade['prop2']:
                                                if isinstance(player2.get_property(i), float) == True:
                                                    player.set_property(i, 0.0, '')
                                                else:
                                                    player.set_property(i, 0, '')
                                                player2.remove_property(i)
                                            print("\n")
                                            for i in trade['prop2']:
                                                if i == trade['prop1'][-1]:
                                                    print(Game.locations[i], end = " ")
                                                else:
                                                    print(Game.locations[i], end = ", ")
                                            print("has/ have been transferred from " + player2.get_name() + " to " + player.get_name())
                                            time.sleep(self.delay*2)
                                            no_sell = 0
                                            break
                                        elif self.button_pressed == "No":
                                            no_sell = 1
                                            break
                                        else:
                                            #print("Invalid input")
                                            self.msg = "Invalid input"
                                elif sum(houses.values()) == 0:
                                    for i in trade['prop2']:
                                        if isinstance(player2.get_property(i), float) == True:
                                            player.set_property(i, 0.0, '')
                                        else:
                                            player.set_property(i, 0, '')
                                        player2.remove_property(i)
                                    print("\n")
                                    for i in trade['prop2']:
                                        if i == trade['prop2'][-1]:
                                            print(Game.locations[i], end = " ")
                                        else:
                                            print(Game.locations[i], end = ", ")
                                    print("has/ have been transferred from " + player2.get_name() + " to " + player.get_name()) 
                                    time.sleep(self.delay*2)
                                    no_sell = 0
                            houses = {}
                            
                            
                            if no_sell == 1:
                                pass
                            else:
                                print("\n\nTrade has been completed!\n\n")
                                time.sleep(self.delay*2)
                                self.street(player)
                                self.street(player2)
                                self.trading(player, 1)
                                return
                            
                        elif self.button_pressed == 'Edit': # TODO CONTINUE WITH THE CHOICE LOCK
                            time.sleep(self.delay*2)
                            break
                        
                        elif self.button_pressed == 'Cancel':
                            print("Cancelling", end = "")
                            for i in range(3):
                                time.sleep(self.delay*2)
                                print('.', end = '')
                            time.sleep(self.delay*2)
                            print("\n\n")
                            self.trading(player, 1) 
                            return
                        else:
                            #print("Invalid input.")
                            self.msg = "Invalid input"
                
                print("\n\n\n" + player.get_name() + "'s part of the trade: ")
                while True:
                    time.sleep(self.delay)
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
                    owned_prop = list(player.get_property('').keys())
                    choice = []
                    print("\nOptions of property to trade: ")
                    time.sleep(self.delay)
                    for i in owned_prop:
                        print(string.ascii_uppercase[counter] + "- " + Game.locations[i])
                        counter += 1
                        time.sleep(self.delay)
                    while True:
                        #ans = input("Please list the properties you want to trade (enter in the format A,B,C) or enter Z to pass:   ")
                        self.choice_lock(['Cancel'], "Choose the properties that you want to trade.")
                        if self.button_pressed == 'Cancel':
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
                                time.sleep(self.delay*2)
                                
                            else:
                                #houses = {}
                                choice = set(choice)
                                choice = [owned_prop[(ord(i.lower()) - 96) - 1] for i in choice]
                                trade['prop1'] = choice
                                break
                    break
                            
                print("\n\n\n" + player2.get_name() + "'s part of the trade: ")
                while True:
                    time.sleep(self.delay*3)
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
                    owned_prop = list(player2.get_property('').keys())
                    choice = []
                    print("\nOptions of property to trade: ")
                    time.sleep(self.delay)
                    for i in owned_prop:
                        print(string.ascii_uppercase[counter] + "- " + Game.locations[i])
                        counter += 1
                        time.sleep(self.delay)
                    while True:
                        #ans = input("Please list the properties you want to trade (enter in the format A,B,C) or enter Z to pass:   ")
                        self.choice_lock(['Cancel'], 'Choose the properties that you want to trade')
                        if self.button_pressed == 'Cancel':
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
                                time.sleep(self.delay*2)
                            else:
                                choice = set(choice)
                                choice = [owned_prop[(ord(i.lower()) - 96) - 1] for i in choice]
                                trade['prop2'] = choice 
                                break
                    break
                
                
            
            else:
                #print("Invalid input.")
                self.msg = "Invalid input"



