import addint
from calculate import compareoptions
def initiate(logs):
  matrix = ["","","","","","","","","","","","","","","",""]
  depth = 3
  gamenum = 0
  if logs:
    logs = "a"
  else:
    logs = "w"
  return matrix, depth, gamenum
def after_move(matrix,logs):
  matrix = addint.addint(matrix)
  f = open("logs.txt", logs)
  f.write("Next move is: "+"\n")
  f.write(str(matrix))
  f.write("\n")
  f.write("\n")
  f.close()
#while matrix doesnt have 2048, calculate the best move and do it
def iterate_game(matrix,logs,depth):
  while matrix.count(2048)==0:
    try:
      matrix = after_move(matrix,logs)
      matrix = compareoptions(matrix,depth)
    except Exception:
      return matrix
  return matrix
def new_game(logs,gamenum):
  gamenum += 1
  f = open("logs.txt", logs)
  f.write("")
  f.write("Game #"+str(gamenum)+"\n")
  f.close()
  return ["","","","","","","","","","","","","","","",""]