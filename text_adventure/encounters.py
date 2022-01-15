

import random


class npc:
    def __init__(self, name, health, weakness):
        self.name = name
        self.health = health
        self.weakness = weakness

    def talk(self):
        print(self.name)

    def attack(self):
        print(f'The {self.name} attacks you!')

    def test(self):
        print(self.name)
        print(f'HP: {self.health}')
        print(f'Weakness: {self.weakness}')
        print()


class encounter:
    def __init__(self, npc_list, diff):
        self.npc_list = npc_list
        self.diff = diff

    def appear(self):
        print(f'You have encounterd a {(random.choice(self.npc_list)).name}.')


goblin = npc('Goblin', 50, ':Light')
troll = npc('Troll', 100, 'Acid')
fire_elemental = npc('Fire Elemental', 125, "Water")


basic = encounter([goblin,troll,fire_elemental],5)


basic.appear()