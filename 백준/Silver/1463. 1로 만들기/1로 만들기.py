N = int(input())
dy = [0]*(N+1)

for i in range(2,N+1):
    dy[i] = dy[i-1]+1
    if i % 2 == 0:
        dy[i] = min(dy[i],dy[i//2]+1)
    if i % 3 == 0:
        dy[i] = min(dy[i], dy[i//3]+1)
print(dy[N])
    


