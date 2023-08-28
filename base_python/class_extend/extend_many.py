"""
支持多重继承
"""


class Base1:
    def foo1(self):
        print("foo1, Base1")


class Base2:
    def foo2(self):
        print("foo2, Base2")


class Ctest(Base1, Base2):
    pass


if __name__ == '__main__':
    c = Ctest()
    c.foo1()
    c.foo2()
