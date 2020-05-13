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
        img = array * [0, 1, 0]
        return img

    @staticmethod
    def to_red(array):
        img = array
        img -= ColorFilter.to_blue(array)
        img -= ColorFilter.to_green(array)
        return img

    @staticmethod
    def celluloid(array):
        thres = int(input('Give threshold number: '))
        img = array * 255
        img = numpy.uint8(img)
        for ext in img:
            for colors in ext:
                threshold = 256 // thres
                for index, val in enumerate(colors):
                    for i in range(thres):
                        if threshold * i <= val < threshold * (i + 1):
                            colors[index] &= threshold * i
        return img
