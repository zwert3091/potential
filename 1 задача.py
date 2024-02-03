with open('scientist.txt', encoding='utf-8') as f:
    '''Считывание файла'''
    data = f.readlines()

'''Фильтрация по названию препарата'''
arr = list()
for c in data[1:]:
    elem = c.split('#')
    if elem[1] == 'Аллопуринол':
        arr.append(elem)

'''Сортировка по дате создания'''
new_arr = sorted(arr, key=lambda x: int(x[2].split('-')[0]))

'''Создание нового файла с конечными результатами'''
with open('scientist_origin.txt', 'w') as f:
    f.write('Разработчиками Аллопуринола были такие люди:\n')
    for c in new_arr:
        f.write(' - '.join([c[0], c[2]]) + '\n')
    f.write(f'\nОригинальный рецепт принадлежит: {new_arr[0][0]}')

