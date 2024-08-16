import os

def clear():
    match os.name:
        case 'posix': os.system('clear')
        case 'nt': os.system('cls')