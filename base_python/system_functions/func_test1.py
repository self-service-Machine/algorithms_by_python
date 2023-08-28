class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


if __name__ == '__main__':
    c = CapStr("testAAAA")
    print(c)

    c.__del__()
    print(c)
