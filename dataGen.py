from random import randint
filename = "data.txt"

output = "["
for i in range(0,10):
    output += "["
    for j in range(0,3):
        num = str(randint(0,100))
        output += num + ", "
    if i == 9:
        output += str(randint(0,100))+"]"
    else:
        output += str(randint(0,100))+"],"

output += "]"                

f = open(filename, 'w')
f.write(output)
f.close()
