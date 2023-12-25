import random
def game_rules(): #описание правил
    print('''
Добро пожаловать в мою игру для угадывания чисел.
Давай я объясню тебе правила. Ты выбираешь диапазон, а я загадываю число из этого диапазона, а ты должен угадать. 
Все просто. Ну что, попробуем?''')
def is_valid(check):
    if check.isdigit():
        return True
    else:
        return False
def is_valid_coordinate(check, x, y,):
    if x <= int(check) <= y:
        return True
    else:
        return False

game_rules()
offer = input('Введи да, если хочешь сыграть и нет, если отказываешься от игры: ')
if offer == 'да':
    x, y = map(int, input('Введи диапазон значений через пробел, в котором хочешь искать число: ').split())
    num = random.randint(x, y)
    print('Число уже загадано, попробуй угадать его!')
    count = 0
    while True:
        num_user = (input('Введи число: '))
        if is_valid(num_user):
            while True:
                if is_valid_coordinate(num_user, x, y):
                    while num != num_user:
                        if int(num_user) < num:
                            print('Загаданное число выше. Попробуй еще раз.')
                            count += 1
                        elif int(num_user) > num:
                            print('Загаданное число меньше. Попробуй еще раз.')
                            count += 1
                        num_user = int(input('Введи число: '))
                    if num == num_user:
                        count += 1
                        print(f'Поздравляю, ты угадал. Ты угадал число за {count} попыток')
                        break
                elif is_valid_coordinate(num_user, x, y) == False:
                    print('Ты ввел число, невходящее в заданный диапазон')
                    num_user = int(input('Введи число в заданном диапазоне: '))
                    continue
            break
        elif is_valid(num_user) == False:
            print('А может введешь все таки число?')
            continue
else:
    print('Жаль, если передумаешь - возвращайся')
