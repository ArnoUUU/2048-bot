def push(submatrix):
    matrixnum = submatrix.count("")
    for i in range(matrixnum):
      ind = submatrix.index("")
      submatrix.pop(ind)
    for i in range(matrixnum):
      submatrix.append("")
    return submatrix
def combine(matrix):
    submatrix1=[matrix[0],matrix[1],matrix[2],matrix[3]]
    submatrix2=[matrix[4],matrix[5],matrix[6],matrix[7]]
    submatrix3=[matrix[8],matrix[9],matrix[10],matrix[11]]
    submatrix4=[matrix[12],matrix[13],matrix[14],matrix[15]]
    push(submatrix1)
    push(submatrix2)
    push(submatrix3)
    push(submatrix4)
    addsame(submatrix1)
    addsame(submatrix2)
    addsame(submatrix3)
    addsame(submatrix4)
    return [submatrix1[0],submatrix1[1],submatrix1[2],submatrix1[3],submatrix2[0],submatrix2[1],submatrix2[2],submatrix2[3],submatrix3[0],submatrix3[1],submatrix3[2],submatrix3[3],submatrix4[0],submatrix4[1],submatrix4[2],submatrix4[3]]
def addsame(submatrix):
    if submatrix[0]==submatrix[1]:
      submatrix=[submatrix[0]+submatrix[1], submatrix[2],submatrix[3],""]
    if submatrix[1]==submatrix[2]:
      submatrix=[submatrix[0],submatrix[1]+submatrix[2],submatrix[3],""]
    if submatrix[2]==submatrix[3]:
      submatrix=[submatrix[0],submatrix[1], submatrix[2]+submatrix[3],""]
    return submatrix
def switchvals(matrix, a,b):
    c = matrix[a]
    d = matrix[b]
    matrix[a] = d
    matrix[b] = c
    return matrix
def rightswitch(matrix):
    matrix = switchvals(matrix, 0, 3)
    matrix = switchvals(matrix, 1, 2)
    matrix = switchvals(matrix, 4, 7)
    matrix = switchvals(matrix, 5, 6)
    matrix = switchvals(matrix, 8, 11)
    matrix = switchvals(matrix, 9, 10)
    matrix = switchvals(matrix, 12, 15)
    matrix = switchvals(matrix, 13, 14)
def upswitch(matrix):
    matrix = switchvals(matrix,1,4)
    matrix = switchvals(matrix,2,8)
    matrix = switchvals(matrix,3,12)
    matrix = switchvals(matrix,6,9)
    matrix = switchvals(matrix,7,13)
    matrix = switchvals(matrix,11,14)
def rotateright(matrix):
    return [matrix[12],matrix[8],matrix[4],matrix[0],matrix[13],matrix[9],matrix[5],matrix[1],matrix[14],matrix[10],matrix[6],matrix[2],matrix[15],matrix[11],matrix[7],matrix[3]]
def moveleft(matrix):
    return combine(matrix)
def moveright(matrix):
    matrix = rightswitch(matrix)
    matrix = combine(matrix)
    matrix = rightswitch(matrix)
    return matrix
def moveup(matrix):
    matrix = upswitch(matrix)
    matrix = combine(matrix)
    matrix = upswitch(matrix)
    return matrix
def movedown(matrix):
    matrix = rotateright(matrix)
    matrix = combine(matrix)
    matrix = rotateright(matrix)
    matrix = rotateright(matrix)
    matrix = rotateright(matrix)
    return matrix