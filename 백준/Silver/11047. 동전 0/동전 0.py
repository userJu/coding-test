import sys
input = sys.stdin.readline
N,K = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
pt = len(arr)-1
cnt = 0
while K:
    if arr[pt]<=K:
        cnt+=K//arr[pt]
        K = K%arr[pt]
    pt-=1
print(cnt)
    
     