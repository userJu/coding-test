import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt=n
for x in arr:
    if x>1:
        for i in range(2, (x//2)+1):
            if x % i == 0 :
                cnt-=1
                break
    elif x ==1:
        cnt-=1
print(cnt)