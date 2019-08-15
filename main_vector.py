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

    zero = Vector.zero(2)
    print("zero 2 = {} ".format(zero))

    norm_vec = Vector([3, 4])
    print('norm({})  = {}'.format(norm_vec, norm_vec.norm()))

    print('normalize({})  = {}   and  its  norm = {}'.format(norm_vec, norm_vec.normalize(),norm_vec.normalize().norm()))
