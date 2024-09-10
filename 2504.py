txt = input()
txts = [] #괄호 검사하는 stack

tmp = 1
result = 0
wrongFlag = False   

for i in range(len(txt)):
    if txt[i] == "(":
        txts.append(txt[i])
        tmp *= 2
    elif txt[i] == "[":
        txts.append(txt[i])
        tmp *= 3
    elif txt[i] == ")":
        if not txts or txts[-1] == "[":
            result = 0
            break
        if txt[i-1] == "(":
            result += tmp
        txts.pop()
        tmp //= 2
    else:
        if not txts or txts[-1] == "(":
            result = 0
            break
        if txt[i-1] == "[":
            result += tmp
        txts.pop()
        tmp //= 3

if txts:
    print(0)
else :
    print(result)