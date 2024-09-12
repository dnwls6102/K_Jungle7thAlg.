n = int(input())

def hap(first_n, current_n, is_first):
    if (is_first == False and first_n == current_n):
        return 0
    is_first = False
    current_n = (current_n % 10) * 10 + ((current_n // 10) + (current_n % 10)) % 10
    return 1 + hap(first_n, current_n, is_first)

print(hap(n, n, True))