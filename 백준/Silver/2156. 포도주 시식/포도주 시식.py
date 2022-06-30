import sys
input = sys.stdin.readline
N = int(input())
dp = [0]
arr = [0]*(N+1)
for _ in range(N):
    dp.append(int(input()))
arr[1] = dp[1]
if N>1:
    arr[2] = dp[1]+dp[2]
if N >3:
    for i in range(3,N+1):
        arr[i] = max(arr[i-2]+dp[i],arr[i-3]+dp[i-1]+dp[i],arr[i-1])
print(max(arr))
