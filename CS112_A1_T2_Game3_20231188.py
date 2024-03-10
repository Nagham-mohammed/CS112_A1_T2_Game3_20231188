# File: CS112_A1_T2_3_20231188.py
# Purpose: The (Subtract a square) game by python.
# Two players choose a perfect square numbers and who takes the last coin wins.
# Author: Nagham Mohamed Mostafa
# ID: 202301188

import math
from random import randint
def main():
#to make a list from wich the user choose the way he wants
  print("Hello players to our subtract game !")
#a help for users to understand the game
  print("who gets the last coin wins!")
  print("choose a prorer way of playing with")
  print("A)Random number ")
  print("B)a certain number")
#to allow the user choose
  choice = input("Enter your choice: ")
  while choice !="A" and choice !="B" :
      choice = input("Enter your choice: ")
      break
  if choice == "B":
      n_coins = int(input("How many coins would you like to play on"))
# offers a random number to user
  elif choice == "A":
       n_coins= randint(1,1000)

  print("the number of coins is :" ,n_coins)

#to let the users see the number of coins

  def check_perfect_square_num(number):
     square_num = math.isqrt(number)
     return square_num*square_num ==number
  while n_coins > 0 :
#checking if the move is a perfect square root
      move=int(input("player 1 , please enter a PERFECT square number: "))
      square_root=math.sqrt(move)
#to assure that the user pick a right number
      while not check_perfect_square_num(move):
          move=int(input(" Enter a VALID prfect square number please :"))
#avoid getting  negative numbers
      while move>n_coins:
          move=int(input("Enter a SMALLER number please :"))
      n_coins-=move
    #let the user khow his next step
      print("the number of coins became  :" ,n_coins)
      if n_coins ==0 :
          print()
          print("player 1 is a WINNER !")

          #to let the user choose if he want to play again
          def offer_another_game():
              print()
              print("do you want to play again?")
              print("1) play again")
              print("2) Exit")
              choice2 = int(input("Enter your choice:"))
              if choice2 == 1:
                  main()
              elif choice2 == 2:
                  exit(0)
              else:
                  choice2 = input("Enter a VALID choice please: ")
              print()
          offer_another_game()
          break
#repeating what happenned with player 1 again
      move=int(input("player 2 , please enter a square number: "))
      square_root=math.sqrt(move)

      while not check_perfect_square_num(move):
          move=int(input(" Enter a VALID prfect square number please :"))

      while move>n_coins:
            move=int(input(" Enter a SMALLER number please :"))
      n_coins-=move
      print("the number of coins became  :" ,n_coins)

      if n_coins==0:
         print()
         print("player 2 is the WINNER !")

         def offer_another_game():
             print()
             print("do you want to play again?")
             print("1) play again")
             print("2) Exit")
             choice2 = int(input("Enter your choice:"))
             if choice2 == 1:
                 main()
             elif choice2 == 2:
                 exit(0)
             else:
                 choice2 = input("Enter a VALID choice please: ")
             print()
         offer_another_game()
         break
#starting the game
if __name__ == "__main__":
    main()


