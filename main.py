# Write code below 💖
import random

print("Welcome to the dice game!")

def roll_dice():
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)

  global total
  total = dice1 + dice2

  return True

roll_true = False

while True:

  play = input("Do you want to play? (Yes/No): ")

  if play.lower() == "yes":
    print("Rolling Dices...")
    roll_true = roll_dice()
    if roll_true == True:
      while True:
        result = int(input("What is the total (2-12)? "))
        if result == total:
          print("You got it")
          break
        else:
          print("Wrong try again!")
  elif play.lower() == "no":
    print("Ok, if do you want to play, just write Yes.")
  else:
    print("Command Invalid, try again.")

  