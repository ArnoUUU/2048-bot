import options
def nulls(matrix):
    nullist = []
    for i in range(15):
        if matrix[i] == "":
        	nullist.append(i)
#uses xX! RECURSION !Xx to determine the move that will have the most null strings
def compareoptions(matrix,dl):
	left = options.moveleft(matrix)
	right = options.moveright(matrix)
	up = options.moveup(matrix)
	down = options.movedown(matrix)
	possible_moves =[left.count(""),left,right.count(""),right,up.count(""),up,down.count(""),down]
	if dl != 0:
		nulls = nulls(matrix)
		for i in range(len(nulls)):
			matrix[nulls[i]] = 2
			left2 = compareoptions(possible_moves[1],dl-1)
			right2 = compareoptions(possible_moves[3],dl-1)
			up2 = compareoptions(possible_moves[5],dl-1)
			down2 = compareoptions(possible_moves[7],dl-1)
			matrix[nulls[i]] = 4
			left4 = compareoptions(possible_moves[1],dl-1)
			right4 = compareoptions(possible_moves[3],dl-1)
			up4 = compareoptions(possible_moves[5],dl-1)
			down4 = compareoptions(possible_moves[7],dl-1)
	twomoves = [left2,right2,up2,down2]
	fourmoves = [left4,right4,up4,down4]
	possible_moves =[left.count(""),left,right.count(""),right,up.count(""),up,down.count(""),down]
	
	result = [left.count(""),right.count(""), down.count(""), up.count("")]
	result.sort()
	return possible_moves[possible_moves.index(result[3])+1]
