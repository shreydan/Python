"""
Written by: Shreyas Daniel - github.com/shreydan
Description: Rolls dice with ability to select the number of dice.
"""

import random

class dice(object):
    
    def __init__(self,dicenum):
        self.dicenum = dicenum

 
    def roll(self):
        roll_list = []
        for i in range(self.dicenum):
            roll_list.append(random.randint(1,6))
        
        return roll_list

        
obj = dice(2) # change the number of dice here
rolls = obj.roll()

for r in rolls:
    print (r,end=' ')
    
print()
