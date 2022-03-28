import options
def compareoptions(matrix):
    left = options.moveleft(matrix)
    right = options.moveright(matrix)
    down = options.movedown(matrix)
    up = options.moveup(matrix)
    possible_moves =[left.count(""),left,right.count(""),right,up.count(""),up,down.count(""),down]
    result = [left.count(""),right.count(""), down.count(""), up.count("")]
    result.sort()
    for i in range(16):
        num=possible_moves.count(i)
        if num !=0:
            x=possible_moves.index(num)
            return possible_moves[x+1]
