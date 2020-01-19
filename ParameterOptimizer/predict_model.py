from abc import ABCMeta, abstractmethod
from PIL.Image import Image


class PredictModel(metaclass=ABCMeta):
    @abstractmethod
    def predict(self, image: Image) -> float:
        pass
