import sys
n = int(input())
narr = set(list(map(int, sys.stdin.readline().split())))
m = int(input())
marr = list(map(int, sys.stdin.readline().split()))

for x in marr:
    print(1) if x in narr else print(0)