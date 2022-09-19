# -*- coding: utf-8 -*-
"""
@author: TitanKronoz

"""

import time
import random

min = 1
max = 6

print("You have rolled...")
time.sleep(2)
roll_1 = random.randint(min, max)
roll_2 = random.randint(min, max)
print(roll_1, " and ", roll_2)
time.sleep(2)
print("Please advance ", (roll_1 + roll_2), " spaces")