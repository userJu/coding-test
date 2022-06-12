import sys
input = sys.stdin.readline

N,K = map(int,input().split())
np = [0]*(K+1)

for _ in range(N):
    w,v = map(int,input().split())
    for i in range(K,w-1,-1):
        np[i] = max(np[i-w]+v, np[i])
        
print(np[-1])