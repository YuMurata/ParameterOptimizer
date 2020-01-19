from abc import ABCMeta, abstractmethod
from .data_generator import Data


class PredictModel(metaclass=ABCMeta):
    '''
    implement
    ---
    def predict(self, data: Data) -> float:
    '''
    @abstractmethod
    def predict(self, data: Data) -> float:
        pass
