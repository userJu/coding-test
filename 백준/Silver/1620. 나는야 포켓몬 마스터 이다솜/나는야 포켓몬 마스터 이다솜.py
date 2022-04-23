import sys
input = sys.stdin.readline
N,M = map(int,input().split())
poketNum = {} 
poketName={}
for i in range(N):
    n = input().rstrip()
    poketName[n]=i+1
    poketNum[i+1]=n
for _ in range(M):
    q = input().rstrip()
    if q.isdecimal():
        print(poketNum[int(q)])
    else:
        print(poketName[q])
    