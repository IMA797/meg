import csv

'''
Описание программы:
в самом начаде мы открываем файл "space.txt" и плюс параллельно открываем файл "space_new.txt" (в самом начале, ну то есть при первом запуске программы такого файла нет, но он сам автоматически
создаст этот файл). далее мы считываем построчно файл плюс параллеьно начинаем заполнять наш новый файл. Следущим моим шагом было в фикле "for" мы прописываем условия и ищем координаты: 
если там по "х" они больше нуля, то они заменяются на определенную вещь, которая получилась из преобразований арифметических действий над "х"б То же самое происходит и с координатой "у". 
Далее мы смотрим, если последний элемент кода корабля оканчивается на "V" то мы выводим его название и его координаты по образцу:  <ShipName> - (<x>, <y>)

reader - считывание файла
writer_new - то, что скидывается в новый файл 
n - первая цифра номера корабля 
m - вторая цифра номера корабля 
t - кол-во букв в родной планете корабля 
koordin - координаты корабля взятые из фалйа
xd, yd - координаты вектора направления


'''
with open('space.txt', encoding='utf-8') as file, open('space_new.txt', 'w', encoding='utf-8') as file_new:
    reader = csv.DictReader(file, delimiter='*')
    writer_new = csv.DictWriter(file_new, ['ShipName', 'planet', 'coord_place', 'direction'], delimiter='*')
    writer_new.writeheader()
    for row in reader:
        n = int(row['ShipName'][5])
        m = int(row['ShipName'][6])
        t = len(row['planet'])
        koordin = row['coord_place'].split(' ')
        xd = int(koordin[0])
        yd = int(koordin[1])
        if n > 5:
            x = n + xd
        else:
            x = -(n + xd) * 4 + t
        if m > 3:
            y = m + t + yd
        else:
            y = -(n + yd) * m
        row['coord_place'] = str(x) + ' ' + str(y)
        if row['ShipName'][3] == 'V':
            print(row['ShipName'], ' - ', '(', str(x), ',', str(y), ')')
        writer_new.writerow(row)
