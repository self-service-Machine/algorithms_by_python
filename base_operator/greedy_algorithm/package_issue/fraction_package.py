# 背包问题
"""
有限的空间尽可能多装

eg：
  商品1： v1=60,  w1=10
  商品2： v2=100, w2=20
  商品3： v3=120, w3=30

  背包容量：w=50

细分为0-1背包、分数背包
"""

# 表示（价格，重量）
goods = [(60, 10), (120, 30), (100, 20)]
goods.sort(key=lambda x: x[0]/x[1], reverse=True)


def fraction_backage(weight):
    """
    分数背包
    :param weight: 背包重量
    :return:
    """
    total = 0
    # 按照价格/重量 降序排序
    m = [0 for _ in range(len(goods))]
    for i, (price, w) in enumerate(goods):
        if weight > w:
            m[i] = 1
            total += price
        else:
            m[i] = weight / w
            w -= weight
            total += m[i] * price
            break
    return m


if __name__ == '__main__':
    fraction_backage(50)
