import sys
input = sys.stdin.readline
N = int(input())
arr=[0]
dy = [0]*(N+1)
for _ in range(N):
    arr.append(int(input()))
dy[0] = arr[0]
dy[1] = arr[1]
if N >1:
    dy[2] = max(arr[0]+arr[2], arr[1]+arr[2], dy[1])
if N >3:
    for i in range(3,N+1):
        dy[i] = max(dy[i-2]+arr[i], dy[i-3]+arr[i-1]+arr[i],dy[i-1])
print(max(dy))
