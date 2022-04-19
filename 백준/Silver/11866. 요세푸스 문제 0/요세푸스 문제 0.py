from collections import deque
n,k = map(int,input().split())
arr = deque([i for i in range(1,n+1)])
res=[]
rem = 1
while arr:
    if rem==k:
        res.append(arr.popleft())
        rem=1
    else :
        rem+=1
        arr.append(arr.popleft())
print('<', end="")
print(*res, sep=", ", end="")
print('>')
    