import sys
input = sys.stdin.readline
N = int(input())
arr=[]
res = [1]*N
cnt=1
for i in range(N):
    x,y = map(int,input().split())
    arr.append((x,y))
for i in range(N):
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            res[i]+=1
print(*res)
            
