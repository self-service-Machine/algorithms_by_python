from abc import ABCMeta, abstractmethod


class Persion:
    def __init__(self, name, dayoff, reason):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__leader = None

    def get_name(self):
        return self.__name

    def get_day_off(self):
        return self.__dayoff

    def get_reason(self):
        return self.__reason

    def set_leader(self, leader):
        self.__leader = leader

    def request(self):
        print('{0} 申请请假 {1} 天， 事由: {2}'.format(self.__name, self.__dayoff, self.__reason))
        if self.__leader is not None:
            self.__leader.handle_request(self)


class Manger(metaclass=ABCMeta):
    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self._next_handler = None

    def get_name(self):
        return self.__name

    def get_title(self):
        return self.__title

    def set_next_handler(self, handler):
        self._next_handler = handler

    @abstractmethod
    def handle_request(self, request):
        pass


class Supervisor(Manger):

    def __init__(self, name, title):
        super().__init__(name, title)

    def handle_request(self, persion):
        if persion.get_day_off() <= 2:
            print('主管 {0} 批准 {1} 的请假申请'.format(self.get_name(), persion.get_name()))
        else:
            print('主管 {0} 无法处理，交由经理处理'.format(self.get_name()))
            self._next_handler.handle_request(persion)


class DepartmentManger(Manger):

    def __init__(self, name, title):
        super().__init__(name, title)

    def handle_request(self, persion):
        if (persion.get_day_off() >= 2) and persion.get_day_off() <= 5:
            print('经理 {0} 批准 {1} 的请假申请'.format(self.get_name(), persion.get_name()))
        else:
            print('经理 {0} 无法处理，交由总经理处理'.format(self.get_name()))
            self._next_handler.handle_request(persion)


class GeneralManger(Manger):
    def __init__(self, name, title):
        super().__init__(name, title)

    def handle_request(self, persion):
        if 5 < persion.get_day_off() <= 22:
            print('总经理 {0} 批准 {1} 的请假申请'.format(self.get_name(), persion.get_name()))
        else:
            print('总经理 {0} 无法处理，交由行政部门处理'.format(self.get_name()))
        if self._next_handler is not None:
            self._next_handler.handle_request(persion)


class Administrator(Manger):
    def __init__(self, name, title):
        super().__init__(name, title)

    def handle_request(self, persion):
        if persion.get_day_off() > 22:
            print('行政部门 {0} 批准 {1} 的请假申请'.format(self.get_name(), persion.get_name()))


if __name__ == '__main__':
    directLeader = Supervisor('Eren', '客户端研发经理')
    departmentLeader = DepartmentManger('Levi', '客户端研发部门经理')
    generalLeader = GeneralManger('Erwin', '技术总监')
    admin = Administrator('Hanji', '行政部门')
    directLeader.set_next_handler(departmentLeader)
    departmentLeader.set_next_handler(generalLeader)
    generalLeader.set_next_handler(admin)

    summy = Persion('Summy', 1, '参加婚礼')
    summy.set_leader(directLeader)
    summy.request()

    tony = Persion('Tony', 5, '有急事')
    tony.set_leader(directLeader)
    tony.request()

    pony = Persion('Pony', 30, '出国旅游')
    pony.set_leader(directLeader)
    pony.request()

