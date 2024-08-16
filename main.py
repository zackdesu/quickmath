import os
from dotenv import dotenv_values
from getpass import getpass
from module import game, leaderboard, clear

PROBLEMS = 10
MIN_NUMBER = 0
MAX_NUMBER = 0
OPERATIONS = ['+', '-', '*']
PATH = './log.csv'
PASSWORD = dotenv_values('.env')['PASSWORD']

if __name__ == '__main__':
    while True:
        clear()
        print('='*88)
        print('''∥      ██████╗ ██╗   ██╗██╗ █████╗ ██╗  ██╗███╗   ███╗ █████╗ ████████╗██╗  ██╗██╗     ∥
∥     ██╔═══██╗██║   ██║██║██╔══██╗██║ ██╔╝████╗ ████║██╔══██╗╚══██╔══╝██║  ██║██║     ∥
∥     ██║██╗██║██║   ██║██║██║  ╚═╝█████═╝ ██╔████╔██║███████║   ██║   ███████║██║     ∥
∥     ╚██████╔╝██║   ██║██║██║  ██╗██╔═██╗ ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║╚═╝     ∥
∥      ╚═██╔═╝ ╚██████╔╝██║╚█████╔╝██║ ╚██╗██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██╗     ∥
∥        ╚═╝    ╚═════╝ ╚═╝ ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ∥''')
        print('='*88)
        print('1. Play Game\n2. Leaderboard\n3. Clear Log\n4. Exit')
        option = input('=> ')

        match option:
            case '1': 
                option = input('Mode:\n1. Easy\n2. Normal\n3. Hard\n=>')
                match option:
                    case '1':
                        MIN_NUMBER = 2
                        MAX_NUMBER = 8
                    case '2':
                        MIN_NUMBER = 3
                        MAX_NUMBER = 12
                    case '3':
                        MIN_NUMBER = 6
                        MAX_NUMBER = 18
                game(PATH, PROBLEMS, MIN_NUMBER, MAX_NUMBER, OPERATIONS, option)
            case '2': 
                option = input('Mode:\n1. Easy\n2. Normal\n3. Hard\n=>')
                leaderboard(PATH, option)
            case '3': 
                password = getpass()
                if password == PASSWORD:
                    os.remove(PATH)
                    with open(PATH, 'w') as file:
                        file.write('name,time,wrong,diff')
                else:
                    input('Password salah')
            case '4': break
            case _: print('Option not valid!')