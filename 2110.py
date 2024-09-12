#왼쪽부터 공유기를 설치해나감
#공유기 사이 최소 거리와 공유기 사이 최대 거리 사이를 이진 탐색
#중간값의 거리를 적용해서 집을 돌며 공유기를 설치했을 때, 알맞는 공유기 갯수가 나오는지
#처음 해당 거리를 적용하여 공유기를 설치했을 경우, 그 이후로는 (해당 거리보다 작게 설치하지 않는 이상) 그 거리가 얼마가 되었건 간에 상관이 없음

import sys

n,c = [int(x) for x in input().split()]

houses = []

for i in range(n):
    temp = int(sys.stdin.readline())
    houses.append(temp)
    
houses.sort()

range_min = 1
range_max = houses[-1] - houses[0]
result = 0

while (range_min <= range_max):
    
    mid = (range_min + range_max) // 2 #가능한 공유기 설치 간격의 중위값
    current = houses[0]
    count = 1 #첫 번째 집에는 이미 설치한 것으로 카운트
    for i in range(1, n): #첫 번째 집에는 이미 공유기를 설치했으니 넘어감
        if (houses[i] >= current + mid) : #설치가 가능하다면 (처음 둔 간격이 mid보다 크더라도 차후에 딱 맞게 적용될 수 있으니 일단 넘어감)
            count += 1 #카운트 추가
            current = houses[i] #마지막 공유기 설치 위치 업데이트
            
    if (count >= c): #공유기 설치 대수가 목표보다 많으면
        range_min = mid + 1 #최소 범위를 줄여서 다시 돌리기
        result = mid
    elif (count < c): #공유기 설치 대수가 목표보다 적으면
        range_max = mid - 1 #최대 범위를 줄여서 다시 돌리기
        
print(result)
        