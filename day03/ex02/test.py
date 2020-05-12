import numpy
from ScrapBooker import ScrapBooker
scbook = ScrapBooker()

array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', 'L',
         'B', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', 'L',
         'C', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', 'L',
         'D', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', 'L',
         'E', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', 'L',
         'F', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', 'L',
         'G', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', 'L',
         'H', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', 'L',
         'I', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', 'L',
         'J', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', 'L',
         'Q', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', 'L']

array = numpy.reshape(array, (11, 12))
array = numpy.array(array)
print("Array")
print(array)
x = scbook.crop(array, (5, 3), (0, 2))
print("\nCroped array(dimensions(5,3), position(0,2))")
print(x)
x = scbook.thin(array, 3, 0)
print("\nThined array(n=3, axis=0)")
print(x)
x = scbook.juxtapose(array, 1, 1)
print("\nJuxtaposed array(n=1, axis=1)")
print(x)
x = scbook.mosaic(array, (1, 1))
print("\nMosaic array(1x1)")
print(x)
