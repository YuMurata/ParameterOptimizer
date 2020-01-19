import numpy as np
import os
import sys
from config import TargetValue

sys.path.append(os.getcwd())
from ParameterOptimizer import BitDecoder


class SampleDecoder(BitDecoder):
    def decode(self, bit_list: list) -> dict:
        max_part_list, min_part_list = np.split(np.array(bit_list), 2)

        def to_dec(bit_part_list: np.array):

            bin_str = ''.join(map(str, bit_part_list.tolist()))
            dec = int(bin_str, 2)
            normalize = TargetValue.normalize(dec)
            return normalize

        return {
            'max_part': to_dec(max_part_list),
            'min_part': to_dec(min_part_list),
        }
