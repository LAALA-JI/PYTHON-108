# Importing Random
from random import randint
# Our Dumb AI logic
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

# Taking Input from user
player = input("Player,Enter your move: ").lower()
print(f"Computer plays {computer}")


# Our RPS Logic

if player == computer:
	print("It's a tie!!")
elif player == "rock" :
	if computer == "paper":
		print("Computer wins")
	else:
		print("Player Wins ")
elif player == "paper" :
	if computer == "scissors":
		print("Computer wins")
	else:
		print("Player Wins ")
elif player == "scissors" :
	if computer == "rock":
		print("Computer wins")
	else:
		print("Player Wins ")
else:
	print("You have entered something Wrong")














