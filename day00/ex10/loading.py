import time
import sys
from decimal import Decimal


def ft_progress(lst):
    barLength = 20
    block = int(round(barLength*lst))
    x = Decimal.from_float(lst * 100)
    text = "\rPercent: [{0}] ".format("|"*block + " "*(barLength-block))
    sys.stdout.write(text + "%d" % x)
    sys.stdout.write("%")
    sys.stdout.flush()


for i in range(101):
    ft_progress(i/100)
    time.sleep(0.1)
