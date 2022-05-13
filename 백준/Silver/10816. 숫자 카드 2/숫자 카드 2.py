import sys
input = sys.stdin.readline

N = int(input())
dict={}
searchedArr = list(map(int,input().split()))
for x in searchedArr:
    dict[x] = dict.get(x,0)+1

M = int(input())
searchingArr = list(map(int,input().split()))

res = []
for x in searchingArr:
    if x in dict:
        res.append(dict[x])
    else:
        res.append(0)
        
print(*res)
        