from cryptogrsphy_algorithms.des_functions import data_combiner
from cryptogrsphy_algorithms.des_functions import key_transformation


def round_key_generation(key):
    key_56_bit = key_transformation.tranform_key_des_56_bit(key)
    key_left = key_56_bit[:28]
    key_right = key_56_bit[28:]
    round_key_array = []
    shift = [
        1, 1, 2, 2,
        2, 2, 2, 2,
        1, 2, 2, 2,
        2, 2, 2, 1]
    for i in range(0, 16):
        swiftedkey = ""
        key_left = key_left[shift[i]:] + key_left[:shift[i]]
        key_right = key_right[shift[i]:] + key_right[:shift[i]]
        swiftedkey = data_combiner.strCombiner(key_left, key_right)
        key_48_bit = key_transformation.tranform_key_des_48_bit(swiftedkey)
        round_key_array.append(key_48_bit)
    return round_key_array
