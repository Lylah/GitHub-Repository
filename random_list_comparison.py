

import random
def compare_list():
	a=[]
	for i in range(10):
		a.append(random.randrange(1,200,1))
	print(a)
	b=[]
	for i in range(20):
		b.append(random.randrange(1,200,1))
	print(b)
	c=[]
	for i in b:
		if i in a:
			c.append(i)
	print(c)
	
compare_list()
