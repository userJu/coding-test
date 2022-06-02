import sys
input = sys.stdin.readline

T = int(input())

dy = [[1,0],[0,1]]

def fibo(n) :
    if n < len(dy):
        return 
    if n >1 and n >=len(dy):
        for i in range(len(dy),n+1):
            dy.append([dy[i-1][0]+dy[i-2][0],dy[i-2][1]+dy[i-1][1]])
        return

for _ in range(T):
    n = int(input())
    fibo(n)
    print(*dy[n])
