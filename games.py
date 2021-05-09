import random

# Current amount of money which should change depending on whether you win or lose the game.
money = 100


# Function that simulates FLIPPING A COIN.
def coin_flip(bet, guess):
  # Shows how much the player is betting on the game.
  if bet < 0:
    print("It seems you have to bet a positive amount.")
    return 0
  if bet > money:
      print("It seems you don't have enough money to bet.")
      return 0

  # Allows the player to call either Heads or Tails.
  # The random module gives access to various useful functions and one of them being able to generate random numbers. It returns a random integer in range including the end points.
  number = random.randint(0, 1)
  if number == 1:
    result = "Heads"
  else:
    result = "Tails"
  print("The coin has landed and it's showing " + result + ". The player called " + str(guess) + ".")

  # If the player wins the game, returns the amount that they won. If the player loses, returns the amount that they lost as a negative number.
  if result == str(guess):
    print("You won £" + str(bet) + ".")
    return bet
  else:
    print("You lost £" + str(bet) + ".")
    return -bet

# Function that simulates playing the game CHO-HAN.
def cho_han(bet, guess):
  # Shows how much the player is betting on the game.
  if bet < 0:
    print("It seems you have to bet a positive amount.")
    return 0
  if bet > money:
      print("It seems you don't have enough money to bet.")
      return 0

  # The function simulates rolling two dice and adding the results together using the random module.
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  total = dice1 + dice2
  print("Dice total is " + str(total) + ".")

  # The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.
  if guess == "even" or guess == "odd":
    print("Please enter Odd or Even, depending on your preference.")
    return 0

  # Checks to see if the total is even or odd.
  if guess == "Even" and total % 2 == 0:
    print("You won " + str(bet) + ".")
    return bet
  elif guess == "Odd" and total % 2 == 1:
    print("You won £" + str(bet) + ".")
    return bet
  else:
    print("You lost £" + str(bet) + ".")
    return -bet

  # If the player was correct, returns the amount that they won. If the player was incorrect, returns the amount that they lost as a negative number.
  if prediction == result:
    print("Correct, player wins £" + str(bet) + ".")
    return bet
  else:
    print("Incorrect. player loses £" + str(bet) + ".")
    return -bet

# Function that simulates two players picking a card randomly from a deck of cards. The higher number wins.
def higher_card(bet):
  # Shows how much the player is betting on the game.
  if bet < 0:
    print("It seems you have to bet a positive amount.")
    return 0
  if bet > money:
      print("It seems you don't have enough money to bet.")
      return 0
  
  available_cards = list(range(1,21))

  available_cards.sort()

  # Code to see all available cards.
  print(available_cards)
  
  # Each player gets a card between 1 and 20 and prints the result.
  player1 = random.randint(1, 20)
  player2 = random.randint(1, 20)
  print("Player 1, your card is " + str(player1))
  print("Player 2, your card is " + str(player2))
  
  # Checks which player has won and returns the outcome.
  if player1 > player2:
    print("Player 1, you won £" + str(bet) + ".")
    print("Player 2, you lost £" + str(bet) + ".")
    return bet
  if player1 < player2:
    print("Player 2, you won £" + str(bet) + ".")
    print("Player 1, you lost £" + str(bet) + ".")
    return -bet
  else:
    print("It is a draw.")
    return 0

# Function that simulates some of the rules of ROULETTE.
def roulette(bet, guess):
  # Shows how much the player is betting on the game.
  if bet < 0:
    print("It seems you have to bet a positive amount.")
    return 0
  if bet > money:
      print("It seems you don't have enough money to bet.")
      return 0

    # When generating the result, 0 will represent 0 and 37 will represent 00. To generate this result we will use the random method again to get a random number between 0 and 37.
  result = random.randint(0,37)
  if result == 37:
    print("The player guessed " + str(guess) + " and the ball landed on 00.")
  else:
    print("The player guessed " + str(guess) + " and the ball landed on " + str(result) + ".")

    # Checks if the player was right and returns the result. If the players result is 37 the player should not win.
  if (guess == "Odd") and (result % 2 == 1 and result != 37):
    print("You won £" + str(bet) + ".")
    return bet
  if (guess == "Even") and (result % 2 == 0 and result != 0):
    print("You won £" + str(bet) + ".")
    return bet
  elif guess == result:
    print("You won £" + str(bet * 35) + ".")
    return bet * 35
  else:
    print("You lost £" + str(bet) + ".")
    return -bet

money += coin_flip(20, "Tails")

money += cho_han(7000, "Even")

money += higher_card(50)

money += roulette(200,"odd")

print("Your total amount of money is £" + str(money) + ".")
