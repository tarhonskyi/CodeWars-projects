def count_vegetables(string):
    vegs = "cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"
    veg_set = set(string.split())
    veg_count = []
    for veg in veg_set:
        if veg in vegs:
            veg_count.append((string.count(veg), veg))
    veg_count.sort(reverse=True)
    return veg_count


s1 = 'potato tofu cucumber cabbage turnip pepper onion carrot celery mushroom potato tofu cucumber cabbage'

lst_1 = count_vegetables(s1)
print(lst_1)
