from collections import deque
n,k = map(int, input().split())
arr = deque(list(x for x in range(1,n+1)))
cnt = 0
res=[]
while arr:
    cnt+=1
    if cnt % k == 0 :
        res.append(arr.popleft())
    else:
        arr.append(arr.popleft())
print('<',', '.join(str(x) for x in res),'>',sep="")
        
        
    