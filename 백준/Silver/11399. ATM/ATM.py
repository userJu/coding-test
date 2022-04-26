# n이 1000까지
# p또한 1000까지
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
arr.sort()

res = 0
for idx, x in enumerate(arr):
    res+=x*(N-idx)
print(res)

