"""
같은수 두번 X
묶은거 또묶기 X
묶은수끼리는 더하기 == 0은 안묶는게 좋음.
큰 수는 묶을수록 좋음

1. 알고리즘
2. 시간복잡도.
N이 50보다 작으니 3승까지 돌릴 수 있다.

"""
import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
arr = []
m_arr = []

res = 0
for _ in range(N):
    x = int(input())
    if x <=0:
        m_arr.append(x)
    elif x == 1:
        res+=1
    else:
        arr.append(x)
        

m_arr.sort()
arr.sort(reverse = True)

if len(arr) %2 !=0:
    arr.append(1)
if len(m_arr)% 2 !=0:
    m_arr.append(1)
for i in range(0,len(arr),2):
    res+=(arr[i]*arr[i+1])
for i in range(0,len(m_arr),2):
    res+=(m_arr[i]*m_arr[i+1])
print(res)
    
    
        

