from ProbaFunctions import*

import time

## GENERAL ENTITY CLASS

class entity:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.strength = 0
        self.agility = 0
        self.focusing = 0
        self.A=0
        self.B=0
    def showstats(self):
        print("\n----------\n"+self.name+"'s stats\n----------")
        print("hp: "+str(self.hp)+"/"+str(self.maxhp))
        print("strength: "+str(self.strength))
        print("agility: "+str(self.agility))
        print("focusing: "+str(self.focusing))
    def showhp(self):
        print(self.name+"'s hp: "+str(self.hp)+"/"+str(self.maxhp))
    def isdead(self):
        if(self.hp<=0):
            return True
        return False
    def attack(self, entity):
        print(self.name+" attack "+entity.name)
        r = kuramaswamyrand(entity.A,entity.B)
        damage=self.strength
        damage = round(bornedcauchyrand(damage))
        if (r + self.focusing/100 > 1.3): #critical attack
            print(r + self.focusing/100)
            damage = int(damage * r *2)
            print("Critical hit !")
        if bernouillirand(0.9 - self.agility/50): #dodge
            print(entity.name+" just lost "+str(damage)+" hp")
            entity.hp -= damage
        else:
            print ("Dodged !")



## PLAYER CLASS

class player(entity):
    pass
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hp = math.floor(triangrand(80,150,100))
        self.maxhp = self.hp
        self.strength = math.floor(triangrand(8,15,10))
        self.agility = math.floor(triangrand(8,15,10))
        self.focusing = math.floor(triangrand(8,15,10))
        self.level = 1
        self.xp = 0
        self.tired = False
    def showstats(self):
        super().showstats()
        print("level: "+str(self.level)+" ("+str(self.xp)+" xp)")
    def speattack(self, entity):
        if (bernouillirand(0.5 + self.focusing/50)):
            print(self.name+" use a special attack on "+entity.name)
            damage = int(self.strength*2)
            print(entity.name+" just lost "+str(damage)+" hp")
            entity.hp -= damage
        else:
            print("It failed...")
    def run(self, entity):
        print("You can't run, where are you supposed to go?")


def init_player():
    print("Now, let's build your character! ")
    p = player(input("Enter your character's name : "))
    print("Nice! Here are your stats:")
    p.showstats()
    input("\npress Enter to continue...")
    return p



## ENEMIES CLASSES

class enemy1(entity):
    pass
    def __init__(self):
        super().__init__()
        self.name = "Serpython"
        self.hp = math.floor(triangrand(20,60,50))
        self.maxhp = self.hp
        self.strength = math.floor(triangrand(5,15,8))
        self.agility = math.floor(triangrand(5,20,10))
        self.focusing = math.floor(triangrand(8,15,10))

class enemy2(entity):
    pass
    def __init__(self):
        super().__init__()
        self.name = "Turboa"
        self.hp = math.floor(triangrand(15,25,20))
        self.maxhp = self.hp
        self.strength = math.floor(triangrand(5,12,10))
        self.agility = math.floor(triangrand(40,70,50))
        self.focusing = math.floor(triangrand(20,50,25))

class enemy3(entity):
    pass
    def __init__(self):
        super().__init__()
        self.name = "Abradacobra"
        self.hp = math.floor(triangrand(15,25,20))
        self.maxhp = self.hp
        self.strength = math.floor(triangrand(15,25,20))
        self.agility = math.floor(triangrand(5,20,10))
        self.focusing = math.floor(triangrand(30,60,40))

def spawn_enemy(): #Spawn a random enemy (uniform)
    r=uniformrand(3)
    if r==1:
        e = enemy1()
    elif r==2:
        e = enemy2()
    elif r==3:
        e = enemy3()
    print("\nA wild "+e.name+" appeared!")
    time.sleep(1)
    print("Let's fight it!")
    input("\npress Enter to continue...")
    return e