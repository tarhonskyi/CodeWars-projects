def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2


n = int(input('Перша квітка '))
m = int(input('Друга квітка '))

print('Are you in love?', lovefunc(n, m))
