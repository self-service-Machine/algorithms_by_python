class StackObj:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def pop(self):
        self.items.pop()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items - 1)]

    def size(self):
        return len(self.items)


#  利用栈来判断左右括号是否数量相等
def par_check(symbol_string):
    tmp_stack = StackObj()
    blanced = True
    index = 0
    while index < len(symbol_string) and blanced:
        symbol = symbol_string[index]
        if symbol == '(':
            tmp_stack.push(symbol)
        else:
            if tmp_stack.is_empty():
                blanced = False
            else:
                tmp_stack.pop()
        index += 1

    if blanced and tmp_stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    print(par_check('((()()))(())'))

