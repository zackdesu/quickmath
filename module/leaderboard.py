import csv
from .clearterminal import clear
from .diffset import diffset

def leaderboard(path=str, difficulty=int):
    clear()
    diff = diffset(difficulty)
    with open(path) as csvFile:
        datas = [row for row in csv.DictReader(csvFile) if row['diff'] == diff]
        print('='*77)
        print('''|                                                                           |
|            █   █▀▀ █▀▀█ █▀▀▄ █▀▀ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ █▀▀█ █▀▀▄            |
|            █   █▀▀ █▄▄█ █  █ █▀▀ █▄▄▀ █▀▀▄ █  █ █▄▄█ █▄▄▀ █  █            |
|            ▀▀▀ ▀▀▀ ▀  ▀ ▀▀▀  ▀▀▀ ▀ ▀▀ ▀▀▀  ▀▀▀▀ ▀  ▀ ▀ ▀▀ ▀▀▀             |''')
        print('-'*77)
        for i, data in enumerate(sorted(datas, key=lambda x: x['time'])[:5], start=1):
            print(f'| {f'{i}.':<3} {data['name']:<40}: {data['time']} with {data['wrong'] + ' wrong':<16} |')
        print('='*77)
        
    input('Enter to exit from leaderboard')