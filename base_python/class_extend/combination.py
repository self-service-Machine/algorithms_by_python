# 组合多个类
class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print('{} fish and {} turtle in the pool'.format(self.fish.num, self.turtle.num))


if __name__ == '__main__':
    pool = Pool(19, 3)
    pool.print_num()
