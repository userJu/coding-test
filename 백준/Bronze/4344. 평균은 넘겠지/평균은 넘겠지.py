import sys
n = int(sys.stdin.readline())

for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = 0 
    avg = sum(arr[1:])/arr[0]
    for j in range(1, arr[0]+1):
        if arr[j] > avg:
            cnt+=1
    res = cnt / arr[0] * 100
    print(f'{res:.3f}%')
        
    