import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
chicken=[]
house=[]
INF = 2147000000
for i in range(N):
    for j in range(N):
        if board[i][j] ==1:
            house.append((i,j))
        elif board[i][j] == 2:
            chicken.append((i,j))
res = INF

for x in combinations(chicken,M):
    city_dist = 0
    for h in house:
        house_dist = INF
        for k in x:
            house_dist = min(house_dist, abs(h[0]-k[0])+abs(h[1]-k[1]))
        city_dist+=house_dist
    res = min(res, city_dist)
            
print(res)
            