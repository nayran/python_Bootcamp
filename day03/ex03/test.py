from ColorFilter import ColorFilter
from ImageProcessor import ImageProcessor

imp = ImageProcessor()
cf = ColorFilter()

arr = imp.load("./image.png")
x = cf.invert(arr)
imp.display(x)

arr = imp.load("./image.png")
x = cf.to_red(arr)
imp.display(x)

arr = imp.load("./image.png")
x = cf.to_blue(arr)
imp.display(x)

arr = imp.load("./image.png")
x = cf.to_green(arr)
imp.display(x)

arr = imp.load("./image.png")
x = cf.celluloid(arr)
imp.display(x)
