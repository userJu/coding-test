import sys
input = sys.stdin.readline
N = str(input().rstrip())
N = sorted(N,reverse = True)
sum = 0
if '0' not in N:
    print(-1)
else:
    for x in N:
        sum+=int(x)
    if sum%3 != 0:
        print(-1)
    else:
        print("".join(N))
