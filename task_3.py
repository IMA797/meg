import csv

'''
описание программы 

в данной программе мы проходимся по бесконечному циклу и смотрим, если имеется введенное название корабля в файле, то мы выводим ответ по образцу: 
Корабль <ShipName> был отправлен с планеты: <planet> и его направление движения было: <direction> 
а если такого кораблся нет в файле, то выводим следующее: error.. er.. ror.. 

vod_nazvanie_korably - переменная, которая отвечает за то, что вводит пользователь с терминала
reader - считывание файла
flag - флаг, отвечающий как-бы за проверку условия
'''

vod_nazvanie_korably = ''

while vod_nazvanie_korably != 'stop':
    with open('space.txt', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='*')
        vod_nazvanie_korably = input()
        flag = True
        for row in reader:
            if vod_nazvanie_korably in row['ShipName']:
                flag = False
                print('Корабль', row['ShipName'], 'был отправлен с планеты:', row['planet'], 'и его направление движения было:', row['direction'])
        if flag:
            print("error.. er.. ror..")
    file.close()
