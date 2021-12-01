file = open("input", "r")
list_file = [int(i) for i in file.readlines()]

list_3pair = []

for i in range(2, len(list_file)):
    list_3pair.append(list_file[i-2] + list_file[i-1] + list_file[i])

a = 0

for i in range(1, len(list_3pair)):
    if list_3pair[i-1] < list_3pair[i]: a += 1
print(a)
