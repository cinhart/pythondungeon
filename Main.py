from Entities import *
from FightingSystem import*

import random
import numpy
import time

def exploreroom(player): ###GENERATE RANDOM ROOM (ENNEMY/SUPPLY/EMPTY)
    e = spawn_enemy() ###SPAWN RANDOM ENEMIES
    fight(player,e)
    time.sleep(1)
    print("There's nothing else in this room, we should get going.")
    input("\npress Enter to continue...")


def launchGame():
    p = init_player()
    roomcount = 0
    while(p.isdead()==False):
        roomcount+=1
        print("\n----------\nROOM "+str(roomcount)+"\n----------")
        exploreroom(p)
    print("Your explored "+str(roomcount)+" rooms, GG!")

launchGame()

