# 选择排序
def selection_sort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# 快速排序
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        # 基准值
        pivot = arr[0]
        # 比基准值小的子数组
        less = [i for i in arr[1:] if i <= pivot]
        # 比基准值大的子数组
        greater = [i for i in arr[1:] if i > pivot]
        # 递归调用
        return quick_sort(less) + [pivot] + quick_sort(greater)


# 希尔排序
def shell_sort(arr):
    import math
    gap = 1
    while(gap < len(arr) / 3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            current = arr[i]
            pre_index = i - gap
            while pre_index >= 0 and arr[pre_index] > current:
                arr[pre_index + gap] = arr[pre_index]
                pre_index -= gap
            arr[pre_index + gap] = current
        gap = math.floor(gap / 3)


# 冒泡排序
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        # j的范围是0到len(arr)-1-i
        for j in range(len(arr) - 1 - i):
            # 如果前一个数比后一个数大，则交换两个数
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 插入排序
def insertion_sort(arr):
    for i in range(1, len(arr)):
        # 当前需要排序的元素
        current = arr[i]
        # 从当前元素的前一个开始比较，如果比当前元素大，则将当前元素向后移动一位
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        # 将当前元素插入到合适的位置
        arr[pre_index + 1] = current