import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
while N>0:
    if N%5 == 0:
        cnt+=N//5
        N = 0
    else:
        N = N-3
        cnt+=1
print(cnt) if N == 0 else print(-1)
        
