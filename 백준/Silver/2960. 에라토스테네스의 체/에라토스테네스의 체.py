import sys
input = sys.stdin.readline
N,K = map(int,input().split())
prime = [0]*(N+1)
cnt = 0
for i in range(2,N+1):
	if cnt>K:
		break
	else:
		if prime[i] == 0:
			for j in range(i,N+1,i):
				if prime[j] == 0:
					cnt+=1
					prime[j] = 1
				if cnt == K:
					print(j)
					break
