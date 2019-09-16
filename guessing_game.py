import random

random_number = random.randint(1, 20)
#https://inventwithpython.com/chapter4.html

def start_game():
    print("Hello, welcome to Mikes number guessing game!")
  
    num_guesses = 0
  
    while True:

        try:
          guess = input("Guess a number from 1 to a 20: ")
          guess = int(guess) 
          if guess > 20:
            print("That's higher than the max number of 20. Try again")
          elif guess < 1:
            print("That's lower than the minimum number of 1. Try again")
        except ValueError:
          print("That's not a number. Please enter a number value between 1 and 20")
          continue
  
        if guess > random_number:
          num_guesses += 1
          print("That number is too high, lets try a lower number.")
        elif guess < random_number:
          num_guesses += 1
          print("That number is too low, lets try a higher number")
        elif guess == random_number:
          print("Thats correct, you guessed the right number!")
          print("you guessed in {} tries!".format(num_guesses))
          try_again = (input("Would you like to try again? Y/N  "))
          if try_again == "Y" or try_again == "y":
              print("Here we go again!")
              start_game()
          elif try_again == "N" or try_again == "n":
              print("Thank you for playing!")
              exit()
              #exit() credit to: https://opentechschool.github.io/python-beginners/en/getting_started.html
            
  
  


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()