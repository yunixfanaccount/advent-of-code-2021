inplist = []
with open('input', 'r') as file:
    inplist = file.read().split()

pos = 0
depth = 0
aim = 0

for i in range(len(inplist)):
    if inplist[i] == "up": aim -= int(inplist[i+1])
    elif inplist[i] == "down": aim += int(inplist[i+1])
    elif inplist[i] == "forward":
        pos += int(inplist[i+1])
        depth += aim * int(inplist[i+1])

print(pos*depth)
