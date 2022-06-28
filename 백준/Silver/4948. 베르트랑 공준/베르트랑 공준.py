import sys
input = sys.stdin.readline
N = int(input())

prime = [0]*((123456*2)+1)
prime[0] = -1
prime[1] = -1
for i in range(2,(int(123456*2**0.5)+1)):
    if prime[i] == 0:
        for j in range(i*2, (123456*2)+1, i):
            prime[j] = -1

while N :
    cnt = 0
    for i in range(N+1,2*N+1):
        if prime[i] == 0:
            cnt+=1
    print(cnt)
    N = int(input())