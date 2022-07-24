def rake_garden(garden: str):
    garden_list = garden.split(" ")
    for key, item in enumerate(garden_list):
        if not (item == "rock" or item == "gravel"):
            garden_list[key] = "gravel"
    garden = " ".join(garden_list)
    return garden


garden_1 = 'slug spider rock gravel gravel gravel gravel gravel gravel gravel'

print(rake_garden(garden_1))
