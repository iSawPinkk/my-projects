class Monster:
    def __init__(self, hp):
        self.hp = hp
class Player:
    def __init__(self, name, level,exp,hp):
        self.level = level
        self.exp = exp
        self.name = name
        self.hp = hp

import random as rd
import time as tm
monster=Monster((rd.randint(5,10))*100)
Player=Player(input('name:'),1,0,1000)
damage=0
kit=0
def wait():
    tm.sleep(0.2)
    print("-" * 40)
while Player.hp>0:
    wait()
    print("choose a way to attack")
    choice=int(input('attack(0) or rush(1):  '))
    random=rd.choice([0,1])
    if choice==0:
        damage=rd.randint(10,15)*10
    else:
        damage=random*rd.randint(20,25)*10
    wait()
    if damage>monster.hp:
        wait()
        print("You beat the monster!")
        kit += 1
        print("kit left:" + str(kit))
        if int(input("Before next round, do you want to use the first aid kit(+hp)? (0,1) :  ")) == 1:
            kit -= 1
            Player.hp += int(Player.hp * rd.randint(2, 5) * 0.1)
        print("player hp: " + str(Player.hp))
        print("You're ready for next round")
        print("Monster just spawned!")
        monster = Monster((rd.randint(5, 10)) * 100)
    else:
        print(str(Player.name)+" dealt monster "+str(damage)+" points of damage!")
        monster.hp-=damage
    print("player hp: "+str(Player.hp))
    print("Monster's hp: "+str(monster.hp))




    wait()
    print("choose a way to defend")
    choice = int(input('defend(0) or counter attack(1):  '))
    random = rd.choice([0, 1])
    if random^choice == 0:
        damage = 0
    else:
        damage =rd.randint(10,20)*10
    if damage>Player.hp:
        damage=Player.hp
    wait()
    print( "Monster dealt " +str(Player.name) +" "+str(damage) + " points of damage!")
    Player.hp-=damage
    print("player hp: " + str(Player.hp))
    print("Monster's hp: " + str(monster.hp))


print("="*40)
print("You lost")















































































































































































































































































































































































































































#by Ryan Lin