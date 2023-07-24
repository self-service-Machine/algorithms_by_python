# 对dict中相同key不同value数据处理

if __name__ == '__main__':
    good_id = [{'goods_id': 9, 'buy_num': 1.0}, {'goods_id': 8, 'buy_num': 8.0}, {'goods_id': 7, 'buy_num': 4.0},
               {'goods_id': 9, 'buy_num': 1.0}, {'goods_id': 3, 'buy_num': 1.0}, {'goods_id': 2, 'buy_num': 1.0},
               {'goods_id': 6, 'buy_num': 1.0}]
    # reverse=False 默认升序，reverse=True降序
    good_id.sort(key=lambda x: x["goods_id"], reverse=True)  # 对goods_id排序
    print("good_id==", good_id)
    from operator import itemgetter
    from itertools import groupby

    for id, va in groupby(good_id, key=itemgetter("goods_id")):
        data = {}
        sm = []
        key = None
        for i in va:
            key = i["goods_id"]  # 对goods_id相同的字段
            x = i["buy_num"]     # 对buy_num进行相加
            sm.append(x)

        data["goods_id"] = key
        data["buy_num"] = sum(sm)
        print("data===", data)
