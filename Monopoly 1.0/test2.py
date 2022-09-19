# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:35:55 2021

@author: 4664
"""

'''
a = {1: 0.0, 2: 0}

for i in a:
    if isinstance(a[i], float) == True:
        print(i)
        
'''
'''
for i, j in [['a', 'b'], [1,2]]:
    print(i)
    print(j)
    
a = 0
[a := a + i for i in range(10)]
print(a)
'''
'''
b = {1: 0,
     2: 0}

b[1] = 0.0

print(b)
'''


'''
ans = input("Enter your choice in the format 1,2,3 ")

int = 0
choice = []

for i in ans:
    if i == " ":
        print("Don't include spaces")
        break
    elif i.isnumeric():
        if int == 1:
            print("must separate numbers with ,")
            break
        int = 1
        choice.append(i)
    elif i == ",":
        if int == 0:
            print("invalid input")
        int = 0
    else:
        print("invalid input")
        break
    
print(choice)

if len(choice) > 3:
    print("You cannot buy more than 3 houses at a time")
  '''  
'''
if all(i > 2 for i in [1,2,3]) == False:
    print("yes")
    '''
for i in range(3):
    print(i)