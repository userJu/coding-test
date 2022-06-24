import sys
input = sys.stdin.readline
board = [list(input().rstrip()) for _ in range(5)]
pt = 0
res=''
while pt<16:
    for i in range(5):
        if len(board[i]) >pt:
            res+=board[i][pt]
    pt+=1
print(res)    
    
        