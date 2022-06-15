import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
arr = set(arr)
arr = list(arr)
arr.sort()
for x in arr:
    print(x)