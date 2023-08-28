import random as r

"""
单一继承
"""


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print('当前位置: ({},{})'.format(self.x, self.y))


class Glodfish(Fish):
    pass


class Carp(Fish):
    pass


class Slamon(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hurgry = True

    def eat(self):
        if self.hurgry:
            print("eat fish")
            self.hurgry = False
        else:
            print("not hurgry")


if __name__ == '__main__':
    # 创建普通小鱼
    fish = Fish()
    fish.move()

    goldfish = Fish()
    goldfish.move()

    shark = Shark()
    shark.eat()
    shark.eat()

    shark.move()
