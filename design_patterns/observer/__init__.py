from abc import abstractmethod, ABCMeta


class Observer(metaclass=ABCMeta):
    """
    观察者的基类
    """
    @abstractmethod
    def update(self, observable, *args, **kwargs):
        pass


class Observer:
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def nodify_observers(self, *args, **kwargs):
        for observer in self.__observers:
            observer.update(self, *args, **kwargs)