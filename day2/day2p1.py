inplist = []
with open('input', 'r') as file:
    inplist = file.read().split()

pos = 0
depth = 0

for i in range(len(inplist)):
    if inplist[i] == "forward": pos += int(inplist[i+1])
    elif inplist[i] == "up": depth -= int(inplist[i+1])
    elif inplist[i] == "down": depth += int(inplist[i+1])

print(pos*depth)
