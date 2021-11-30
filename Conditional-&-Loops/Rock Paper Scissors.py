print("....ROCK....")
print("....PAPER....")
print("....SCISSORS....")

player_1 = input("Enter your move , player 1 : ").lower()
# print("**NO  CHEATING ** \n \n " * 20)
player_2 = input("Enter your move , player 2 : ").lower()


if player_1 == player_2:
	print("It's a Draw !!")
elif player_1 == 'rock':
	if player_2 == 'scissors':
		print("Player 1 Wins !")
	elif player_2 == 'paper':
		print("Player 2 Wins !!")
elif player_1 == 'paper':
	if player_2 == 'rock':
		print("Player 1 Wins !")
	elif player_2 == 'scissors':
		print("Player 2 Wins !!")
elif player_1 == 'scissors':
	if player_2 == 'paper':
		print("Player 1 Wins !")
	elif player_2 == 'rock':
		print("Player 2 Wins !!")
else:
	print("You have chosen the Wrong Move ")













