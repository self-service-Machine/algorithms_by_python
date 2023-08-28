# 贪心算法   --   找零问题
# 有很多张纸币，面值有100元、50元、20元、5元和1元面值，用最小纸币张数找零

# 纸币面额
denomination = [100, 50, 20, 5, 1]


def change(target):
    """
    :param target: 目标金额
    :return:
    """
    # 创建一个和纸币面额列表元素个数相同的列表
    m = [0 for _ in range(len(denomination))]
    # enumerate() 函数，返回index, index_val
    for i, money in enumerate(denomination):
        # 计算当前面值纸币需要张数
        m[i] = target // money
        # 计算余数(除去当前面额外剩余找零金额)
        target = target % money

    return m, target


if __name__ == '__main__':
    print(change(371))



