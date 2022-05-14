import sys
input = sys.stdin.readline

N = int(input())
cardArr = list(map(int,input().split()))
dict = {}
for x in cardArr:
    dict[x] = 1
M = int(input())
myArr = list(map(int,input().split()))
res = []
for x in myArr:
    if x in dict:
        res.append(1)
    else:
        res.append(0)
print(*res)