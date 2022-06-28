import sys
input = sys.stdin.readline
n = int(input())

stack = []
res = ''
cur = 1
for _ in range(n):
    x = int(input())
    while cur <x:
        stack.append(cur)
        cur+=1
        res+='+'
    if cur ==x:
        res+="+-"
        cur+=1
    elif cur > x:
        if stack.pop() ==x:
            res+='-'
        else:
            print('NO')
            cur = 0
            break
if cur!=0:
    print(*res,sep="\n")
    
    

            
