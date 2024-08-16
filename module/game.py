import random
import time
from .clearterminal import clear
from .diffset import diffset

def game(path=str, questions=int, min_number=int, max_number=int, operations=list[str], difficulty = str):
    clear()
    diff = diffset(difficulty)
    for a in range(3):
        name = input('What is your name?\n=> ')
        if name:
            clear()
            break
        print('You must input your name!')
    name = 'Anonymous'
    clear()
    print('Your name will be set to', name)
    input('''
█▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀█ 　 ▀▀█▀▀ █▀▀█ 　 █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ 
█▀▀ █  █   █   █▀▀ █▄▄▀ 　   █   █  █ 　 ▀▀█   █   █▄▄█ █▄▄▀   █   
▀▀▀ ▀  ▀   ▀   ▀▀▀ ▀ ▀▀ 　   ▀   ▀▀▀▀ 　 ▀▀▀   ▀   ▀  ▀ ▀ ▀▀   ▀  ''')
    clear()
    wrong = 0
    print('-'*20)
    time_start = time.time()

    for i in range(questions):
        first = random.randrange(min_number, max_number)
        second = random.randrange(min_number, max_number)

        rand_op = random.randrange(0, len(operations))

        calculate = f'{first} {operations[rand_op]} {second}'
        result = int(eval(calculate))

        while True:
            answer = input(f'Question #{i+1}. {calculate} = ')
            if answer == str(result):
                break
            print('Wrong answer!')
            wrong += 1
        
    time_end = time.time()
    finished_time = round(time_end-time_start, 2)

    print('-'*20)
    input(f'You finished the game in {finished_time} with {wrong} wrong.')
    with open(path, 'a', encoding = 'utf-8') as file:
        file.write(f'\n{name},{finished_time},{wrong},{diff}')