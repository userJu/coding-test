import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
F={}
stack=[]
res=[-1]*N
for x in arr:
    F[x] = F.get(x,0)+1
for i in range(N):
    while stack and F[arr[i]] > F[arr[stack[-1]]]:
        res[stack.pop()]= arr[i]
    stack.append(i)
print(*res)