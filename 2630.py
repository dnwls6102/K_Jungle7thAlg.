n = int(input())
arr = []

blue = 0
white = 0

for i in range(n):
    arr.append([int(x) for x in input().split()])
    
def color_check(arr, n, location):
    first = arr[location[0]][location[1]]
    for hang in range(location[0], location[0] + n):
        for yeol in range(location[1], location[1] + n):
            if arr[hang][yeol] != first:
                return -1
    return first

def color_paper(arr, n, location) :
    global blue, white
    if (n == 1):
        if (arr[location[0]][location[1]] == 1):
            blue += 1
        else :
            white += 1
    elif (color_check(arr, n, location) != -1):
        if color_check(arr, n, location) == 0:
            white += 1
        else:
            blue += 1
    else:
        color_paper(arr, n//2, location)
        color_paper(arr, n//2, (location[0] + n//2, location[1]))
        color_paper(arr, n//2, (location[0], location[1] + n//2))
        color_paper(arr, n//2, (location[0] + n//2, location[1] + n//2))
    
color_paper(arr, n, (0, 0))
print(white)
print(blue)