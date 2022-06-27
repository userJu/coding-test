"""
 K개의 랜선은 길이가 제각각
 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 
 K개의 랜선을 잘라서 만들어야 한다.
  N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.
  만들 수 있는 최대 랜선의 길이 => 길이를 최대로

1. 아이디어
이분탐색
2. 시간복잡도
N이 100만 이하의 정수,
3. 자료구조, 변수
while문 안에 cnt로 개수 카운팅
lt = 1부터, rt는 최대 렌선 값
"""
import sys
input = sys.stdin.readline
K,N = map(int,input().split())
arr = []
lt = 1
rt = 0
for _ in range(K):
    x = int(input())
    rt = max(rt,x)
    arr.append(x)
    
while lt<=rt:
    mid = (lt+rt)//2
    cnt = 0
    for x in arr:
        if x>=mid:
            cnt+=x//mid
        if cnt >=N:
            lt = mid+1
            break
    if cnt<N:
        rt = mid-1
print(rt)
        