import random
# adds a 2 or a 4 in a random spot in the "matrix"
def randadd(matrix):
	oneortwo = random.randint(1,2)
	twoorfour = oneortwo*2
	randomax = 0
	for i in range(matrix.count("")):
		randomax += 1
		ind = matrix.index("")
		matrix[ind] = str(randomax)
	spot = random.randint(1, randomax)
	ind = matrix.index(str(spot))
	matrix[ind] = twoorfour
	for i in range(len(matrix)):
		if type(matrix[i])==str:
			matrix[i] = ""
	return matrix    
