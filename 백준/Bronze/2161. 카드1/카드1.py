from collections import deque
N = int(input())

arr = [i for i in range(1,N+1)]
arr = deque(arr)

res = []
while arr:
    res.append(arr.popleft())
    if arr:
        arr.append(arr.popleft())
    else:
        break
print(*res)

