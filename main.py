import addint
from calculate import compareoptions
matrix = ["","","","","","","","","","","","","","","",""]

logs = bool(input("Do you want to enable logs (this may take up a lot of space) for the failed tries? (type True if yes and False if no) Capitalization and spelling matter"))
depth = int(input("What depth do you want me to calculate in? (positive integers only)"))

#while matrix doesnt have 2048 empty logs and try again from scratch
while matrix.count(2048)==0:
  f = open("logs.txt","w")
  f.write("")
  f.close()
  matrix = ["","","","","","","","","","","","","","","",""]
  #while matrix doesnt have 2048, claculate the best move and do it
  while matrix.count(2048)==0:
    try:
      matrix = addint.addint(matrix)
      f = open("logs.txt", "a")
      f.write(str(matrix))
      f.close()
      matrix = compareoptions(matrix,2)
    except Exception:
      print(matrix)
      break
#when you are done print the end to show how lucky they are
print("THE END")