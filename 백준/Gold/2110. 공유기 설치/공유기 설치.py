import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,C = map(int,input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()
lt = 1
rt = house[-1]-house[0] # 최소 거리 최대 거리
res = 0

while lt<=rt:
    mid = (lt+rt)//2
    cur = house[0]
    cnt = 1
    for i in range(1,len(house)):
        if house[i]>=cur+mid:
            cnt+=1
            cur = house[i]
    if cnt >=C:
        lt = mid+1
        res = mid
    else:
        rt = mid-1

print(res)
