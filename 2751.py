#start: 시작 인덱스, end: 끝 인덱스 , arr : 배열

def merge(left, right):
    i, j = 0, 0
    sorted_list = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    
    return sorted_list

def merge_sort(arr):
    
    if (len(arr) == 1):
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    left_sorted = merge_sort(left_arr)
    right_sorted = merge_sort(right_arr)
    return merge(left_sorted, right_sorted)

n = int(input())
result = []
for i in range(n):
    result.append(int(input()))

result = merge_sort(result)
for x in result:
    print(x)
    