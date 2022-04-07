import sys
n = int(input())
arr= list(map(int, sys.stdin.readline().split()))
F = dict()
res= [-1 for i in arr]
stack=[]
for x in arr:
    F[x] = F.get(x,0)+1
for i in range(n):
    while stack and F[arr[stack[-1]]] < F[arr[i]]  :
        res[stack.pop()]= arr[i]
    stack.append(i)
print(*res)