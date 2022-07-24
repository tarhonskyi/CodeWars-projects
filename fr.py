import time

number = 5 * 10**10


def minimum_perimeter(area):
    compare = area ** 0.5
    for i in range(int(area ** 0.5), area+1):
        if area % i == 0 and i >= compare:
            j = int(area / i)
            prmtr = 2 * i + 2 * j
            break

    return prmtr

start_time = time.time()
print(minimum_perimeter(number))
print("--- %s mseconds ---" % ((time.time() - start_time) * 1000))