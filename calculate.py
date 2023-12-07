import options


def nulls(matrix):
    nullist = []
    for i in range(15):
        if matrix[i] == "":
            nullist.append(i)
    return nullist


# uses xX! RECURSION !Xx to determine the move that will have the most null strings
def compareoptions(matrix, dl):
    left = options.moveleft(matrix)
    right = options.moveright(matrix)
    up = options.moveup(matrix)
    down = options.movedown(matrix)
    if dl != 0:
        null = []
        null = nulls(matrix)
        for i in range(len(null)):
            matrix[null[i]] = 2
            left2 = compareoptions(left, dl - 1)
            right2 = compareoptions(right, dl - 1)
            up2 = compareoptions(up, dl - 1)
            down2 = compareoptions(down, dl - 1)
            matrix[null[i]] = 4
            left4 = compareoptions(left, dl - 1)
            right4 = compareoptions(right, dl - 1)
            up4 = compareoptions(up, dl - 1)
            down4 = compareoptions(down, dl - 1)
    avgs = [
        	(left2.count("") + left4.count("")) / 2,
        "l",
        (right2.count("") + right4.count("")) / 2,
        "r",
        (up2.count("") + up4.count("")) / 2,
        "u",
        (down2.count("") + down4.count("")) / 2,
        "d",
    ]
    result = [
        (left2.count("") + left4.count("")) / 2,
        (right2.count("") + right4.count("")) / 2,
        (up2.count("") + up4.count("")) / 2,
        (down2.count("") + down4.count("")) / 2,
    ]
    result.sort()
    best = avgs[2 * avgs.index(result[3]) + 1]
    if best == "l":
        return left
    if best == "r":
        return right
    if best == "u":
        return up
    if best == "p":
        return down
def evaluator
