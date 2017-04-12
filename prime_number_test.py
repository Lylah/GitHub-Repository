
#determines whether or not a number input by the user is a prime number

def is_it_prime():
	number=int(input("Please enter a number:"))
	end = number -1
	
	if number == 2:
		print (" is a prime number")
	elif number % 2 == 0:
		print( " is not a prime number")
	else: 
		for i in range (3, end):
			if number % i == 0:
				print ("not prime")
			else:
				print("prime")
is_it_prime()
