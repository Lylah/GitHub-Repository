
nums = [67, 89, 55, 100, 43, 5, 34]
seq =[]

def sort_numbers_ascending(X):
	seq=[]
	while len(X)>0:
		largest=X[0]
		for i in X:
			if i<largest:
				largest=i
		seq.append(largest)
		X.remove(largest)
	print(seq)

sort_numbers_ascending(nums)

nums = [67, 89, 55, 100, 43, 5, 34]
seq =[]

def sort_numbers_descending(X):
        seq=[]
        while len(X)>0:
                smallest=X[0]
                for i in X:
                        if i>smallest:
                                smallest=i
                seq.append(smallest)
                X.remove(smallest)
        print(seq)

sort_numbers_descending(nums)
