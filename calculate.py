
def search(root,d):
    legals = root.generateLegalMoves()
    scores =[]
    for move in legals:
        scores.append(minimax(move,False,d-1))
    return (legals[scores.index(max(scores))])


def minimax(root, human, d):
    if d == 0:
        if root.generateLegalMoves() == []:
            return 0
        return expectiEvaluation(root)
    legals = root.generateLegalMoves()
    scores = []
    for move in legals:
        scores.append(minimax(move, not human, d-1))
    if human:
        return max(scores) 
    else:
        return min(scores)


def evaluation(gamestate):
    return gamestate.score

def expectiEvaluation(gamestate):
    score = gamestate.score
    for i in range(3):
        score += 2**i*gamestate.matrix[i]
    return score