from abc import ABCMeta, abstractmethod


class Request:
    def __init__(self, name, day_off, reason):
        self.__name = name
        self.__day_off = day_off
        self.__reason = reason
        self.__leader = None

    def get_name(self):
        return self.__name

    def get_reason(self):
        return self.__reason

    def get_day_off(self):
        return self.__day_off

    def get_reason(self):
        return self.__reason


class Responsible(metaclass=ABCMeta):
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

    def handle_request(self, request):
        self.handle_request(request)
        if self._next_handler is not None:
            self._next_handler.handle_request(request)

    @abstractmethod
    def _handle_request_impl(self, request):
        pass
