import sys
import math
input = sys.stdin.readline
N,S = map(int,input().split())
arr = list(map(int,input().split()))
res = abs(arr[0]-S)
for i in range(1,N):
    res = math.gcd(res,abs(arr[i]-S))
print(res)