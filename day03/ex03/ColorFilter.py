import numpy


class ColorFilter:
    def __init__(self):
        pass

    @staticmethod
    def invert(array):
        return 1 - array

    @staticmethod
    def to_blue(array):
        img = numpy.zeros(array.shape)
        img[:, :, 2] = array[:, :, 2]
        return img

    @staticmethod
    def to_green(array):
        img = array
        img[:, :, 2] *= 0
        img[:, :, 0] *= 0
        return img

    @staticmethod
    def to_red(array):
        img = array
        img -= ColorFilter().to_blue(array)
        img -= ColorFilter.to_green(array)
        return img
