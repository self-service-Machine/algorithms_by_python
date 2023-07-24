# 假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，
# 前面 正好 有 ki 个身高大于或等于 hi 的人。
#
# 请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，
# 其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。
#
# 输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# 输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# 解释：
# 编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
# 编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
# 编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
# 编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
# 编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
# 编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
# 因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。



# 1 <= people.length <= 2000
# 0 <= hi <= 106
# 0 <= ki < people.length
# 题目数据确保队列可以被重建

# 输入：people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# 输出：[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

if __name__ == '__main__':

    # test = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    test = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

    # 位置和item标记
    index_dict = {}
    # 身高和位置map
    high_index_map = {}
    # 位置和身高map
    index_high_map = {}

    # 身高和位置map
    index_num = 0

    # 身高数组
    high_list = []
    # 遍历数组
    for item in test:
        index_dict[index_num] = item

        #  todo 相同key的情况下，后面的会覆盖前面的
        high_index_map[item[0]] = index_num
        index_high_map[index_num] = item[0]
        high_list.append(item[0])
        index_num += 1

    # 对身高进行排序 (从小到大)
    high_list.sort(reverse=True)

    # 将数组按high排序
    dd = []

    # 将test数组按身高排序
    for ee in high_list:
        dd.append(index_dict[high_index_map[ee]])
    mm = []
    dd_len = dd.__len__()
    # 再按照ki插入数组
    # 对比指针
    a = 0
    # 数组长度指针
    v = 0
    for ddd in range(dd_len):
        # 表示小的需要加载数组首部
        if dd[ddd][1] == 0:
            mm.insert(0, dd[ddd])
        # 不为0的需要插入到指定位置
        else:
            mm.insert(dd[ddd][1], dd[ddd])
        v += 1
            # 需要对比下和前一个的ki
            # if dd[ddd][0]
    # for ddd in range(dd_len):
    #     t = dd[dd[ddd][1]]
    #     dd[dd[ddd][1]] = dd[ddd]
    #     dd[ddd] = t
    #     pass
        # print(dd[len(dd) - ddd - 1])
        # print(ddd)
    #     # ddd 为数组下标
    #

    print(dd)

    print(mm)

# [[7, 1], [7, 1], [6, 1], [5, 2], [5, 2], [4, 4]]
# [[7, 1], [6, 1], [5, 2], [5, 2], [4, 4], [7, 1]]
# [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]