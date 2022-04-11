import options
#uses xX! RECURSION !Xx to determine the move that will have the most null strings
def compareoptions(matrix,dl):
	left = options.moveleft(matrix)
	right = options.moveright(matrix)
	up = options.moveup(matrix)
	down = options.movedown(matrix)
	possible_moves =[left.count(""),left,right.count(""),right,up.count(""),up,down.count(""),down]
	if dl != 0:
		left = compareoptions(possible_moves[1],dl-1)
		right = compareoptions(possible_moves[3],dl-1)
		up = compareoptions(possible_moves[5],dl-1)
		down = compareoptions(possible_moves[7],dl-1)
	possible_moves =[left.count(""),left,right.count(""),right,up.count(""),up,down.count(""),down]
	result = [left.count(""),right.count(""), down.count(""), up.count("")]
	result.sort()
	return possible_moves[possible_moves.index(result[3])+1]
