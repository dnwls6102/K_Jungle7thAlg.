cmd = [int(x) for x in input().split()]
m, n, l = cmd[0], cmd[1], cmd[2] #사대의 수, 동물의 수, 사정거리

marks = sorted([int(x) for x in input().split()]) #사대 위치 저장하는 배열
animals = [] #동물들 위치를 저장하는 배열

count = 0 #사냥 가능한 동물 수를 저장하는 변수

for x in range(n):
    loc = [int(t) for t in input().split()] #[x,y]형태로 저장
    animals.append(loc)
    
for x,y in animals:
    #사대 위치 별로 사정거리를 계산하기
    if (y > l): #동물 좌표 값 y가 사정거리보다 길 경우(사대가 어디에 있던 간에 사냥이 불가능함)
        continue
    # 동물 위치 기준에서 동물이 잡힐 수 있는 사대 위치의 최대/최소값
    # 사대 위치의 y값은 무조건 0이다
    # l값은 무조건 y값 이상이다 (y값이 l값보다 큰 경우는 위 조건문에서 배제시킴)
    # 그러므로 최솟값은 x - (l - y) => x + y - l
    # 최댓값은 x + (l - y) => x - y + l
    # lt가 rt보다 작을 때까지 반복문을 진행시키고, 그 동안에 알맞는 사대 위치가 나온다면 count += 1, 없으면 그냥 넘어가기
    min_mark = x + y - l
    max_mark = x - y + l
    lt = 0
    rt = m - 1 # lt, rt는 사대를 저장하는 배열의 index
    while lt <= rt:
        mid = (lt + rt) // 2
        mid_mark = marks[mid]
        if (mid_mark >= min_mark and mid_mark <= max_mark): #중위값으로 찾은 사대 위치가 최대,최소 범위 안에 있을 경우
            count += 1
            break
        elif (mid_mark < min_mark): # 그 외의 경우 : 어차피 mid 인덱스의 사대는 사정거리 내에 없는 것으로 판정되었으니 +-1 해준 값으로 업데이트
            lt = mid + 1
        else:
            rt = mid - 1

print(count)