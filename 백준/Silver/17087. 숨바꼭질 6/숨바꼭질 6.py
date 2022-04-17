import sys
import math
n,s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    if arr[i]-s < 0:
        arr[i] = abs(arr[i]-s)
    else:
        arr[i] = arr[i]-s
for i in range(1,n):
    arr[0] = math.gcd(arr[0],arr[i])
print(arr[0])
