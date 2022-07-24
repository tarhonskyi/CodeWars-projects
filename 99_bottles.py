def sing():
    first_str = "{} bottle{} of beer on the wall, {} bottle{} of beer."
    second_str = "Take one down and pass it around, {} bottle{} of beer on the wall."
    final = ["Take one down and pass it around, no more bottles of beer on the wall.",
             "No more bottles of beer on the wall, no more bottles of beer.",
             "Go to the store and buy some more, 99 bottles of beer on the wall."]
    song = []
    bottles = 99
    end = "s"
    while True:
        if bottles == 0:
            song.pop()
            song += final
            return song
        song.append(first_str.format(bottles, end, bottles, end))
        if bottles - 1 == 1:
            end = ""
        song.append(second_str.format(bottles - 1, end))
        bottles -= 1


print(sing()[199])