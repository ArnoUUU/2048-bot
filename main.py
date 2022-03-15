import calculate
import addint
from calculate import compareoptions
matrix = ["","","","","","","","","","","","","","","",""]
while matrix.count("2048")==0:
    matrix = addint(matrix)
    matrix = compareoptions(matrix)
print(matrix)