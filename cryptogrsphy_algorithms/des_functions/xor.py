def xor_with_key(d1, d2):
    x = 0
    for i in range(0, len(d1)):
        temp = ''
        for j in range(0, len(d1[i])):
            ans = int(d1[i][j]) ^ int(d2[x])
            temp = temp+str(ans)
            x = x + 1
        d1[i] = temp
    return d1


def xor_two_str(d1, d2):
    temp = ''
    for i in range(0, len(d2)):
        temp = temp + str(int(d1[i]) ^ int(d2[i]))
    return temp
