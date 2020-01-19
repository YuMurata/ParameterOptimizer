from abc import ABCMeta, abstractmethod
import typing

Param = typing.NewType('Param', typing.Any)


class BitDecoder(metaclass=ABCMeta):
    '''
    implement
    ---
    def decode(self, bit_list: list) -> Param
    '''
    @abstractmethod
    def decode(self, bit_list: list) -> Param:
        pass
