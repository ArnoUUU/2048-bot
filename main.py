import addint
from calculate import compareoptions
matrix = ["","","","","","","","","","","","","","","",""]
gamenum = 0
logs = True
depth = 5
if logs:
  logs = "a"
else:
  logs = "w"
#while matrix doesnt have 2048 empty logs and try again from scratch
while matrix.count(2048)==0:
  gamenum += 1
  movenum = 0
  matrix = ["","","","","","","","","","","","","","","",""]
  #while matrix doesnt have 2048, calculate the best move and do it
  while matrix.count(2048)==0:
    try:
      movenum +=1
      matrix = addint.addint(matrix)
      matrix = compareoptions(matrix,depth)
    except Exception:
      print(matrix)
      break
#when you are done print the end to show how lucky they are
print(matrix)
print(movenum)