with open('scientist.txt', encoding='utf-8') as f:
    '''Считывание файла'''
    data = list(map(str.rstrip, f.readlines()))

arr = list()
for c in data[1:]:
    elem = c.split('#')
    arr.append(elem)

while (date := input()) != 'эксперимент':
    d = date.split('.')
    d = d[::-1]
    d = '-'.join(d)

    flag = False
    for elem in arr:
        if d in elem:
            name = elem[0].split()

            print(f'Ученый {name[0]} {name[1][0]}. {name[2][0]}. создал препарат: {elem[1]} - {date}')
            flag = True
    if not flag:
        print('В этот день ученые отдыхали')
