def chr_to_hex(data):
    return hex(ord(data))
def data_to_bytes_arr(data):
    result = []
    data_in_16B_str_arr = []
    row_temp_arr=[]
    temp_hex_4x4_arr=[]
    for i in range(0,len(data),16):
        if len(data[i:i+16])==16:
            data_in_16B_str_arr.append(data[i:i+16])
        if len(data[i:i+16]) <16:
            diff = 16-len(data[i:i+16])
            data_with_padding= data[i:i+16] + str(" "*diff) 
            data_in_16B_str_arr.append(data_with_padding)
    for i in range(len(data_in_16B_str_arr)):
        for j in range(len(data_in_16B_str_arr[i])):
            row_temp_arr.append(chr_to_hex(data_in_16B_str_arr[i][j]))
            if len(row_temp_arr) == 4 :
                temp_hex_4x4_arr.append(row_temp_arr)
                row_temp_arr = []
            if len(temp_hex_4x4_arr) == 4 :
                result.append(temp_hex_4x4_arr)
                temp_hex_4x4_arr = []          
    return result   