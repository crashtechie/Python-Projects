# Purpose: This script demonstrates logic usage in python using random number guessing game

import random

def main(): 
  random_number = random.randint(1,10) 
  run_game = True
  while run_game == True:
    user_input = input("Pick an number between 1 and 10: ")
    if validate_number(user_input) == False:
      print("Not a number please try again.")
    elif validate_range(int(user_input)) == False:
      print("Not between 1 and 10 please try again.")
    elif int(user_input) < random_number:
      print("Too low guess again")
    elif int(user_input) > random_number:
      print("Too high guess again")
    else:
      print("Yay! you guessed it.")
      run_game = False
  print("Thank you for playing.")
      
def validate_number(input_str):
  isIntiger = True
  try:
      int(input_str)
  except :
      isIntiger = False
  return isIntiger 
  
def validate_range(input_int:int):
  if input_int < 1 or input_int > 10:
    return False
  else:
    return True

if __name__ == "__main__":
  main()