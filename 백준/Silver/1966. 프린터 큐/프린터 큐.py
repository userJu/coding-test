from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    prior = list(map(int,input().split()))
    
    dq = deque([])
    
    for idx, x in enumerate(prior):
        dq.append([idx,x])
    prior.sort(reverse = True)
    
    cnt = 0
    
    while dq:
        if dq[0][1] >= prior[cnt]:
            if dq[0][0] == M:
                cnt+=1
                print(cnt)
                break
            dq.popleft()
            cnt+=1
        elif dq[0][1] < prior[cnt]:
            dq.append(dq.popleft())
    