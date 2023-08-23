"""
单向队列

使用数组实现队列，通过在数组第一个index添加元素和pop()最后一个index实现队列先进先出
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# 队列模拟击鼓传花
def hot_potato(name_list, num):
    simqueue = Queue()
    for name in name_list:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


if __name__ == '__main__':
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
