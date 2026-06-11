import random

def game():
    print('Number guessing game!')
    print('I thought of a number between 1-100')

    number = random.randint(1,100)
    return number
number = game()

def guessing(number):
    guess = int(input("Guess the number : "))

    if guess > number:
        print('Wrong ! try lower')
    elif guess < number:
        print('wrong! try higher')
    else:
        print('You guessed it right!')
        return guess

while True:
    if guessing(number) == number:
        break

