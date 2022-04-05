import sys
metal = sys.stdin.readline().strip()
stack=[]
cnt = 0
for i in range(len(metal)):
    if metal[i] == '(':
        stack.append(metal[i])
    else:
        stack.pop()
        if i > 0 and metal[i-1] == ")":
            cnt+=1
        elif i > 0 and metal[i-1] == "(":
            cnt+=len(stack)
print(cnt)