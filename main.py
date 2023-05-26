from random import randint
from colorama import *
init(autoreset=True)
while True:
    print("Что бы начать игру напишите любое число от 1 до 3")
    a = int(input())
    b = randint(1, 3)
    if a == b :
        print(Fore.GREEN +"ВЫ ВЫЙГРАЛИ", b,)
    elif a!= b and a < 10 and a > 0:
        print(Fore.RED +"ВЫ ПРОИГРАЛИ", b,)
    else:
        print(Fore.YELLOW +"вы ввели неправильное число!!") 