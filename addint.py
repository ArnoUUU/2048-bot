import random
# adds a 2 or a 4 in a random spot in the "matrix"
def randadd(matrix):
	nulls = []
	oneortwo = random.randint(1,2)
	randint = oneortwo*2
	for i in range(15):
		if matrix[i]==None:
			nulls.append(i)
	spot = random.randint(0, len(nulls)-1)
	matrix[nulls[spot]] = randint
	return matrix    
