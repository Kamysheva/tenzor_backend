import random

currentNum = random.randint(1, 100)
isCorrect = False

while not isCorrect:
    print(f'Твое число - {currentNum}?\n0 - верно, 1 - больше, -1 - меньше')
    answer = input()
    if answer == '1':
        currentNum = random.randint(currentNum, 100)
    elif answer == '-1':
        currentNum = random.randint(1, currentNum)
    elif answer == '0':
        isCorrect = True
        print('Ура!')
    else:
        print('Непонятный ответ')
