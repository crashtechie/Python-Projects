# Purpose: This script demonstrates logic usage in python using random number generator.
import random

    

function main():
  random_int = generate_number()

function generate_number():
  rand_int = random.randint(1,10)
  return rand_int

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



if __name__ == "__main__":
    sys.exit(int(main() or 0))