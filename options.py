
def push(matrix):
    while True:
        try: 
            ind = matrix.index("")
            try:
                if matrix[ind+1] != "":
                    matrix[ind] = matrix[ind+1]
                    matrix[ind+1] = "gibberish"
            except Exception:
                matrix[ind] = "gibberish"
        except Exception:
            for i in range(matrix.count("gibberish")):
                ind = matrix.index("gibberish")
                matrix[ind] = ""
    return matrix
def switchvals(matrix, a,b):
    matrix[a] = matrix[a] + matrix[b]
    matrix[b] = matrix[a] - matrix[b]
    matrix[a] = matrix[a] - matrix[b]
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
    matrix = switchvals(1,4)
    matrix = switchvals(2,8)
    matrix = switchvals(3,12)
    matrix = switchvals(6,9)
    matrix = switchvals(7,13)
    matrix = switchvals(11,14)
def rotateright(matrix):
    return [matrix[12],matrix[8],matrix[4],matrix[0],matrix[13],matrix[9],matrix[5],matrix[1],matrix[14],matrix[10],matrix[6],matrix[2],matrix[15],matrix[11],matrix[7],matrix[3]]
def moveleft(matrix):
    return push(matrix)
def moveright(matrix):
    matrix = rightswitch(matrix)
    matrix = push(matrix)
    matrix = rightswitch(matrix)
    return matrix
def moveup(matrix):
    matrix = upswitch(matrix)
    matrix = push(matrix)
    matrix = upswitch(matrix)
    return matrix
def movedown(matrix):
    matrix = rotateright(matrix)
    matrix = push(matrix)
    matrix = rotateright(matrix)
    matrix = rotateright(matrix)
    matrix = rotateright(matrix)
    return matrix