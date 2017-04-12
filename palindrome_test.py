def palindrome_list(l):
	  length = len(l)
	  reverse_list = []
	  for i in l:
	  	reverse_list.append(l[length-1])
	  	length -= 1
	  print(reverse_list)
	  
	  if reverse_list == l:
	  	print("Your list is a palindrome")
	  else:
	  	print("Your list is not a palindrome")

my_list = ["a", "b", "c", "b"]



palindrome_list(my_list)
