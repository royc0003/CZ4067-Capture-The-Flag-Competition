# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)

import random

key = 'ntu'
strr = '218,118,52,87,81,92,71,84,205,30,245,195,215,16,160,250,0,120,172,42,227,222,144,227,208,123,231,255,162,86,148,217'

def func1(str1, key):
    random.seed(key)
    str2 = ''
    for c in str1:
        str2 += str(ord(c) ^ random.randint(0, 255)) + ','

    str2 = str2.strip(',')
    return str2


def func2(str2, key):
    random.seed(key)
    str1 = ''
    for i in str2.split(','):
        i = int(i)
        n = random.randint(0, 255)
        str1 += chr(i ^ n)
        print(n)

    return str1

print(func2(strr,key))