from Entities import *
from FightingSystem import *
from GameClass import *

import time

def changetiredness(player):
    if(player.tired==False):
        print("You feel tired all of a sudden...")
        player.strength*=0.9
        player.agility*=0.9
        player.focusing*=0.9
        player.tired=True
    elif(player.tired==True):
        print("You don't feel tired anymore!")
        player.strength*=1.1
        player.agility*=1.1
        player.focusing*=1.1
        player.tired=False

def checktiredness(player, difficulty):
    if player.tired==False:
        if difficulty==1: #easy
            r = bernouillirand(0.05)
        elif difficulty==2: #normal
            r = bernouillirand(0.1)
        elif difficulty==3: #hard
            r = bernouillirand(0.3)
    elif player.tired==True:
        if difficulty==1: #easy
            r = bernouillirand(0.8)
        elif difficulty==2: #normal
            r = bernouillirand(0.5)
        elif difficulty==3: #hard
            r = bernouillirand(0.5)
    if(r==1):
        changetiredness(player)

def exploreroom(game): ###GENERATE RANDOM ROOM (ENNEMY/SUPPLY/EMPTY)
    checktiredness(game.player, game.difficulty)
    event = nonuniformrand3(0.2-0.05*game.difficulty,0.7+0.05*game.difficulty)
    if event==1:
        print("You find a health potion!")
        game.potioncount+=1
        game.player.hp+= int(0.25*game.player.maxhp)
    elif event==2:
        e = spawn_enemy()
        game.mobcount+=1
        fight(game.player,e)
    time.sleep(1)
    if game.player.isdead()==False:
        print("There's nothing left to see in this room, we should get going.")
        input("\npress Enter to continue...")