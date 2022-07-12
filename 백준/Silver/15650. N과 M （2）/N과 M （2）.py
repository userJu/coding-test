import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
for x in combinations(arr,M):
    print(*x)
