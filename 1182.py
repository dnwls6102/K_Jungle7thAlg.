import sys

n,s = [int(x) for x in sys.stdin.readline().split()]

nums = [int(x) for x in sys.stdin.readline().split()]

count = 0

def func(idx, s, nums ,current_sum, n):
    global count
    if (idx >= n):
        return
    current_sum += nums[idx]
    
    if (current_sum == s):
        count += 1
    
    func(idx + 1, s, nums, current_sum, n)
    
    func(idx + 1, s, nums, current_sum - nums[idx], n)

func(0, s, nums, 0, n)
print(count)