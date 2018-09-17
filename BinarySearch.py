import random
from random import randint

def performSearch():
    lower_bound = 0
    upper_bound = 100
    search_num = randint(1,101)
    guess = (upper_bound + lower_bound) // 2
    num_guesses = 0

    print('Searching between ' + str(lower_bound) + ' and ' + str(upper_bound) + ', random number to find is ' + str(search_num))

    while guess != search_num:
        print('Is it ' + str(guess) + '?')
        if guess > search_num:
            upper_bound = guess
        elif guess < search_num:
            lower_bound = guess
        guess = (upper_bound + lower_bound) // 2
        num_guesses += 1
        print('nope')
    print('Is it ' + str(guess) + '?')
    print('Yes!')
    print('Finished after ' + str(num_guesses) + ' guesses, found value is ' + str(guess))

performSearch()
