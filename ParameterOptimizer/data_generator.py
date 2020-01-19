from abc import ABCMeta, abstractclassmethod
import typing


class DataGenerator(metaclass=ABCMeta):
    @abstractclassmethod
    def generate(self, param: typing.Any) -> typing.Any:
        pass
