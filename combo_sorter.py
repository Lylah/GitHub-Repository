
#combination function that will sort a list of numbers in ascending order or a list of words (without duplicate first-letters) in alphabetical order


nums = [67, 89, 55, 100, 43, 5, 34]
my_list = ["Bird", "Gargoyle", "Flavor", "Mnemonic", "Absent"]
seq =[]

def sorting(X):
	seq=[]
	if type(X[0]) == str:
		X=[item.lower() for item in X]
		while len(X)>0:
			large=X[0]
			largest=ord(X[0][0])
			for i in X:
				if ord(i[0])<largest:
					large=i
					largest=ord(i[0])
			seq.append(large)
			X.remove(large)
			
	elif type(X[0]) == int:
		while len(X)>0:
			largest=X[0]
			for i in X:
				if i<largest:
					largest=i
			seq.append(largest)
			X.remove(largest)

	print(seq)
		
	
	
sorting(my_list)
sorting(nums)
