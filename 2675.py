n = int(input())

for i in range(n) :
    temp = input().split()
    for x in temp[-1]:
        print(x * int(temp[0]), end="")
    print()