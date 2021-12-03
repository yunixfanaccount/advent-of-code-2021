inplist = []
with open('input', 'r') as file: inplist = file.read().split()
oxyL = inplist[:]
carL = inplist[:]
for x in range(1,13):
    ones = 0
    ones_car = 0

    for i in range(len(oxyL)):
        ones += int(oxyL[i][x-1:x])

    for i in range(len(carL)):
        ones_car += int(carL[i][x-1:x])

    ### OXY
    if len(oxyL) >= 2:
        if ones > (len(oxyL) - ones) or ones == (len(oxyL) - ones):
            oxyLRM = [oxyL[i] for i in range(len(oxyL)) if int(oxyL[i][x-1:x]) != 1]
            for i in oxyLRM:
                oxyL.remove(i)
            
        else:
            oxyLRM = [oxyL[i] for i in range(len(oxyL)) if int(oxyL[i][x-1:x]) != 0]
            for i in oxyLRM:
                oxyL.remove(i)

    ### CAR
    if len(carL) >= 2:
        if ones_car > (len(carL) - ones_car) or ones_car == (len(carL) - ones_car):
            carLRM = [carL[i] for i in range(len(carL)) if int(carL[i][x-1:x]) != 0]
            for i in carLRM:
                carL.remove(i)
            
        else:
            carLRM = [carL[i] for i in range(len(carL)) if int(carL[i][x-1:x]) != 1]
            for i in carLRM:
                carL.remove(i)

print(oxyL)
print(carL)
print(int(oxyL[0], 2), int(carL[0], 2))
print(int(oxyL[0], 2) * int(carL[0], 2))
