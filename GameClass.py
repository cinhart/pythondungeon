from Entities import*

def choosedifficulty():
    print("Choose a difficulty\n1) Easy peasy\n2) Normal\n3) Hardly hard")
    while(True):
        i=input("")
        if i=="1": #easy
            return 1
        elif i=="2": #normal
            return 2
        elif i=="3": #hard
            return 3
        else:
            print("Please choose a valid option")

## GAME CLASS

class game():
    def __init__(self):
        print("\nStarting new game...\n")
        self.difficulty = choosedifficulty()
        p = init_player()
        self.player = p
        self.roomcount=0
        self.mobcount=0
        self.potioncount=0
    def showstats(self):
        print("\n----------\nFinal game stats\n----------")
        print(str(self.roomcount)+" rooms explored")
        print(str(self.mobcount)+" monsters encountered")
        print(str(self.potioncount)+" potions drunk")
        print("GG!")