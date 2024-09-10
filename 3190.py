import sys
from collections import deque

n = int(sys.stdin.readline()) #맵 크기 (n*n)

map = [[0 for y in range(n)] for x in range(n)]

k = int(sys.stdin.readline())
for a in range(k):
    apple_index = sys.stdin.readline().strip().split()
    apple_index_x = int(apple_index[0]) - 1
    apple_index_y = int(apple_index[1]) - 1
    map[apple_index_x][apple_index_y] = -1

l = int(sys.stdin.readline())
move_buffer = [] #이동 커맨드를 저장하는 리스트
snake_loc = deque() #뱀 머리가 이동한 지역들(=뱀 몸이 위치한 지역들)을 저장하는 queue

for m in range(l): #이동
    move_buffer.append(sys.stdin.readline().strip().split())

sec = 0 #결괏값
death_flag = False #사망 플래그
cur_location = [0,0, "열+"] #행, 열, 이동 방향 (x,y)
snake_loc.appendleft((cur_location[0], cur_location[1])) #시작 위치 enqueue
map[cur_location[0]][cur_location[1]] = 1 #시작 위치 표시

for move in move_buffer: #게임 시작
    move[0] = int(move[0])
    for s in range(move[0] - sec):
        sec += 1
        if (cur_location[2] == "열+"): #오른쪽
            cur_location[1] += 1
        elif (cur_location[2] == "열-"): #왼쪽
            cur_location[1] -= 1
        elif (cur_location[2] == "행+"): #아래
            cur_location[0] += 1
        elif (cur_location[2] == "행-"): #위
            cur_location[0] -= 1
        if (cur_location[0] < 0 or cur_location[0] >= n or cur_location[1] < 0 or cur_location[1] >= n): #벽에 부딪혔으면
            death_flag = True
            break
        if (map[cur_location[0]][cur_location[1]] == 1): #자기 몸이랑 부딪혔으면
            death_flag = True
            break
        if (map[cur_location[0]][cur_location[1]] != -1): #이동한 곳에 사과가 없다면
            last_loc = snake_loc.pop() #마지막 위치 dequeue
            map[last_loc[0]][last_loc[1]] = 0 #map 이차원 배열에 현재 위치 정보 update
        snake_loc.appendleft((cur_location[0], cur_location[1])) #queue에 현재 위치값 enqueue
        map[cur_location[0]][cur_location[1]] = 1 #해당 위치에 snake가 있음을 표시
            
    if death_flag :
        break
    if (cur_location[2] == "열+"): #커맨드에 따른 진행 방향 조정
        if (move[1] == "L"):
            cur_location[2] = "행-"
        elif (move[1] == "D"):
            cur_location[2] = "행+"
    elif (cur_location[2] == "열-"):
        if (move[1] == "L"):
            cur_location[2] = "행+"
        elif (move[1] == "D"):
            cur_location[2] = "행-"
    elif (cur_location[2] == "행+"):
        if (move[1] == "L"):
            cur_location[2] = "열+"
        elif (move[1] == "D"):
            cur_location[2] = "열-"
    else:
        if (move[1] == "L"):
            cur_location[2] = "열-"
        elif (move[1] == "D"):
            cur_location[2] = "열+"
            
while (not death_flag):
    sec += 1
    if (cur_location[2] == "열+"): #오른쪽
        cur_location[1] += 1
    elif (cur_location[2] == "열-"): #왼쪽
        cur_location[1] -= 1
    elif (cur_location[2] == "행+"): #아래
        cur_location[0] += 1
    elif (cur_location[2] == "행-"): #위
        cur_location[0] -= 1
    if (cur_location[0] < 0 or cur_location[0] >= n or cur_location[1] < 0 or cur_location[1] >= n): #벽에 부딪혔으면
        death_flag = True
        break
    if (map[cur_location[0]][cur_location[1]] == 1): #자기 몸이랑 부딪혔으면
        death_flag = True
        break
    if (map[cur_location[0]][cur_location[1]] != -1): #이동한 곳에 사과가 없다면
        last_loc = snake_loc.pop() #마지막 위치 dequeue
        map[last_loc[0]][last_loc[1]] = 0 #map 이차원 배열에 현재 위치 정보 update
    snake_loc.appendleft((cur_location[0], cur_location[1])) #queue에 현재 위치값 enqueue
    map[cur_location[0]][cur_location[1]] = 1 #해당 위치에 snake가 있음을 표시
        
    

print(sec)


    

