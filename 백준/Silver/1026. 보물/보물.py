import sys
input = sys.stdin.readline
N = int(input())
Arr = list(map(int,input().split()))
Brr = list(map(int,input().split()))
Arr.sort()
Brr.sort(reverse=True)
s =0
for i in range(N):
    s += Arr[i]*Brr[i]
    
print(s)
    

