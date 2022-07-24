def wallpaper(l, w, h):
    numbers = ["zero", "one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine", "ten",
               "eleven", "twelve", "thirteen", "fourteen", "fifteen",
               "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
               ]
    square = (l + w) * 2 * h * 1.15
    num_of_rolls = square / 0.52 / 10
    if (num_of_rolls % 1) > 0:
        number_of_rolls = (num_of_rolls // 1) + 1
    elif num_of_rolls < 0:
        number_of_rolls = 0
    else:
        number_of_rolls = num_of_rolls // 1

    if l == 0 or w == 0 or h == 0:
        number_of_rolls = 0
    rolls = numbers[int(number_of_rolls)]
    return rolls


print(wallpaper(3, 5, 2.5))
