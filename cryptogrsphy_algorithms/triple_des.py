from cryptogrsphy_algorithms import des


def hex_to_chr(data):
    temp = ""
    for i in range(0, len(data), 2):
        temp = temp + chr(int(data[i:i+2], 16))
    return temp


def chr_to_hex(data):
    temp = ""
    for i in range(0, len(data)):
        print(hex(ord(data[i])))
    return temp


def triple_des_encryption(data, k1, k2, k3):
    data = hex_to_chr(data)
    k1 = hex_to_chr(k1)
    k2 = hex_to_chr(k2)
    k3 = hex_to_chr(k3)
    step_1 = des.encryption(data, k1)
    step_2 = des.decryption(step_1, k2)
    step_3 = des.encryption(step_2, k3)
    return step_3


def triple_des_decryption(data, k1, k2, k3):
    data = hex_to_chr(data)
    k1 = hex_to_chr(k1)
    k2 = hex_to_chr(k2)
    k3 = hex_to_chr(k3)
    step_1 = des.decryption(data, k1)
    step_2 = des.encryption(step_1, k2)
    step_3 = des.decryption(step_2, k3)
    return step_3
