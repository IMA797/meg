import csv
'''
описание программы 
в данном случае мы считываем файл, закидываем его в словарь а уже с помощью ключа "ShipName" мы закидываем в список название кораблоей. Далее мы сортируем данный массив в порядке возрастания

spisok_korabl - список, где хранятся названия кораблей
reader - считывание файла
i - начальное значение корабля
n - длина названий кораблей
j - последующий корабль 
m - значение корабля, ну то есть мы находим больший по номеру j и присваиваем переменной "m" значение "j"
'''
spisok_korabl = []
with open('space.txt', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='*')
    for row in reader:
        spisok_korabl.append(row['ShipName'])

i = 0
n = len(spisok_korabl)
while i < n - 1:
    m = i
    j = i + 1
    while j < n:
        if spisok_korabl[j][5:] < spisok_korabl[m][5:]:
            m = j
        j += 1
    spisok_korabl[i], spisok_korabl[m] = spisok_korabl[m], spisok_korabl[i]
    i += 1
for i in range(10):
    print(spisok_korabl[i])
