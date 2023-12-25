from random import randint

print('Добро пожаловать в числовую угадайку!')


def continue_game():
    continu = input('Желаете продолжить игру?(д/да, н/нет): ')
    if continu == 'д':
        return game()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся:)')
def is_valid(n1, a, b):

    for i in range(a, b + 1):
        if i == n1:
            return True
    return False
def game():
    a = int(input('Введите левый предел диапазона: '))
    b = int(input('Введите правый предел диапазона: '))
    n = randint(a, b)
    count = 0
    while True:

        n1 = int(input(f'Введите число от {a} до {b}: '))

        if is_valid(n1, a, b) == True:
            if n1 < n:
                print('Ваше число меньше загаданного. Попробуйте еще раз!')
                count += 1
                continue
            elif n1 > n:
                print('Ваше число больше загаданного. Попробуйте еще раз!')
                count += 1
                continue
            else:
                print('Вы угадали поздравляем!')
                count += 1
                break

        else:
            print(f'А может быть выберем число от {a} до {b}?')
            continue
    while True:
        if count == 1:
            print(f'Вы угадали загаданное число за {count} попытку')
        elif 2 <= count <= 4:
            print(f'Вы угадали загаданное число за {count} попытки')
        else:
            print(f'Вы угадали загаданное число за {count} попыток')

        if continue_game():
            continue_game()
            count = 0

        else:
            break

game()