import addint
from calculate import compareoptions
matrix = ["","","","","","","","","","","","","","","",""]
gamenum = 0
movenum = 0
logs = bool(input("Do you want to enable logs (this may take up a lot of space) for the failed tries? (type True if yes and False if no) Capitalization and spelling matter"))
depth = int(input("What depth do you want me to calculate in? (positive integers only)"))
if logs:
  logs = "a"
else:
  logs = "w"
#while matrix doesnt have 2048 empty logs and try again from scratch
while matrix.count(2048)==0:
  gamenum += 1
  f = open("logs.txt", logs)
  f.write("")
  f.write("Game #"+str(gamenum)+"\n")
  f.close()
  matrix = ["","","","","","","","","","","","","","","",""]
  #while matrix doesnt have 2048, calculate the best move and do it
  while matrix.count(2048)==0:
    try:
      matrix = addint.addint(matrix)
      f = open("logs.txt", "a")
      f.write("Next move is: "+"\n")
      f.write(str(matrix))
      f.write("\n")
      f.write("\n")
      f.close()
      matrix = compareoptions(matrix,depth)
    except Exception:
      print(matrix)
      break
#when you are done print the end to show how lucky they are
print("THE END")