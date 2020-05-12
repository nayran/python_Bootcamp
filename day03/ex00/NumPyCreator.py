import numpy
import random


def error(x):
    raise ValueError(x)


def tester(arg, instance, ret):
    if ret == "array":
        if isinstance(arg, instance):
            return numpy.array(arg)
        error("Parameter list required")


class NumPyCreator:
    def __init__(self):
        pass

    @staticmethod
    def from_list(lst):
        return tester(lst, list, 'array')

    @staticmethod
    def from_tuple(tpl):
        return tester(tpl, tuple, 'array')

    @staticmethod
    def from_iterable(itr):
        return numpy.array(itr)

    @staticmethod
    def from_shape(shape, value=0):
        y = shape[0]
        x = shape[1]
        total = y * x
        a = []
        aux = 0
        while(aux < total):
            a.append(value)
            aux += 1
        return numpy.reshape(a, (y, x))

    @staticmethod
    def random(shape):
        y = shape[0]
        x = shape[1]
        total = y * x
        a = []
        aux = 0
        while(aux < total):
            a.append(random.random())
            aux += 1
        return numpy.reshape(a, (y, x))

    @staticmethod
    def identity(n):
        return numpy.identity(n)
