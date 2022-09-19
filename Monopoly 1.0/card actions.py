# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:41:01 2021

@author: leost

"""

import time
import random

costOfProp = 10
freePMon = 100


database = {'p1': [0, 1500, [1, 21, 29]],
            'p2': [0, 1500, []],
            'p3': [0, 1500, []],
            'p4': [0, 1500, []],
            'p5': [0, 1500, []],
            'p6': [0, 1500, []],}


locations = ['Go', 
          'Brown- Old Kent Road',
          'Community chest',
          'Brown- Whitechapel road',
          'Income Tax',
          'Kings Cross Station',
          'Light Blue- The Angel, Islington',
          'Chance',
          'Light Blue- Euston Road',
          'Light Blue- Pentonville Road',
          'Jail',
          'Pink- Pall Mall',
          'Electric Company',
          'Pink- Whitehall',
          'Pink- Northumbland Avenue',
          'Marylebone Station',
          'Orange- Bow Street',
          'Community Chest',
          'Orange- Marlborough Street',
          'Orange- Vine Street',
          'Free Parking',
          'Red- Strand',
          'Chance',
          'Red- Fleet Street',
          'Red- Trafalgar Square',
          'Frenchurch Station',
          'Yellow- Leicester Square',
          'Yellow- Coventry Street',
          'Water Works',
          'Yellow- Piccadilly',
          'Go to Jail',
          'Green- Regent Street',
          'Green- Oxford Street',
          'Community Chest',
          'Green- Bond Street',
          'Liverpool St. Station',
          'Chance',
          'Dark Blue- Park Lane',
          'Super tax',
          'Dark Blue- Mayfair']

chance_deck = ["Advance to Go! (Collect $200)",
               "Go to Jail. (Go directly to jail)",
               "You are assessed for street repairs: $40 per house, $115 per hotel",
               "Advance to Pall Mall - If you pass Go, collect $200",
               "Advance to Trafalgar Square – If you pass Go, collect $200"
               "Advance to Mayfair",
               "Take a trip to Marylebone Station and if you pass Go collect £200",
               "Bank pays you dividend of $50",
               "Get Out of Jail Free",
               "Go Back Three Spaces",
               "Make general repairs on all your property – For each house pay $25 – For each hotel $100",
               "Speeding fine $15",
               "Pay school fees of $150",
               "Drunk in charge fine $20",
               "Your building and loan matures — Collect $150",
               "You have won a crossword competition — Collect $100"]

GO = "Advance to Go! (Collect $200)"
Jail = "Go to Jail. (Go directly to jail)"
Pall_Mall = "Advance to Pall Mall - If you pass Go, collect $200"
Trafalgar = "Advance to Trafalgar Square – If you pass Go, collect $200"
Street_repairs = "You are assessed for street repairs: $40 per house, $115 per hotel"
Station = "Take a trip to Marylebone Station and if you pass Go collect £200"
Dividend = "Bank pays you dividend of $50"
Jail_Card = "Get Out of Jail Free"
Back_3 = "Go Back 3 Spaces"
General_repairs = "Make general repairs on all your property–For each house pay $25 – For each hotel $100"
Speeding = "Speeding fine $15"
School = "Pay school fees of $150"
Drunk = "Drunk in charge fine $20"
Loan_matures = "Your building and loan matures — Collect $150"
Crossword = "You have won a crossword competition — Collect $100"
Mayfair = "Advance to Mayfair"


community_chest_deck = ["Advance to Go (Collect $200)",
                        "Bank error in your favor — Collect $200",
                        "Doctor's fee — Pay $50",
                        "From sale of stock you get $50",
                        "Get Out of Jail Free",
                        "Go to Jail – Go directly to jail – Do not pass Go – Do not collect $200",
                        "Go back to Old Kent Road",
                        "Annuity matures. Collect $100",
                        "Income tax refund – Collect $20",
                        "It is your birthday — Collect $10 from each player",
                        "Pay a $10 fine or take a Chance",
                        "Pay hospital fees of $100",
                        "Receive interest on 7% preference shares: $25",
                        "Pay your insurance premium $50",
                        "You have won second prize in a beauty contest – Collect $10",
                        "You inherit $100"]

Bank_error = "Bank error in your favor — Collect $200"
Doctor = "Doctor's fee — Pay $50"
Stock = "From sale of stock you get $50"
Old_Kent = "Go back to Old Kent Road"
Annuity = "Annuity matures. Collect $100"
Income = "Income tax refund – Collect $20"
Birthday = "It is your birthday — Collect $10 from each player"
Fine = "Pay a $10 fine or take a Chance"
Hospital = "Pay hospital fees of $100"
Interest = "Receive interest on 7% preference shares: $25"
Insurance = "Pay your insurance premium $50"
Beauty = "You have won second prize in a beauty contest – Collect $10"
Inherit = "You inherit $100"

def shuffle():
    '''
    Shuffles chance and community decks
    '''
    while True:
        time.sleep(0.7)
        decision = str(input("Would you like to shuffle the chance and community chest cards? (Y/N) "))
        if  decision == "Y":
            time.sleep(1)
            print("Shuffling", end = "")
            time.sleep(1)
            for i in range(3):
                print(".", end = "")
                time.sleep(0.7)
            random.shuffle(community_chest_deck)    
            random.shuffle(chance_deck)
            print("\nYour cards have been shuffled... by Krammer.", end = "")
            time.sleep(1)
            print(" Don't be surprised if he wins.")
            return(chance_deck)
            return(community_chest_deck)
            break
        elif decision == "N":
            time.sleep(1)
            print("Why u tryna cheat??? Sus. Fined £200 for cheating.", end ="")
            time.sleep(2)
            print("jk ;)")
        else:
            time.sleep(1)
            print("Why you chatting WASS my G")


def GO():
    database['p1'][0] = 0
    print("You have landed on... ", end = " ")
    time.sleep(1)
    print(locations[database['p1'][0]], "!")
    time.sleep(1)
    print("$200 has been added to your bank account! ")
    database['p1'][1] += 200
    
def Jail():
    database['p1'][0] = 10
    print("You have landed on... ", end = " ")
    time.sleep(1)
    print(locations[database['p1'][0]], "!")
    time.sleep(1)
    Fine = input("Miss the next three goes or pay $50! Would you like to pay? Y/N ")
    if Fine == "Y":
        time.sleep(1)
        print("Thank you, $50 has been deducted from your account, you are free to go.")
        database['p1'][1] -= 50
    elif  Fine == "N":
        time.sleep(1)
        print("Skip the next three turns")
    else:
        time.sleep(1)
        print("So, you think you a sly boy huh? Pay $200, and skip the next three turns!")
        database['p1'][1] -= 200

def Pall_Mall():
    if database['p1'][0] <= 11:
        database['p1'][0] = 11
        print("You have landed on... ", end = " ")
        time.sleep(1)
        print(locations[database['p1'][0]], "!")
    elif database['p1'][0] > 11:
        database['p1'][0] = 11
        print("You have landed on... ", end = " ")
        time.sleep(1)
        print(locations[database['p1'][0]], "!")
        time.sleep(1)
        print("You also passed GO, and $200 has been added to your account")
        database['p1'][1] += 200
    
def Trafalgar():
    if database['p1'][0] <= 24:
        database['p1'][0] = 24
        print("You have landed on... ", end = " ")
        time.sleep(1)
        print(locations[database['p1'][0]], "!")
    elif database['p1'][0] > 24:
        database['p1'][0] = 24
        print("You have landed on... ", end = " ")
        time.sleep(1)
        print(locations[database['p1'][0]], "!")
        time.sleep(1)
        print("You also passed GO, and $200 has been added to your account")
        database['p1'][1] += 200


def Station():
    if database['p1'][0] <= 15:
        database['p1'][0] = 15
        print("You have landed on... ", end = " ")
        time.sleep(1)
        print(locations[database['p1'][0]], "!")
    elif database['p1'][0] > 15:
        database['p1'][0] = 15
        print("You have landed on... ", end = " ")
        time.sleep(1)
        print(locations[database['p1'][0]], "!")
        time.sleep(1)
        print("You also passed GO, and $200 has been added to your account")
        database['p1'][1] += 200
    
def Dividend():
    print("$50 has been added to your account")
    database['p1'][1] += 50
    balance()

def Back_3():
    print("You have been teleported back three spaces")
    database['p1'][0] -= 3
    balance()

def Speeding():
    print("$15 has been deducted from your account")
    database['p1'][1] -= 15
    balance()

def School():
    print("$150 has been deducted from your account")
    database['p1'][1] -= 150
    balance()

def Drunk():
    print("$20 has been deducted from your account")
    database['p1'][1] -= 20
    balance()
    
def Loan_matures():
    print("$150 has been added to your account")
    database['p1'][1] += 150
    balance()
    
def Crossword():
    print("$100 has been added to your account")
    database['p1'][1] += 100
    balance()
    
def Mayfair():
    database['p1'][0] = 39
    print("You have landed on... ", end = " ")
    print(locations[database['p1'][0]], "!")

def balance():
    time.sleep(1)
    print("You currently have... ", end = " ")
    time.sleep(1)
    print("$",database['p1'][1])

"""
Bank_error = "Bank error in your favor — Collect $200"
Doctor = "Doctor's fee — Pay $50"
Stock = "From sale of stock you get $50"
Old_Kent = "Go back to Old Kent Road"
Annuity = "Annuity matures. Collect $100"
Income = "Income tax refund – Collect $20"
Birthday = "It is your birthday — Collect $10 from each player"
Fine = "Pay a $10 fine or take a Chance"
Hospital = "Pay hospital fees of $100"
Interest = "Receive interest on 7% preference shares: $25"
Insurance = "Pay your insurance premium $50"
Beauty = "You have won second prize in a beauty contest – Collect $10"
Inherit = "You inherit $100"
"""

def Bank_error():
    time.sleep(1)
    print("$200 has been added to your account")
    database['p1'][1] += 200




Back_3()




