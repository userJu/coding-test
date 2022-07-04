"""
구현
"""
import sys
input = sys.stdin.readline
N = int(input())

S = [0]*21

for _ in range(N):
    cmd = list(map(str,input().split()))
    if len(cmd)>1:
        c = cmd[0]
        n = int(cmd[1])
        if c == 'add':
            if S[n] == 0:
                S[n] = 1
        elif c == 'remove':
        	if S[n] == 1:
        		S[n] = 0
        elif c == 'check':
            if S[n] == 1:
                print(1)
            else:
                print(0)
        elif c == 'toggle':
            if S[n] == 1:
                S[n] = 0
            else:
                S[n] = 1
    else:
        if cmd[0] == 'all':
            for i in range(1,21):
                S[i] = 1
        elif cmd[0] == 'empty':
            for i in range(1,21):
                S[i] = 0
            
    