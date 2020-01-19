from abc import ABCMeta, abstractmethod
import typing


class PredictModel(metaclass=ABCMeta):
    @abstractmethod
    def predict(self, data: typing.Any) -> float:
        pass
