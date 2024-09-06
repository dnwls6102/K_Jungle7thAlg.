templist = []
for i in range (9):
    templist.append(int(input()))

print(max(templist))
print(templist.index(max(templist)) + 1)