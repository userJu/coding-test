import sys
input = sys.stdin.readline
N = int(input())
step = [0]
for _ in range(N):
    step.append(int(input()))

if N == 1:
    print(step[1])
else:
    dy = [0]*(N+1)
    dy[1] = step[1]
    dy[2] = step[1]+step[2]
    for i in range(3,N+1):
        dy[i] = max(dy[i-3]+step[i-1], dy[i-2])+step[i]
    print(dy[N])
    