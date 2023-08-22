"""
双端队列 python实践和应用解决问题

"""


class DoubleEndedQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # 在队列头部添加元素
    def add_front(self, item):
        self.items.append(item)

    # 在队列尾部添加元素
    def add_rear(self, item):
        self.items.insert(0, item)

    # 移除头一个元素
    def remove_front(self):
        return self.items.pop()

    # 移除最后一个元素
    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# 回文方法
def pal_check(a):

    chardeque = DoubleEndedQueue()
    # 将字符串尾插法加入队列
    for ch in a:
        chardeque.add_rear(ch)

    still_equal = True

    while chardeque.size() > 1 and still_equal:
        first = chardeque.remove_front()
        last = chardeque.remove_rear()
        if first != last:
            still_equal = False

    return still_equal


if __name__ == '__main__':

    # 测试回文
    print(pal_check("d2d33d2d"))
