def push(matrix, d):
    if d == "left":
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


