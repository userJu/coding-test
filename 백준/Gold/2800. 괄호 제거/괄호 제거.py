import sys
from itertools import combinations
input = sys.stdin.readline
stack = []
arr = input().rstrip()
glst = []
resarr = set()
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(i)
    elif arr[i] == ')':
        s = stack.pop()
        glst.append((s,i))


for i in range(1,len(glst)+1):
    for comb in combinations(glst,i):
        tmp = list(arr)
        for x in comb:
            tmp[x[0]] = ""
            tmp[x[1]] = ""
            resarr.add("".join(tmp))
for x in sorted(list(resarr)):
    print(x)
            
            
