inplist = []
with open('input', 'r') as file: inplist = file.read().split()

gamma = ""
epsilon = ""
ones = 0

for x in range(1,13):
    for i in range(len(inplist)):
        ones += int(inplist[i][x-1:x])
    if ones > (len(inplist) - ones):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
    ones = 0

print(int(gamma, 2) * int(epsilon, 2))
