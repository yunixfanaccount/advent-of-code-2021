inplist = []
with open('input', 'r') as file:
    inplist = [int(i) for i in file.readlines()]

a = 0
for i in range(1, len(inplist)):
    if inplist[i-1] < inplist[i]: a += 1
print(a)
