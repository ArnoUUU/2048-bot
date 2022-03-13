def moveleft(matrix):
    return push(matrix)
def moveright(matrix):
    matrix = rightswitch(matrix)
    matrix = push(matrix)
    matrix = rightswitch(matrix)
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

