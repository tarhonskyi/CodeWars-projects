import time
from math import sqrt


def gen_area(start, stop):
    start = start
    while 1:
        if start < stop:
            yield start
            start += 1


def mult_area(area):
    mult = []
    if area == 1:
        return [1]
    for i in range(int(area**0.5) - 1, area + 1):  # обычно делитель не будет больше корня
        while area % i == 0:  # while, а не if
            mult.append(i)
            area //= i
    return mult



def minimum_perimeter(area):
    h = w = int(sqrt(area))
    while 1:
        if h * w == area:
            return 2 * h + 2 * w
        else:
            h += 1
            w = int(area / h)


start_time = time.time()
for i in gen_area(5, 100):
    print(mult_area(i), i)

print("--- %s mseconds ---" % ((time.time() - start_time) * 1000))