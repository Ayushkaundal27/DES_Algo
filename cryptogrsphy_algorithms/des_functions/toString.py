from cryptogrsphy_algorithms.des_functions import data_dividing


def toString(data):
    result = ""
    data8bitChunkArray = data_dividing.data_splitter(data, 8)
    for i in range(0, len(data8bitChunkArray)):
        temp = chr(int(data8bitChunkArray[i], 2))
        result = result + temp
    return result
