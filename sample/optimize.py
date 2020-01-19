import numpy as np
import os
import sys

from bit_decoder import SampleDecoder
from data_generator import SampleGenerator
from predict_model import SampleModel

sys.path.append(os.getcwd())
from ParameterOptimizer import Optimizer


if __name__ == "__main__":
    param, logbook = \
        Optimizer(SampleModel(), SampleGenerator(),
                  SampleDecoder()).optimize(30)

    print(param)
