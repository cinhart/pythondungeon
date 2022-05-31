from Entities import *
from FightingSystem import*

import numpy
import time

def changetiredness(player):
    if(player.tired==False):
        print("You feel tired all of a sudden...")
        player.tired=True
    elif(player.tired==True):
        print("You don't feel tired anymore!")
        player.tired=False

def checktiredness(player, difficulty):
    if player.tired==False:
        if difficulty==1: #easy
            r = binomialrand(0.05)
        elif difficulty==2: #normal
            r = binomialrand(0.1)
        elif difficulty==3: #hard
            r = binomialrand(0.3)
    elif player.tired==True:
        if difficulty==1: #easy
            r = binomialrand(0.8)
        elif difficulty==2: #normal
            r = binomialrand(0.5)
        elif difficulty==3: #hard
            r = binomialrand(0.5)
    if(r==1):
        changetiredness(player)

def exploreroom(player, difficulty): ###GENERATE RANDOM ROOM (ENNEMY/SUPPLY/EMPTY)
    checktiredness(player, difficulty)
    e = spawn_enemy()
    fight(player,e)
    time.sleep(1)
    if player.isdead()==False:
        print("There's nothing else in this room, we should get going.")
        input("\npress Enter to continue...")

def choosedifficulty():
    print("Choose a difficulty\n1) Easy peasy\n2) Normal\n3) Hardly hard")
    while(True):
        i=input("")
        if i=="1":
            return 1
        elif i=="2":
            return 2
        elif i=="3":
            return 3
        else:
            print("Please choose a valid option")

def launchGame():
    difficulty = choosedifficulty()
    p = init_player()
    roomcount = 0
    while(p.isdead()==False):
        roomcount+=1
        print("\n----------\nROOM "+str(roomcount)+"\n----------")
        exploreroom(p, difficulty)
    print("Your explored "+str(roomcount)+" rooms, GG!")

launchGame()

