file = open("input", "r")
list_file = [int(i) for i in file.readlines()]
a = 0
for i in range(1, len(list_file)):
    if list_file[i-1] < list_file[i]:
        a = a + 1
print(a)