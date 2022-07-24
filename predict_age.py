def predict_age(*ages):
    mult_ages = 0
    for age in ages:
        mult_ages += age * age
    return int(mult_ages ** 0.5 / 2)


print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))
