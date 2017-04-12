
import random
def rock_paper_scissors():
	player1=input("Please enter rock, paper, or scissors:")
	player2=random.choice(["rock", "paper", "scissors"])
	print(player1, player2)
	if player1 == player2:
		print("tie - try again!")
	elif player1 == "rock" and player2 == "scissors":
		print("player1 wins")
	elif player1 == "paper" and player2 == "scissors":
		print("computer wins!")
	elif player1 == "scissors" and player2 == "paper":
		print("player1 wins")
	elif player1 == "scissors" and player2 == "rock":
		print("computer wins!")
	elif player1=="rock" and player2 == "paper":
		print("computer wins!")
	else:
		print("you missed a condition")

rock_paper_scissors()
