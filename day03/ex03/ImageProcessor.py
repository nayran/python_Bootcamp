import matplotlib.pyplot as mp
import matplotlib.image as mi
import numpy


class ImageProcessor:
    def __init__(self):
        pass

    @staticmethod
    def load(path):
        image = mi.imread(path)
        print(f"Loading {len(image[0])}x{len(image)} image")
        return numpy.array(image)

    @staticmethod
    def display(array):
        mp.imshow(array)
        mp.show()
