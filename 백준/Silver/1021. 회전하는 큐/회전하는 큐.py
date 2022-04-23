from collections import deque
N,M = map(int,input().split())
arr = deque([i for i in range(1,N+1)])
point = list(map(int,input().split()))
cnt=0
for x in point:
    idx = arr.index(x)
    if len(arr)/2 < idx:
        while arr[0] != x:
            arr.appendleft(arr.pop())
            cnt+=1
    else:
        while arr[0] != x:
            arr.append(arr.popleft())
            cnt+=1
    if arr[0]== x:
        arr.popleft()
print(cnt)
            