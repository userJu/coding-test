import sys
input = sys.stdin.readline

T = int(input())

dy=[0,1,2,4]
def dynamic(n):
    if n<len(dy):
        return
    if n>3 and n >=len(dy):
        for i in range(len(dy),n+1):
            dy.append(dy[i-1]+dy[i-2]+dy[i-3])
        return

for _ in range(T):
    n = int(input())
    dynamic(n)
    print(dy[n])