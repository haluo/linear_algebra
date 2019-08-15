# coding: utf-8
'''
@author: jessezhu
@file: main_vector.py
@time: 2019/8/15 2:46 PM
@desc:

'''
from la.vector import Vector

if __name__ == '__main__':
    vector = Vector([1, 2, 3])
    print("vector={}".format(vector))
    print('vector[0]={},vector[1]={}'.format(vector[0], vector[1]))
    vector2 = Vector([1, 2, 3])
    print("{}+{}={}".format(vector, vector2, vector + vector2))
    print("{}-{}={}".format(vector, vector2, vector - vector2))

    print("{}*{}={}".format(vector, 3, vector * 3))
    print("{}*{}={}".format(3, vector, 3 * vector))

    print("+{}={}".format(vector, +vector))
    print("-{}={}".format(vector, -vector))
