import sys
input = sys.stdin.readline
N= int(input())

arr=[]
for _ in range(N):
    s,e = map(int,input().split())
    arr.append((s,e))
arr.sort(key = lambda x :(x[1],x[0]))

et = 0
cnt = 0
for s,e in arr:
    if s >=et:
        cnt+=1
        et = e

print(cnt)