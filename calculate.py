import options
def compareoptions(matrix):
    left = options.moveleft(matrix)
    right = options.moveright(matrix)
    down = options.movedown(matrix)
    up = options.moveup(matrix)
    possible_moves = [left,right,up,down]
    result = [left.count(""),right.count(""), down.count(""), up.count("")]
    result.sort()
    while True:
        if c == len(possible_moves):
            break
        if result[0]>possible_moves[c]:
            possible_moves.pop(c)
            c = 0
    return possible_moves[0]