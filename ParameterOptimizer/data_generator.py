from abc import ABCMeta, abstractclassmethod
import typing
from .bit_decoder import Param

Data = typing.NewType('Data', typing.Any)


class DataGenerator(metaclass=ABCMeta):
    @abstractclassmethod
    def generate(self, param: Param) -> Data:
        pass
