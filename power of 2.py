def powers_of_two(n: int):
    two_power = []
    counter = 0
    for counter in range(n + 1):
        power = 2 ** counter
        two_power.append(power)
    return two_power


n_str = input('Введіть число степеня: ')
n = int(n_str)

print(powers_of_two(n))
