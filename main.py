import cryptogrsphy_algorithms.des as des


def main():
    while 1:
        choose_algo = input("Enter algo name : ")
        if choose_algo == "":
            print("please  enter valid algo name")
        else:
            break
    data = input("Enter data to be encrypted : ")
    key = input("Enter key : ")
    if choose_algo.lower() == "des":
        encrypted_data = des.encryption(data, key)
        decrypted_data = des.decryption(encrypted_data, key)
        print("Encrypted Data : " + encrypted_data)
        print("Dencrypted Data : " + decrypted_data)


main()
