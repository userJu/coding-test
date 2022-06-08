import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
dy=[0]*N
dy[0] = 1

res = 1
for i in range(1,N):
    max = 0
    for j in range(i,-1,-1):
        if arr[j]<arr[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max+1
    if dy[i]>res:
        res = dy[i]
print(res)
    