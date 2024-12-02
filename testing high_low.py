#init checking 
#high low card simulator
#tie to user

import random

def card():
    card=random.randint(1,13)
    return card

def result(user,comp,bid):
    if user==comp:
        note="Win"
    
    elif bid=="high" and user >comp:
        note="Win"
    elif bid=="low" and user <comp:
        note="Win"
    
    else:
        note="Lose"
    return note


#main    
while True:
    user_card,comp_card = card(),card()
    print("user:",user_card,"comp:",comp_card)

    user_bid = input("high or low: ")
    print(result(user_card,comp_card,user_bid))
    repeat = input("play again?")
    if repeat in ("x","n"):
        break
    else:
        True