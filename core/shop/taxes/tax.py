from abc import ABCMeta, abstractmethod


class Tax(metaclass=ABCMeta):
    def __init__(self):
        self._rate

    @property
    @abstractmethod
    def rate(self):
        pass



