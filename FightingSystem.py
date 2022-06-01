from Entities import*

import time

## TURNS SYSTEM

def playerturn(player, entity):
    print("What do you want to do ?\n1) Attack\n2) Spe Attack\n3) Randomise Critical Probabilities\n4) Run")
    while(True):
        i=input("")
        if i=="1":
            return player.attack(entity)
        elif i=="2":
            return player.speattack(entity)
        elif i=="3":
            player.A=uniformrand(10)
            player.B=uniformrand(10)
            print("Something just changed, you can feel it")
            return 0
        elif i=="4":
            return player.run(entity)
        else:
            print("Please choose a valid option")

def enemyturn(player, entity):
    entity.attack(player)

## MAIN FUNCTION

def fight(player, entity):
    turncount=1
    while(True):
        print("\n\n----------\nTurn: "+str(turncount)+"\n----------")
        time.sleep(1)
        player.showhp()
        entity.showhp()
        print("----------")
        time.sleep(1)
        playerturn(player, entity)
        if not(entity.isdead()==False):
            print("\n"+entity.name+" is dead! GG!")
            del entity
            return "Win"
        time.sleep(1)
        entity.attack(player)
        if not(player.isdead()==False):
            print("\nOh no, you're dead! Better luck next time")
            return "Loss"
        time.sleep(1)
        turncount+=1