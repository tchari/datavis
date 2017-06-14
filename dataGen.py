from random import randint
numPoints = 10;
filename = "data.txt"

output = "["
for i in range(0,numPoints):
    output += "["
    for j in range(0,3):
        num = str(randint(0,100))
        output += num + ", "
    if i == numPoints-1:
        output += str(randint(0,100))+"]"
    else:
        output += str(randint(0,100))+"],"

output += "]"                

f = open(filename, 'w')
f.write(output)
f.close()
