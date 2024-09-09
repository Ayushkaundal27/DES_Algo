from cryptogrsphy_algorithms.des_functions import to_bineary


def data_splitter(data, size):
    data = to_bineary.to_bineary(data)
    length = int(len(data))
    divided_data = ""
    result = []
    data_chunk_size_in_bytes = size / 8
    for i in range(0, length, 8):
        divided_data = divided_data+data[i:i+8]
        if int(len(divided_data)/8) == data_chunk_size_in_bytes:
            result.append(divided_data)
            divided_data = ""
    if divided_data == "":
        return result
    if (len(divided_data) / 8) < data_chunk_size_in_bytes:
        remaining_size = len(divided_data) / 8
        padding = to_bineary.to_bineary(' ')
        while remaining_size < data_chunk_size_in_bytes:
            divided_data = divided_data + padding
            remaining_size = len(divided_data) / 8
    if divided_data != '':
        result.append(divided_data)
    return result


def data_splitter_4bits(data):
    data8bitArray = data_splitter(data, 8)
    result = []
    i = 0
    while i < len(data8bitArray):
        result.append(data8bitArray[i][0:4])
        result.append(data8bitArray[i][4:8])
        i = i + 1
    return result
