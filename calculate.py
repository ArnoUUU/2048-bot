import options
#uses xX! RECURSION !Xx to determine the move that will have the most null strings
def nullstrings(matrix,dl):
	left = options.moveleft(matrix)
	right = options.moveright(matrix)
	up = options.moveup(matrix)
	down = options.movedown(matrix)
	if dl != 0:
		left = nullstrings(left,dl-1)
		right = nullstrings(right,dl-1)
		up = nullstrings(up,dl-1)
		down = nullstrings(down,dl-1)
	possible_moves =[left.count(""),left,right.count(""),right,up.count(""),up,down.count(""),down]
	result = [left.count(""),right.count(""), down.count(""), up.count("")]
	result.sort()
	return possible_moves[possible_moves.index(result[3])+1]
