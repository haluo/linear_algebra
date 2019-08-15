# coding: utf-8
'''
@author: jessezhu
@file: vector.py
@time: 2019/8/15 2:26 PM
@desc:

'''
import math
from ._global import EPSILON

class Vector(object):
    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        """零向量"""
        return cls([0] * dim)

    def __str__(self):
        return "({})".format(",".join(str(i) for i in self))

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __getitem__(self, item):
        """vec[i]"""
        return self._values[item]

    def __len__(self):
        """长度"""
        return len(self._values)

    def __iter__(self):
        """可遍历"""
        return self._values.__iter__()

    def __add__(self, other):
        """向量相加"""
        assert len(self) == len(other), 'Length of vectors must be same.'
        return Vector([i + k for i, k in zip(self, other)])

    def __sub__(self, other):
        """向量相减"""
        assert len(self) == len(other), 'Length of vectors must be same.'
        return Vector([i - k for i, k in zip(self, other)])

    def __mul__(self, k):
        """乘法"""
        return Vector([i * k for i in self])

    def __rmul__(self, k):
        """右乘"""
        return self * k

    def __pos__(self):
        """取正"""
        return 1 * self

    def __neg__(self):
        """取负"""
        return -1 * self

    def __truediv__(self, k):
        """除法"""
        return self * (1 / k)

    def norm(self):
        """向量的模"""
        return math.sqrt(sum(i ** 2 for i in self))

    def normalize(self):
        """单位向量"""
        if self.norm() < EPSILON:
            raise ZeroDivisionError('norm is zero')
        return Vector(self._values) / self.norm()
