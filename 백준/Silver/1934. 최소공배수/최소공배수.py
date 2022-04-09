import math
n = int(input())
for _ in range(n):
    cnt=1
    a,b = map(int, input().split())
    print(math.lcm(a,b))