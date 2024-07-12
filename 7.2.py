info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    file.tell()
    x = []
    y = []
    values = []

    for i in range(len(strings)):
        x.append(i + 1)

    for j in strings:
        y.append(file.tell())
        file.write(j + '\n')
        values.append(j)

    keys = list(zip(x, y))
    strings_positions = {}

    for i in range(len(keys)):
        strings_positions.update({keys[i]: values[i]})
        file.close()
    return strings_positions


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
