import re


def to_bineary(data):
    c = re.compile('[^01]')
    if len(c.findall(data)):
        bineary_data = ''.join(format(ord(i), '08b') for i in data)
        return bineary_data
    return data
