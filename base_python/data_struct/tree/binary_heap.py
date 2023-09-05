class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    # 节点根据大小换位
    def perc_up(self, i):
        # 判断其有无父节点
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    # 新增节点
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    # 构建堆
    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            # 对比当前节点和其较小的子节点大小
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    # 获取子节点中小的那个
    def min_child(self, i):
        # 判断是否有右子节点
        if i * 2 + 1 > self.current_size:
            # 无右子节点，返回左子节点
            return i * 2
        # 有右子节点
        else:
            # 从左右两个子节点中取较小的那个
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # 移除最小元素
    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval


if __name__ == '__main__':
    bh = BinaryHeap()
    bh.insert(5)
    bh.insert(8)
    bh.insert(3)
    bh.insert(11)
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
