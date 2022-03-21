import sys
n = int(sys.stdin.readline())
arr = int(sys.stdin.readline())
res = 0
for x in str(arr):
    if int(x) >0:
        res+=int(x)
print(res)