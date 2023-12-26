import options
class GameState():

    def __init__(self,matrix,score,human):
        self.matrix = matrix
        self.score = score
        self.human = human

    def generateLegalMoves(self):
        legals = []
        if self.human:
            left = options.moveleft(self)
            up = options.moveup(self)
            down = options.movedown(self)
            right = options.moveright(self)
            moves = [left,up,down,right]
            for move in moves:
                if self.matrix != move:
                    legals.append(move)
            return legals
        else:
            for i in range(15):
                if self.matrix[i] == None:
                    new2 = new4 = self.matrix
                    new2[i] = 2
                    new4[i] = 4
                    legals.append(new2,new4)
            return legals