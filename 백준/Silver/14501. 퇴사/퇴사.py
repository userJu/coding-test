import sys
input = sys.stdin.readline
N = int(input())
np = [0]*(N+1)
arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N-1,-1,-1):
    if i + arr[i][0]<=N:
        np[i] = max(arr[i][1]+np[i+arr[i][0]],np[i+1])
    else:
        np[i] = np[i+1]
print(np[0])
            
