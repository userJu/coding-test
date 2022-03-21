import sys
t = int(sys.stdin.readline())
for _ in range(t):
    res=''
    r,s = map(str, sys.stdin.readline().split())
    for x in s:
        for _ in range(int(r)):
            res +=x
    print(res)