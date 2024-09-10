cmd = input().split()
cmd = [int(x) for x in cmd]

n, m = cmd[0], cmd[1]
trees = input().split()
trees = [int(x) for x in trees]

trees.sort()

lt = 0
rt = trees[-1]

while True:
    mid = (lt + rt) // 2
    temp = 0
    for t in trees:
        if (t >= mid):
            temp += (t - mid)
    if temp == m :
        print(mid)
        break
    elif temp > m :
        lt = mid
    else :
        rt = mid
    if (mid == (lt + rt) // 2) :
        print(mid)
        break