import sys
input = sys.stdin.readline
M,N = map(int,input().split())

prime = [0]*1000001
prime[0] = -1
prime[1] = -1
for i in range(2,(int(1000000**0.5))+1):
    if prime[i] == 0:
        for j in range(i*2,1000001,i):
            prime[j] = -1
for i in range(M,N+1):
    if prime[i] == 0:
        print(i)