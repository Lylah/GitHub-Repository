

import random

def guessing_game_one():
	computer_number = random.randint(0,10)
	
	user_guess = int(input("Please guess a number between 1 and 9 (inclusive)"))
	
	while user_guess!=computer_number:
		if user_guess > computer_number:
				print("You guessed too high")
				user_guess = int(input("Guess again"))
		elif user_guess < computer_number:
					print("You guessed too low")
					user_guess = int(input("Guess again"))
		
	if user_guess == computer_number:
		print("You guessed correctly")
	
					
guessing_game_one()
