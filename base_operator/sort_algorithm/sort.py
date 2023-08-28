def heap_sort(alist):
    if alist is None or len(alist) == 0:
        return
    length = len(alist)
    output = []
    for i in range(length):
        temp_len = len(alist)
        for j in range(temp_len//2-1, -1, -1):
            pre_index = j
            pre_val, heap = alist[pre_index], False
            while 2 * pre_index < temp_len - 1 and not heap:
                cur_index = 2 * pre_index + 1
                if cur_index < temp_len - 1:
                    if alist[cur_index] < alist[cur_index+1]:
                        cur_index += 1
                if pre_val >= alist[cur_index]:
                    heap = True
                else:
                    alist[pre_index] = alist[cur_index]
                    pre_index = cur_index
            alist[pre_index] = pre_val
        output.insert(0, alist.pop(0))
    return output


if __name__ == '__main__':
    test = [2, 6, 5, 9, 10, 3, 7]
    aa = heap_sort(test)
    print()
