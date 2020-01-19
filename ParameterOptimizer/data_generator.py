from abc import ABCMeta, abstractmethod
import typing
from .bit_decoder import Param

Data = typing.NewType('Data', typing.Any)


class DataGenerator(metaclass=ABCMeta):
    '''
    implement
    ---
    def generate(self, param: Param) -> Data:
    '''
    @abstractmethod
    def generate(self, param: Param) -> Data:
        pass
