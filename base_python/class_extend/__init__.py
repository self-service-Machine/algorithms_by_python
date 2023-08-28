

class CC:
    def setXY(self, x, y):
        self.x = x
        self.y = y

    def printXY(self):
        print(self.x, self.y)


if __name__ == '__main__':
    c = CC()
    c.setXY(3,5)
    c.printXY()

    del CC

    c.printXY()