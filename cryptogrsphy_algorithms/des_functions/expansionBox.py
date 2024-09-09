from cryptogrsphy_algorithms.des_functions import data_dividing


def expansion(data):
    Data4bitChunk = data_dividing.data_splitter_4bits(data)
    for i in range(0, len(Data4bitChunk)):
        index = (i + 1) % len(Data4bitChunk)
        t1 = Data4bitChunk[i][len(Data4bitChunk[i]) - 1]
        t2 = Data4bitChunk[index][0]
        Data4bitChunk[i] = Data4bitChunk[i] + t2
        Data4bitChunk[index] = t1 + Data4bitChunk[index]
    return Data4bitChunk
