"""
类的内置方法
"""


class D:
    pass


class B(D):
    pass


class V:
    pass


class C:
    def __init__(self, x):
        self.x = x


class E:
    def __init__(self, size=10):
        self.size = size

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def del_size(self):
        del self.size

    # property() 返回一个可以设置属性的属性
    y = property(get_size, set_size, del_size)


if __name__ == '__main__':
    # 判断第一个元素是否为第二个元素的子类
    print(issubclass(B, D))
    print(issubclass(B, V))

    # 第一个参数是否为第二个参数的实例对象
    b = B()
    print(isinstance(b, B))
    print(isinstance(b, D))
    print(isinstance(b, V))
    # print(isinstance(B, D))
    # print(issubclass(B, V))

    # 判断该实例是否有某属性名
    c = C('test')
    print(hasattr(c, 'x'))
    # 返回某属性名的属性值
    print(getattr(c, 'x'))

    # 设置对象中的属性值，属性不存在时会新建属性并赋值
    setattr(c, 'y', 'ssss')
    setattr(c, 'x', 'eeee')
    print(c.__dict__)

    # 删除对象的某属性
    delattr(c, 'y')

    dd = E()
    print(dd.y)
    dd.y = 12
    del dd.y
    print(dd.__dict__)


