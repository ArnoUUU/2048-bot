import sys
import calculate
import addint

b = 0
matrix = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
gamenum = 0
movenum = 0
logs = True
depth = 2
if logs:
    logs = "a"
else:
    logs = "w"
# while matrix doesnt have 2048 empty logs and try again from scratch
while matrix.count(2048) == 0:
    gamenum += 1
    f = open("logs.txt", logs)
    f.write("")
    f.write("Game #" + str(gamenum) + "\n")
    f.close()
    matrix = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    # while matrix doesnt have 2048, calculate the best move and do it
    while matrix.count(2048) == 0 and b < 10:
        if matrix.count("") > 0:
            matrix = addint.addint(matrix)
            f = open("logs.txt", "a")
            f.write("Next move is: " + "\n")
            f.write(str(matrix))
            f.write("\n")
            f.close()
            matrix = calculate.compareoptions(matrix, depth)
        else:
            print(matrix)
            b += 1
            break
# when you are done print the end to show how lucky they are
print("hi")
