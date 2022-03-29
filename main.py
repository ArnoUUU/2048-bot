import addint
from calculate import compareoptions
matrix = ["","","","","","","","","","","","","","","",""]

while matrix.count(2048)==0:
  f = open("logs.txt","w")
  f.write("")
  f.close()
  matrix = ["","","","","","","","","","","","","","","",""]
  while matrix.count(2048)==0:
    try:
      matrix = addint.addint(matrix)
      f = open("logs.txt", "a")
      f.write(str(matrix))
      f.close()
      matrix = compareoptions(matrix)
    except Exception:
      print(matrix)
      break
print("THE END")