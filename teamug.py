class Teamug:
    """There is a mug filled with tea"""

mymug=Teamug()

mymug.color="green"
mymug.size="24 ounces"  #the amount in the cup
mymug.shape="square"
mymug.amount=24 #integer version of amount in the cup

import math

def tea_drinking_simulation(minutes):
    tea_left= mymug.amount-.5*minutes      #you can drink half an ounce in one minute
    print(tea_left)


tea_drinking_simulation(45)
