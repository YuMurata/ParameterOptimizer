import numpy as np
import os
import sys

sys.path.append(os.getcwd())
from ParameterOptimizer import DataGenerator


class SampleGenerator(DataGenerator):
    def generate(self, param: dict) -> dict:
        return param
