from cryptogrsphy_algorithms.des_functions import to_bineary


def tranform_key_des_56_bit(Key):
    key_in_bineary = to_bineary.to_bineary(Key)
    pc1_table = [
        57, 49, 41, 33, 25, 17, 9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15, 7, 62, 54, 46, 38,
        30, 22, 14, 6, 61, 53, 45, 37,
        29, 21, 13, 5, 28, 20, 12, 4
        ]
    key_56_bit = "".join(key_in_bineary[position-1] for position in pc1_table)
    return key_56_bit


def tranform_key_des_48_bit(Key):
    pc2_table = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
        ]
    key_conv_into_48_bit = "".join(Key[position-1] for position in pc2_table)
    return key_conv_into_48_bit
