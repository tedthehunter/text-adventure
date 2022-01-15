

class npc:
    def __init__(self, name, health, weakness):
        self.name = name
        self.health = health
        self.weakness = weakness

    def talk(self):
        print(f'A {self.name} has appeared.')

    def attack(self):
        print(f'The {self.name} attacks you!')

    def test(self):
        print(self.name)
        print(f'HP: {self.health}')
        print(f'Weakness: {self.weakness}')
        print()

goblin = npc('Goblin', 50, ':Light')
troll = npc('Troll', 100, 'Acid')
fire_elemental = npc('Fire Elemental', 125, "Water")


goblin.test()
troll.test()
fire_elemental.test()