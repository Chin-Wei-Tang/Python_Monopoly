# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:32:55 2021

@author: leost
"""

import time

p1 = str()
p1_empty = True
p2 = str()
p2_empty = True
p3 = str()
p3_empty = True
p4 = str()
p4_empty = True
done = False

while done == False:
    if p1_empty == True:
        name = str(input("Welcome to Monopoly! Please enter your name: "))
        time.sleep(2)
        print("Hey, ", name, ". Nice to meet you!")
        p1 += name
        p1_empty = False
        time.sleep(1)
    elif p2_empty == True:
        name = str(input("Welcome to Monopoly! Please enter your name: "))
        time.sleep(2)
        print("Hey, ", name, ". Nice to meet you!")
        p2 += name
        p2_empty = False
        time.sleep(1)
    elif p3_empty == True:
        name = str(input("Welcome to Monopoly! Please enter your name: "))
        time.sleep(2)
        print("Hey, ", name, ". Nice to meet you!")
        p3 += name
        p3_empty = False
        time.sleep(1)
    elif p4_empty == True:
        name = str(input("Welcome to Monopoly! Please enter your name: "))
        time.sleep(2)
        print("Hey, ", name, ". Nice to meet you!")
        p4 += name
        p4_empty = False
        time.sleep(1)
    else:
        done = True
        
