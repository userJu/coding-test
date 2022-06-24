"""
아이디어
DFS 백트레킹
시간복잡도 => 8까지니까 중복 가능으로 뽑을 수 있음 | 하지만 문제는 중복 불가
사전순 출력
자료구조
1. 깊이
2. M 배열
"""
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

arr = [0]*M

def DFS(L):
    if L == M:
        print(*arr)
    else:
        for i in range(1,N+1):
            if i not in arr:
                arr[L] = i
                DFS(L+1)
                arr[L] = 0
DFS(0)
