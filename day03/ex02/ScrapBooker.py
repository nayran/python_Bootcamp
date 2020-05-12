import numpy


class ScrapBooker:
    def __init__(self):
        pass

    @staticmethod
    def crop(array, dimensions, position=(0, 0)):
        dx = dimensions[1]
        dy = dimensions[0]
        px = position[1]
        py = position[0]
        if dx > len(array[0]) or dy > len(array):
            raise ValueError("Dimensions are larger than current array")
        array = array[px:px+dx, py:py+dy]
        return numpy.array(array)

    @staticmethod
    def thin(array, n, axis):
        return numpy.delete(numpy.array(array), n, axis=axis)

    @staticmethod
    def juxtapose(array, n, axis):
        i = 0
        while(i < n):
            array = numpy.concatenate((array, array), axis=axis)
            i += 1
        return array

    @staticmethod
    def mosaic(array, dimensions):
        array = ScrapBooker.juxtapose(array, dimensions[1], 1)
        array = ScrapBooker.juxtapose(array, dimensions[0], 0)
        return array
