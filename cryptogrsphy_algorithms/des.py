from cryptogrsphy_algorithms.des_functions import permutation
from cryptogrsphy_algorithms.des_functions import data_dividing
from cryptogrsphy_algorithms.des_functions import expansionBox
from cryptogrsphy_algorithms.des_functions import sBoxCompression
from cryptogrsphy_algorithms.des_functions import xor
from cryptogrsphy_algorithms.des_functions import toString
from cryptogrsphy_algorithms.des_functions import round_key_generation
from cryptogrsphy_algorithms.des_functions import data_combiner


def encryption(data, key):
    for i in range(8-len(key)):
        key = key + " "
    if len(key) > 8:
        key = key[:8]
    data_64_bit = data_dividing.data_splitter(data, 64)
    xor_keyay = round_key_generation.round_key_generation(key)
    result = ""
    for i in range(len(data_64_bit)):
        initial_permutation = permutation.initial_permutation(data_64_bit[i])
        left_half = initial_permutation[:32]
        right_half = initial_permutation[32:]
        for j in range(0, 16):
            expanded_data = expansionBox.expansion(right_half)
            xor_key = xor.xor_with_key(expanded_data, xor_keyay[j])
            sbox_compressed_result = sBoxCompression.sbox_compression(xor_key)
            straight_permu = permutation.straight_permu(sbox_compressed_result)
            xor_with_left_half = xor.xor_two_str(left_half, straight_permu)
            left_half = right_half
            right_half = xor_with_left_half
        final_result = data_combiner.strCombiner(right_half, left_half)
        final_pernutation = permutation.final_permutation(final_result)
        final_cipher = toString.toString(final_pernutation)
        print(final_cipher)
        result = result + final_cipher
    return result


def decryption(data, key):
    for i in range(8 - len(key)):
        key = key + " "
    if len(key) > 8:
        key = key[:8]
    data_64_bit = data_dividing.data_splitter(data, 64)
    xor_keyay = round_key_generation.round_key_generation(key)
    result = ""
    for i in range(len(data_64_bit)):
        initial_permutation = permutation.initial_permutation(data_64_bit[i])
        left_half = initial_permutation[:32]
        right_half = initial_permutation[32:]
        for j in range(0, 16):
            expanded_data = expansionBox.expansion(right_half)
            xor_key = xor.xor_with_key(expanded_data, xor_keyay[15-j])
            sbox_compressed = sBoxCompression.sbox_compression(xor_key)
            straight_permu = permutation.straight_permu(sbox_compressed)
            xor_with_left_half = xor.xor_two_str(left_half, straight_permu)
            left_half = right_half
            right_half = xor_with_left_half
        final_result = data_combiner.strCombiner(right_half, left_half)
        final_pernutation = permutation.final_permutation(final_result)
        final_cipher = toString.toString(final_pernutation)
        result = result + final_cipher
    return result
