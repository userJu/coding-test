# 필요한 시간의 최솟값
# 사람의 수 <= 1000 => 2승을 해도 된다
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split())) # 3 1 4 3 2
arr.sort() # 1 2 3 4 5
sum = 0
for i in range(N,0,-1):
    sum +=(arr[N-i]* i)
print(sum)