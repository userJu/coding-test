import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
res=[arr[0][0]]
for i in range(1,N):
    arr[i][0] = arr[i-1][0]+arr[i][0]
    arr[i][-1] = arr[i-1][-1]+arr[i][-1]
    for j in range(1,len(arr[i])-1):
        arr[i][j] = max(arr[i-1][j-1],arr[i-1][j])+arr[i][j]
print(max(arr[N-1]))
    
