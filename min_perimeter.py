import time
from math import sqrt


def gen_area(stop):
    start = 1
    while 1:
        if start < stop:
            yield start
            start += 1


def minimum_perimeter(area):
    h = w = int(area**0.5)
    while 1:
        if h * w == area:
            return 2 * h + 2 * w
        else:
            h += 1
            w = int(area / h)


num = 5 * 10**10

start_time = time.time()

print(minimum_perimeter(num))

print("--- %s mseconds ---" % ((time.time() - start_time) * 1000))



