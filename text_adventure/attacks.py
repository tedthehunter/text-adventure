import random

class attack:
    def __init__(self, name, type, min_dmg, max_dmg):
        self.name = name
        self.type = type
        max_dmg += 1
        self.damage = range(min_dmg, max_dmg)

    def hit(self):
        print(f'You hit for {random.choice(self.damage)} {self.type} damage!')

    def test(self):
        print(self.name)
        print(self.type)
        print(self.damage)
        self.hit()
        print()


stab = attack('stab', 'piercing', 1, 6)
bash = attack('bash', 'crushing', 2, 8)
fireball = attack('fireball', 'fire', 6, 36)


stab.test()
bash.test()
fireball.test()