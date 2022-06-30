import sys
input = sys.stdin.readline
N = int(input())
board = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(N):
    a,b = map(int,input().split())
    for i in range(a,10+a):
        for j in range(b,10+b):
            if board[i][j] == 0:
                board[i][j] = 1
                cnt+=1
print(cnt)