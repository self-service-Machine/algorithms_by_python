# 代理模式
from abc import ABCMeta, abstractmethod


class ReceiveParcel(metaclass=ABCMeta):
    self.__name = None

    def get_name(self):
        return self.__name


    @abstractmethod
    def receive(self, parcel):
        pass


class Tony(ReceiveParcel):
    def __init__(self, name, phone):
        super().__init__(name)
        self.__phone = phone

    def get_phone(self):
        return self.__phone

    def receive(self, parcel):
        print('快递员 {0} 送来一个包裹，签收人是 {1}'.format(self.get_name(), self.get_name()))
