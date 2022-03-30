import options
def compareoptions(matrix):
    left = options.moveleft(matrix)
    right = options.moveright(matrix)
    down = options.movedown(matrix)
    up = options.moveup(matrix)
    possible_moves =[left.count(""),left,right.count(""),right,up.count(""),up,down.count(""),down]
    result = [left.count(""),right.count(""), down.count(""), up.count("")]
    result.sort()
    return possible_moves[possible_moves.index(result[3])+1]
