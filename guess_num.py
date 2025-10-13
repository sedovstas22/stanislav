from random import randint

num = randint(1, 10)

while True:
    guess = int(input())
    if guess == 0:
        break
    if guess == num:
        print('Congratulations, u guessed the number!!!')
        continue
    elif num < guess:
        print("Try again, the number is less from what u've written")
    else:
        print('Try again, the number is greater')
