# 연속합 : 다익스트라. 연속된 숫자가 커야 한다
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
dy = [0]*N
dy[0] = arr[0]
res = -2147000000
for i in range(1,N):
    dy[i] = max(dy[i-1]+arr[i], arr[i])
    if dy[i]> res:
        res = dy[i]
if res < dy[0]:
    print(dy[0])
else:
    print(res)
