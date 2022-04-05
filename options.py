#it combines like terms (when you make a move in 2048, it combines like numbers in a specific order)
def addsame(submatrix):
	if submatrix[0]==submatrix[1]:      
		submatrix=[submatrix[0]+submatrix[1], submatrix[2],submatrix[3],""]
	if submatrix[1]==submatrix[2]:
		submatrix=[submatrix[0],submatrix[1]+submatrix[2],submatrix[3],""]
	if submatrix[2]==submatrix[3]:
		submatrix=[submatrix[0],submatrix[1], submatrix[2]+submatrix[3],""]
	return submatrix
#this is where all the computation happens when you moveleft. (the matrix will be ordered in a way )
def combine(matrix):
	submatrix1=[matrix[0],matrix[1],matrix[2],matrix[3]]
	submatrix2=[matrix[4],matrix[5],matrix[6],matrix[7]]
	submatrix3=[matrix[8],matrix[9],matrix[10],matrix[11]]
	submatrix4=[matrix[12],matrix[13],matrix[14],matrix[15]]
	submatrix1=push(submatrix1)
	submatrix2=push(submatrix2)
	submatrix3=push(submatrix3)
	submatrix4=push(submatrix4)
	submatrix1=addsame(submatrix1)
	submatrix2=addsame(submatrix2)
	submatrix3=addsame(submatrix3)
	submatrix4=addsame(submatrix4)
	return [submatrix1[0],submatrix1[1],submatrix1[2],submatrix1[3],submatrix2[0],submatrix2[1],submatrix2[2],submatrix2[3],submatrix3[0],submatrix3[1],submatrix3[2],submatrix3[3],submatrix4[0],submatrix4[1],submatrix4[2],submatrix4[3]]
#this pops and appends all of the null strings in the submatrix
def push(submatrix):
	matrixnum = submatrix.count("")
	for i in range(matrixnum):
		ind = submatrix.index("")
		submatrix.pop(ind)
	for i in range(matrixnum):
		submatrix.append("")
	return submatrix
# switches the values of two indexes in a matrix
def switchvals(matrix, a,b):
	c = matrix[a]
	d = matrix[b]
	matrix[a] = d
	matrix[b] = c
	return matrix
#prepares a rightmoved matrix to be combined
def rightswitch(matrix):
	matrix = switchvals(matrix, 0, 3)
	matrix = switchvals(matrix, 1, 2)
	matrix = switchvals(matrix, 4, 7)
	matrix = switchvals(matrix, 5, 6)
	matrix = switchvals(matrix, 8, 11)
	matrix = switchvals(matrix, 9, 10)
	matrix = switchvals(matrix, 12, 15)
	matrix = switchvals(matrix, 13, 14)
	return matrix
#prepares a upmoved matrix to be combined
def upswitch(matrix):
	matrix = switchvals(matrix,1,4)
	matrix = switchvals(matrix,2,8)
	matrix = switchvals(matrix,3,12)
	matrix = switchvals(matrix,6,9)
	matrix = switchvals(matrix,7,13)
	matrix = switchvals(matrix,11,14)
	return matrix
def rotateclockwise(matrix):
	return [matrix[12],matrix[8],matrix[4],matrix[0],matrix[13],matrix[9],matrix[5],matrix[1],matrix[14],matrix[10],matrix[6],matrix[2],matrix[15],matrix[11],matrix[7],matrix[3]]
#similar to pressing the left arrow key when playing 2048
def moveleft(matrix):
	return combine(matrix)
#similar to pressing the right arrow key when playing 2048
def moveright(matrix):
	matrix = rightswitch(matrix)  
	matrix = combine(matrix)
	matrix = rightswitch(matrix)
	return matrix
#similar to pressing the up arrow key when playing 2048
def moveup(matrix):
	matrix = upswitch(matrix)
	matrix = combine(matrix)
	matrix = upswitch(matrix)
	return matrix
#similar to pressing the down arrow key when playing 2048
def movedown(matrix):
	matrix = rotateclockwise(matrix)
	matrix = combine(matrix)
	matrix = rotateclockwise(matrix)
	matrix = rotateclockwise(matrix)
	matrix = rotateclockwise(matrix)
	return matrix