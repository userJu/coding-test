import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
res=[arr[0][0]]
for i in range(1,N):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][0] = arr[i-1][0]+arr[i][0]
        elif j == len(arr[i])-1:
            arr[i][-1] = arr[i-1][-1]+arr[i][-1]
        else:
            arr[i][j] = max(arr[i-1][j-1],arr[i-1][j])+arr[i][j]
print(max(arr[N-1]))
    
