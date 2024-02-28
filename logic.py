# Purpose: This script demonstrates logic usage in python using random number generator.
import random
my_int = random.randint(1,10)
your_int = int(input("Pick an number between 1 and 10: "))
    
while your_int != my_int:
    if your_int < 1:
        your_int = int(input('Your number is less than 1! \n Please enter a number between 1 and 10: '))
    elif your_int > 10:
        your_int = int(input('Your number is above 10! \n Please enter a number between 1 and 10: '))
    elif your_int < my_int:
        print(f'\n{your_int} is too low\n')
        your_int = int(input('Guess again: '))
    elif your_int > my_int:
        print(f'\n{your_int} is to high \n')
        your_int = int(input('Guess again: '))
    else:
        print('WTF Dude!?')

print('You Win!!')