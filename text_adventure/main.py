
import random

class attack:
    def __init__(self, name, type, min_dmg, max_dmg):
        self.name = name
        self.type = type
        max_dmg += 1
        self.damage = range(min_dmg, max_dmg)

    def hit(self):
        x = random.choice(self.damage)
        print(f'You hit for {x} {self.type} damage!')
        return x


    def test(self):
        print(self.name)
        print(self.type)
        print(self.damage)
        self.hit()
        print()


class npc:
    def __init__(self, name, health, weakness, dmg):
        self.name = name
        self.health = health
        self.weakness = weakness
        self.dmg = range(1,dmg)

        def getname(self):
            return self.name
        def gethealth(self):
            return self.health
        def getweakness(self):
            return self.weakness
        def getdmg(self):
            return self.dmg

        def setname(self, newname):
            self.name = newname
        def sethealth(self, newhealth):
            self.health = newhealth
        def setweakness(self, newweakness):
            self.weakness = newweakness
        def dmg(self, newdmg):
            self.dmg = newdmg

    def talk(self):
        print(f'A {self.name} has appeared.')

    def attack(self):
        x = random.choice(self.dmg)
        print(f'The {self.name} attacks you and deals {x} damage!')

    def test(self):
        print(self.name)
        print(f'HP: {self.health}')
        print(f'Weakness: {self.weakness}')
        print()


class player:
    def __init__(self, health, attack_list):
        self.health = health
        self.attack_list = attack_list

    def player_attack(self):
        print('Choose your attack:')
        x = 0
        for attack in self.attack_list:
            x += 1
            print(f'({x}) {attack.name}')
        y = int(input())
        (self.attack_list[(y-1)]).hit()
        return y-1



class encounter:
    def __init__(self, enemy_combatants, player_combatants):
        self.enemy_combatants = enemy_combatants
        self.player_combatants = player_combatants

    def combat(self):
        #initiative = random.choice(True,False)
        #if initiative == True:
        (self.player_combatants).player_attack()
        (self.enemy_combatants).sethealth(5)#((self.enemy_combatants).gethealth()-(self.player_combatants).player_attack(y)))
        (self.enemy_combatants).attack()







kick = attack('Kick', 'bludgeoning', 1, 3)
stab = attack('Stab', 'piercing', 1, 6)
fireball = attack('Fireball','fire', 6, 12)
longbow = attack('Longbow', 'piercing', 1, 8)


available_attacks = [kick,stab,fireball,longbow]


hero = player(100,available_attacks)


goblin = npc('goblin', 25, 'light', 6)
troll = npc('troll', 50, 'fire', 12)
npc_list = [goblin]


testfight = encounter(goblin,hero)


testfight.combat()