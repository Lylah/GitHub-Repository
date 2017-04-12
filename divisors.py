
#generates a list of divisors for a number input by the user

def divisors():
	X= int(input("please enter a number:"))
	divisor_list=[]
	for i in range(1,500):
		if X%i==0:
			divisor_list.append(i)
	print(divisor_list)
			
divisors()
