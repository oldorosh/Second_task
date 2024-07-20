# День и год рождения Пушкина
bornyear = int(input('В каком году родился А.С.Пушкина? '))

if bornyear == 1799:
    bornday = int(input('А в какой день? '))
    if bornday == 6:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')
