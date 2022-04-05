import random
# adds a 2 or a 4 in a random spot in the "matrix"
def addint(matrix):
	oneortwo = random.randint(1,2)
	twoorfour = oneortwo*2
	rando = 0
	for i in range(matrix.count("")):
		rando += 1
		ind = matrix.index("")
		matrix[ind] = str(rando)
	spot = random.randint(1, rando)
	ind = matrix.index(str(spot))
	matrix[ind] = twoorfour
	for i in range(len(matrix)):
		if type(matrix[i])==str:
			matrix[i] = ""
	return matrix    
