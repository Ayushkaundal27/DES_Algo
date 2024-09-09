from Cryptodome.Cipher import DES3
from binascii import unhexlify,hexlify
def hex_to_chr(data):
    temp = ""
    for i in range(0,len(data),2):
        temp = temp  + chr(int(data[i:i+2],16))
    return temp
def chr_to_hex(data):
    temp = ""
    for i in range(0,len(data)):
        print(hex(ord(data[i])))
    return temp  
key = unhexlify('9ec2372c86379df4')+unhexlify('ad7ac4464f73805d')+unhexlify('20c4f87564527c91')
print(key)
k1 = hex_to_chr('b624d6bd41783ab1')
cipher = DES3.new(key, DES3.MODE_ECB)
msg = cipher.encrypt(unhexlify("b624d6bd41783ab1"))
print(msg)
print(unhexlify('8d64960bfb34b096'))