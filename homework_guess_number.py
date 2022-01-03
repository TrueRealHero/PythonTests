# 1. Игра угадай число, в игре 3 уровня, на первом уровне у пользователя есть 1 попытка чтобы угадать число в диапазоне от 1 до 10,
# на втором уровне у него 3 попыток, диапазон чисел от 1 до 50, на третьем уровне у него 5 попыток,
# диапазон от 1 до 100, если он угадывает, то переходит на следующий уровень.

# 1. Guess the number game. 3 Rounds.
# First round 1 attempt in range from 1 to 10. Second round 3 attempts, 1-50. Thrid one 5 att from 1 to 100.

import random

def round3():
    print("*" * 20)
    num = random.randrange(1,100)
    attempts = 5
    while attempts > 0:
        my_num = int(input("Enter number between 1 to 100: "))
        if num == my_num:
            print("YOU WON! ARE U SERIOUS?!")
            break
        elif num != my_num:
            attempts -= 1
            print("Wrong! Try again. You have", attempts, "attempts left.")
            if attempts == 0:
                print("You lost! =(")
    return

def round2():
    print("*" * 20)
    num = random.randrange(1,50)
    attempts = 3
    while attempts > 0:
        my_num = int(input("Enter number between 1 to 50: "))
        if num == my_num:
            print("You won! Next round!")
            round3()
            break
        elif num != my_num:
            attempts -= 1
            print("Wrong! Try again. You have", attempts, "attempts left.")
            if attempts == 0:
                print("You lost! =(")

def round1():
    print("*" * 20)
    print("Casino!!! You have only one chance!!! Or you die!!!")
    num = random.randrange(1,10)
    my_num = int(input("Enter number between 1 to 10: "))
    attempts = 1
    if num == my_num:
        print("You won! Next round!")
        round2()
    while num != my_num:
        attempts -= 1
        if attempts == 0:
            print("You lost! =(")
            round1()

round1()