# Дата рождения Пушкина в цикле

while True:
    birthyear_data = int(input('В каком году родился А.С.Пушкин? '))
    if birthyear_data == 1799:
        while True:
            birthday_data = int(input('А в какой день? '))
            if birthday_data == 6:
                break
        else:
            print('Неверный день рождения')
        break
    else:
        print('Неверный год')

print('Верно')
