import options


def nulls(matrix):
    nullist = []
    for i in range(15):
        if matrix[i] == "":
            nullist.append(i)
    return nullist


def search(Node root, d):
    left = options.moveleft(GameState)
    right = options.moveright(GameState)
    up = options.moveup(GameState)
    down = options.movedown(GameState)
    root.AddChild(left, )
# uses xX! RECURSION !Xx to determine the move that will have the most null strings
def recursor(GameState, d):
    left = options.moveleft(GameState)
    right = options.moveright(GameState)
    up = options.moveup(GameState)
    down = options.movedown(GameState)
    if d == 0:
        return evaluator(GameState.matrix)
    null = nulls(GameState.matrix)
    for i in range(len(null)):
        GameState.matrix[null[i]] = 2
        left2 = recursor(left, d - 1)
        right2 = recursor(right, d - 1)
        up2 = recursor(up, d - 1)
        down2 = recursor(down, d - 1)
        GameState.matrix[null[i]] = 4
        left4 = recursor(left, d - 1)
        right4 = recursor(right, d - 1)
        up4 = recursor(up, d - 1)
        down4 = recursor(down, d - 1)
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
def evaluator():
    return 
