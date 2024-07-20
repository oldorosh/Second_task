# Игра - даты рождения знаменитостей

count_true = 0

while True:
    year_1 = int(input('В каком году родилась Мария Шарапова? '))
    # 1987
    if year_1 == 1987:
        count_true += 1
    year_2 = int(input('В каком году родился Александр Овечкин? '))
    # 1985
    if year_2 == 1985:
        count_true += 1
    year_3 = int(input('В каком году родилась Ксения Собчак? '))
    # 1981
    if year_3 == 1981:
        count_true += 1
    year_4 = int(input('В каком году родился Никита Михалков? '))
    # 1945
    if year_4 == 1945:
        count_true += 1
    year_5 = int(input('В каком году родился Валерий Гергиев? '))
    # 1953
    if year_5 == 1953:
        count_true += 1
    print('Количество верных ответов:', count_true)
    print('Количество ошибок:', 5 - count_true)
    print('Процент правильных ответов:', count_true * 20, '%')
    print('Процент неправильных ответов:', 100 - count_true * 20, '%')
    game_continue = input('Хотите начать игру сначала? ')
    if game_continue == 'нет'.lower():
        break

print('Игра окончена.')

