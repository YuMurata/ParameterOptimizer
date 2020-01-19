from abc import ABCMeta, abstractclassmethod
import typing



class BitDecoder(metaclass=ABCMeta):
    '''
    implement
    ---
    def decode(self, bit_list: list) -> Param
    '''
    @abstractmethod
    def decode(self, bit_list: list) -> Param:
        pass
