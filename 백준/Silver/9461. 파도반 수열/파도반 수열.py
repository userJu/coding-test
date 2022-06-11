import sys
input = sys.stdin.readline
T = int(input())
dy = [0]*101
dy[1] = 1
dy[2] = 1
dy[3] = 1

for _ in range(T):
    N = int(input())
    if dy[N]>0:
        print(dy[N])
    else:
        for i in range(4,N+1):
            dy[i] = dy[i-3]+dy[i-2]
        print(dy[N])
        