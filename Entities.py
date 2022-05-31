import time

## GENERAL ENTITY CLASS

class entity:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.strength = 0
        self.agility = 0
        self.focusing = 0
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
    def attack(self, entity): ###DEAL POISSON LAW DAMAGE + PROBILITY OF DODGING
        print(self.name+" attack "+entity.name)
        damage = self.strength
        print(entity.name+" just lost "+str(damage)+" hp")
        entity.hp -= damage



## PLAYER CLASS

class player(entity):
    pass
    def __init__(self, name): ###GENERATE RANDOM STATS
        self.name = name
        self.hp = 100
        self.maxhp = self.hp
        self.strength = 10
        self.agility = 10
        self.focusing = 5
        self.level = 1
        self.xp = 0
    def showstats(self):
        super().showstats()
        print("level: "+str(self.level)+" ("+str(self.xp)+" xp)")
    def speattack(self, entity):
        print(self.name+" use a special attack on "+entity.name)
        damage = self.strength*2
        print(entity.name+" just lost "+str(damage)+" hp")
        entity.hp -= damage
    def run(self, entity):
        print(entity.name+" did not let you run")


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
        self.name = "Serpython"
        self.hp = 50
        self.maxhp = self.hp
        self.strength = 5
        self.agility = 10
        self.focusing = 10

class enemy2(entity):
    pass
    def __init__(self):
        self.name = "Turboa"
        self.hp = 20
        self.maxhp = self.hp
        self.strength = 10
        self.agility = 50
        self.focusing = 25

class enemy3(entity):
    pass
    def __init__(self):
        self.name = "Abradacobra"
        self.hp = 100
        self.maxhp = self.hp
        self.strength = 20
        self.agility = 10
        self.focusing = 50

def spawn_enemy(): ###RANDOM ENNEMY
    e = enemy1()
    print("\nA wild "+e.name+" appeared!")
    time.sleep(1)
    print("Let's fight it!")
    time.sleep(2)
    return e