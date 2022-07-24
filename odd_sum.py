def row_sum_odd_numbers(n):
    from math import factorial
    quantity = factorial(n)

    num = 1
    odds = {}

    for num_in_raw in range(1, n + 1):
        for i in range(num_in_raw):
            if i == 0:
                odds[num_in_raw] = 0
            odds[num_in_raw] += num
            num += 2
    return odds[n]


print(row_sum_odd_numbers(41))
