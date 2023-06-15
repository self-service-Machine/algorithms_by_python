# 系统函数
from itertools import count

# __call__ 用于实例化对象后，直接调用对象，而不是调用对象的方法
# __hash__ 用于获取对象的哈希值
# __repr__ 用于获取对象的描述信息
# __slots__ 用于限制对象可以绑定的属性
# __init__ 用于初始化对象
# __main__ 用于判断模块是否是主模块
# __name__ 用于获取模块的名字
# __bool__ 用于判断对象的布尔值
# __reduce__ 用于序列化对象
# __dict__ 用于获取对象的属性字典
# __str__ 用于获取对象的字符串描述
# __format__ 用于获取对象的格式化字符串
# __getattribute__ 用于获取对象的属性
# __getattr__ 用于获取对象的属性
# __setattr__ 用于设置对象的属性
# __delattr__ 用于删除对象的属性
# __dir__ 用于获取对象的属性列表
# __len__ 用于获取对象的长度
# __getitem__ 用于获取对象的元素
# __setitem__ 用于设置对象的元素
# __delitem__ 用于删除对象的元素
# __iter__ 用于获取对象的迭代器
# __reversed__ 用于反转对象
# __contains__ 用于判断对象是否包含某个元素
# __missing__ 用于获取字典中不存在的元素
# __enter__ 用于进入上下文管理器
# __exit__ 用于退出上下文管理器
# __next__ 用于获取迭代器的下一个元素
# __index__ 用于获取对象的索引
# __copy__ 用于复制对象
# __deepcopy__ 用于深度复制对象
# __eq__ 用于判断对象是否相等
# __ne__ 用于判断对象是否不相等
# __lt__ 用于判断对象是否小于
# __le__ 用于判断对象是否小于等于
# __gt__ 用于判断对象是否大于
# __ge__ 用于判断对象是否大于等于
# __add__ 用于获取对象的加法结果
# __sub__ 用于获取对象的减法结果
# __mul__ 用于获取对象的乘法结果
# __floordiv__ 用于获取对象的整除结果
# __truediv__ 用于获取对象的除法结果
# __mod__ 用于获取对象的取模结果
# __pow__ 用于获取对象的幂运算结果
# __lshift__ 用于获取对象的左移结果
# __rshift__ 用于获取对象的右移结果
# __and__ 用于获取对象的按位与结果
# __or__ 用于获取对象的按位或结果
# __xor__ 用于获取对象的按位异或结果
# __radd__ 用于获取对象的反向加法结果
# __rsub__ 用于获取对象的反向减法结果
# __rmul__ 用于获取对象的反向乘法结果
# __rfloordiv__ 用于获取对象的反向整除结果
# __rtruediv__ 用于获取对象的反向除法结果


# @property 用于将方法转换为属性


class SystemFunctions:
    _counter = count()
    __slots__ = ("func", "priority", "location", "definition")

    @property
    def counter(self):
        return self._counter


if __name__ == '__main__':
    system_client = SystemFunctions()
    print(system_client.counter)
