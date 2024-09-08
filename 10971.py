n = int(input())

arr = []
flags = [False] * n
min = float("inf")

for i in range(n):
    temp = input().split()
    temp = [int(x) for x in temp]
    arr.append(temp)
        
def DFS(start, current, end, arr, cost, turn, flags):
    global min
    if (turn == 1):
        cost = arr[current][end]
        #print(cost)
        
    else :
        cost += arr[current][end]
        #print(cost)
        if (turn == 4):
            if (cost < min):
                min = cost
            else:
                return
    
    turn += 1
    
    for i in range(len(arr[current])):
        if (turn == 4):
            flags[start] = True
            DFS(start, end, start, arr, cost, turn ,flags)
            flags[start] = False
        
        elif (flags[i] == False and i != start):
            flags[i] = True
            DFS(start, end, i, arr, cost, turn, flags)
            flags[i] = False
            
for t in range(n):
    if t < 3:
        flags[t+1] = True
        DFS(t, t, t + 1, arr, 0, 1, flags)
        flags[t+1] = False
    else :
        flags[0] = True
        DFS(t, t, 0, arr, 0, 1, flags)
        flags[0] = False
    
print(min)