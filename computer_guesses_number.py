print("Think of a number from 0 to 100. The computer will try to guess it.")
print()

user_ready = input('Have you picked a number? Type "yes" when you are ready ')

print("The computer's guess: ")
low_n = 0
high_n = 101
from random import randrange
guess = randrange(low_n, high_n)
print(guess)
counter = 1
user_says = input("Type 'correct' if the computer's guess is correct. Otherwise say 'too high' or 'too low': ")

too_low_list = []
too_high_list = []

winner = False
while not winner:
    
    if user_says == 'correct':
        print("The computer guessed your number. ", "It is ", guess, ".", sep="")
        if counter == 1:
            print("It took the computer", counter, "attempt to guess it.")
        elif counter > 1:
            print("It took the computer", counter, "attempts to guess it.")
        winner = True
        
    elif user_says == 'too high':
        too_high_list.append(int(guess))
        too_high_list.sort()
        high_n = too_high_list[0]
        guess = randrange(low_n, high_n)
        ok = False
        while not ok:
            if guess in too_high_list or guess in too_low_list:
                guess = randrange(low_n, high_n)
            else:
                ok = True
        print("The computer's guess: ")
        print(guess)
        counter += 1
        user_says = input("Type 'correct' if the computer's guess is correct. Otherwise say 'too high' or 'too low': ")
        
    elif user_says == 'too low':
        too_low_list.append(int(guess))
        too_low_list.sort()
        low_n = too_low_list[-1]
        guess = randrange((low_n+1), high_n)
        ok = False
        while not ok:
            if guess in too_low_list or guess in too_high_list:
                guess = randrange((low_n+1), high_n)
            else:
                ok = True
        print("The computer's guess: ")
        print(guess)
        counter += 1
        user_says = input("Type 'correct' if the computer's guess is correct. Otherwise say 'too high' or 'too low': ")
        
    else:
        print("Error")
