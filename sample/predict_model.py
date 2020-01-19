import numpy as np
import os
import sys

sys.path.append(os.getcwd())
from ParameterOptimizer import PredictModel
from config import TargetValue


class SampleModel(PredictModel):
    def predict(self, data: dict) -> float:
        max_part_diff = -abs(data['max_part'] - TargetValue.MAX)
        min_part_diff = -abs(data['min_part'] - TargetValue.MIN)
        return max_part_diff + min_part_diff
