import os,cryptogrsphy_algorithms.triple_des as triple_des
file_name = input("Enter file name : ")
file =  open(os.path.dirname(os.path.abspath(__file__))+'\\triple_des_testcases\\'+file_name,'r')
file_content = file.readlines()
number_of_testcase = 0
def chr_to_hex(data):
    temp = ""
    for i in range(0,len(data)):
        t1=str(hex(ord(data[i]))).replace("0x","")
        temp =temp+t1
    return temp  
def hex_to_chr(data):
    temp = ""
    for i in range(0,len(data),2):
        temp = temp  + chr(int(data[i:i+2],16))
    return temp
key_1 = ""
key_2 = ""
key_3 = ""
plain_text = ""
cipher_text = ""
count_encrypt_testcase = 0
count_decrypt_testcase = 0
encryption_decryption_switch = -1
for i in range(len(file_content)):
    current_line = file_content[i]
    if current_line.find('[ENCRYPT]')==0:
         encryption_decryption_switch = 0
    if current_line.find('[DECRYPT]')==0:
         encryption_decryption_switch = 1
    if current_line.find('COUNT')==0:
        current_line = current_line.replace("COUNT = ","")
        number_of_testcase = number_of_testcase+1
    if current_line.find('KEY1')==0:
        key_1 = current_line.replace("KEY1 = ","").strip()
    if current_line.find('KEY2')==0:
        key_2 = current_line.replace("KEY2 = ","").strip()
    if current_line.find('KEY3')==0:
        key_3 = current_line.replace("KEY3 = ","").strip()
    if current_line.find('PLAINTEXT')==0:
        plain_text = current_line.replace("PLAINTEXT = ","").strip()
    if current_line.find('CIPHERTEXT')==0:
        cipher_text = current_line.replace("CIPHERTEXT = ","").strip()
    if (cipher_text !="") & (plain_text !=""):
        if encryption_decryption_switch == 0 :
            result = triple_des.triple_des_encryption(plain_text,key_1,key_2,key_3)
            print("Testcase " + str(number_of_testcase)+" of encryption\n")
            print("Output of Triple DES : ",chr_to_hex(result),"\n")
            print("Desired output : ",cipher_text,"\n")
            if(result==hex_to_chr(cipher_text)):
                count_encrypt_testcase=count_encrypt_testcase+1
            print("Passed testcase "+str(count_encrypt_testcase)+"/"+str(number_of_testcase))    
            plain_text=""
            cipher_text=""
        if encryption_decryption_switch == 1 :
            result = triple_des.triple_des_decryption(cipher_text,key_1,key_2,key_3)
            print("Testcase " + str(number_of_testcase)+" of decryption\n")
            print("Output of Triple DES : ",chr_to_hex(result),"\n")
            print("Desired output : ",plain_text,"\n")
            if(result==hex_to_chr(plain_text)):
                count_decrypt_testcase=count_decrypt_testcase+1
            print("Passed testcase "+str(count_decrypt_testcase)+"/"+str(number_of_testcase))    
            plain_text=""
            cipher_text=""        
file.close()            