import random
#Please create a list containing the three actions of the game.
actions = ["rock", "paper", "scissors"]
print(actions)

#Select a random action for each player
player1 = random.choice(actions)
player2 = actions[random.randint(0,2)]
print(player1)
print(player2)

while True:
  if player1 == player2:
    print("Tie! Both players choose the same action.")
  elif player1 == 'paper':
    if player2 == 'rock':
      print("Winner is: Player 1")
    else:
      print("Winner is: Player 2")
  elif player1 == 'rock':
    if player2 == 'paper':
      print("Winner is: Player 2")
    else:
      print("Winner is: Player 1")
  elif player1 == 'scissors':
    if player2 == 'paper':
      print("Winner is: Player 1")
    else:
      print("Winner is: Player 2")

  play_again = input("Play again? (yes/no): ")
  if play_again.lower() != "yes" :
      break
  else:
    totalRound = input("How many rounds do you want to play? ")
    player1_score = 0
    player2_score = 0
    for i in range(int(totalRound)):
      player1 = random.choice(actions)
      player2 = actions[random.randint(0, 2)]
      print(player1)
      print(player2)
      if player1 == player2:
        print("Tie! Both players choose the same action.")
      elif player1 == 'paper':
        if player2 == 'rock':
          print("Winner is: Player 1")
          player1_score += 1
        else:
          print("Winner is: Player 2")
          player2_score += 1

      elif player1 == 'rock':
        if player2 == 'paper':
          print("Winner is: Player 2")
          player2_score += 1
        else:
          print("Winner is: Player 1")
          player1_score += 1

      elif player1 == 'scissors':
        if player2 == 'paper':
          print("Winner is: Player 1")
          player1_score += 1
        else:
          print("Winner is: Player 2")
          player2_score += 1

      print("Score:", "Player1 =", player1_score, "Player2 =", player2_score)








