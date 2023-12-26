import calculate
from addint import randadd
from Board import GameState


legals = [0]
f = open('logs.txt','w')
for i in range(10):
    matrix = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    score = 0
    human = False

    root = GameState(matrix, score, False)
    root.matrix = randadd(root.matrix)
    root.matrix = randadd(root.matrix)
    root.human = True

    depth = 1.5
    while True:
        try:
            root = calculate.search(root, 2*depth)
            root.matrix = randadd(root.matrix)
        except Exception:
            break

    f.write("Score: "+str(root.score)+" Highest Number: "+str(max(root.matrix))+"\n")
f.close()