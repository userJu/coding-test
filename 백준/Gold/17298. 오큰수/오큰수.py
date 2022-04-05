import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
blueprint = [-1]*n 
stack = []
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        blueprint[stack.pop()] = arr[i]
    stack.append(i)
print(*blueprint)    
            
    