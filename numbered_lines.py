def number(input_line):
    numbered_lines = []
    for i in range(len(input_line)):
        numbered_lines.append(f'{i+1}: {input_line[i]}')
    return numbered_lines


lines = ['a', 'b', 'c']
empty = []

print(number(lines))
print(number(empty))
