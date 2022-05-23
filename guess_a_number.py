print("Lets play a game!")
print("The computer will pick a number from 0 to 100. Try to guess it!")

from random import randrange

comp_num = randrange(0, 101)

won = False
count = 0

while not won:

    user_num = int(input("Guess a number: "))

    if comp_num > user_num:
        print("You guessed too low! Try again.")
        count += 1
        continue

    elif comp_num < user_num:
        print("You guessed too high! Try again.")
        count += 1
        continue

    elif comp_num == user_num:
        print("Well done! You have guessed the number! Its ", comp_num, ".", sep="")
        count += 1
        if count == 1:
            print("It took you", count, "attempt to guess it.")
        elif count > 1:
            print("It took you", count, "attempts to guess it.")
        break
        
        
