import sys
metal = sys.stdin.readline().strip()
stack=[]
cnt = 0
for i in range(len(metal)):
    if metal[i] == '(':
        stack.append(metal[i])
    else:
        stack.pop()
        if metal[i-1] == ")":
            cnt+=1
        else:
            cnt+=len(stack)
print(cnt)