# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 13:59:13 2021

@author: leost

Next steps:
    actually performing the cards by using the existing functions
"""

import random
import time
#import itertools


chance_deck = ["Advance to Go! (Collect $200)",
               "Go to Jail. (Go directly to jail)",
               "You have been elected Chairman of the Board – Pay each player $50",
               "Advance to Illinois Ave - If you pass Go, collect $200",
               "Advance to St. Charles Place – If you pass Go, collect $200"
               "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.",
               "Advance token to the nearest Railroad and pay owner twice the rental to which he/she {he} is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.",
               "Bank pays you dividend of $50",
               "Get Out of Jail Free",
               "Go Back 3 Spaces",
               "Make general repairs on all your property–For each house pay $25 – For each hotel $100",
               "Pay poor tax of $15",
               "Take a trip to Reading Railroad – If you pass Go, collect $200",
               "Take a walk on the Boardwalk – Advance token to Boardwalk",
               "Your building and loan matures — Collect $150",
               "You have won a crossword competition — Collect $100"]


community_chest_deck = ["Advance to Go (Collect $200)",
                        "Bank error in your favor — Collect $200",
                        "Doctor's fee — Pay $50",
                        "From sale of stock you get $50",
                        "Get Out of Jail Free",
                        "Go to Jail–Go directly to jail–Do not pass Go – Do not collect $200",
                        "Grand Opera Night—Collect $50 from every player for opening night seats",
                        "Holiday Fund matures — Receive $100",
                        "Income tax refund – Collect $20",
                        "It is your birthday — Collect $10",
                        "Life insurance matures – Collect $100",
                        "Pay hospital fees of $100",
                        "Pay school fees of $150",
                        "Receive $25 consultancy fee",
                        "You are assessed for street repairs – $40 per house – $115 per hotel",
                        "You have won second prize in a beauty contest – Collect $10",
                        "You inherit $100"]

#valid = True
def shuffle():
    #global valid
    while True:
        decision = str(input("Would you like to shuffle the cards? (Y/N) "))
        if  decision == "Y":
            time.sleep(1)
            print("Shuffling", end = "")
            time.sleep(1)
            for i in range(3):
                print(".", end = "")
                time.sleep(1)
            random.shuffle(community_chest_deck)    
            random.shuffle(chance_deck)
            print("\nYour cards have been shuffled!")
            return(chance_deck)
            return(community_chest_deck)
            break
            #valid = True
        elif decision == "N":
            time.sleep(1)
            print("Why u tryna cheat??? Sus")
            time.sleep(1)
            #valid = False
        else:
            time.sleep(1)
            print("Why you chatting WASS my G")
            #valid = False

def chance_pick():
    #if valid == True:
    time.sleep(1)
    print("You picked...")
    time.sleep(1)
    print(chance_deck[0])
    chance_deck.append(chance_deck[0])
    chance_deck.remove(chance_deck[0])
        
def community_chest_pick():
    #if valid == True:
    time.sleep(1)
    print("You picked...")
    time.sleep(1)
    print(community_chest_deck[0])
    community_chest_deck.append(community_chest_deck[0])
    community_chest_deck.remove(community_chest_deck[0])

shuffle()
community_chest_pick()
community_chest_pick()