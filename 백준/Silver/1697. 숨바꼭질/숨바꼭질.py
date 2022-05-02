from collections import deque
N,K = map(int,input().split())

def BFS(X):
    dq = deque()
    arr = [0]*100001
    dq.append(X)
    visited = set()
    visited.add(X)

    while dq:
        p = dq.popleft()
        if p == K:
            return arr[p]
        for x in [p-1, p+1, 2*p]:
            if 0<= x <= 100000 and x not in visited:
                visited.add(x)
                dq.append(x)
                arr[x] = arr[p]+1

print(BFS(N))

