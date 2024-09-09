import sys,os
path=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1,path+"\\aes_functions")
import to_bytes_convertion

def encrytion(data,key):
    print(len(data))
    data_divided_in_128_bits = to_bytes_convertion.data_to_bytes_arr(data)
    print(data_divided_in_128_bits[1])
encrytion("ayushayushayuaaaa","")  