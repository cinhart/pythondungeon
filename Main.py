from ExplorationFunctions import *
from GameClass import *

import numpy
import time

def launchGame():
    g = game()
    while(g.player.isdead()==False):
        g.roomcount+=1
        print("\n----------\nROOM "+str(g.roomcount)+"\n----------")
        exploreroom(g)
    g.showstats()

launchGame()

