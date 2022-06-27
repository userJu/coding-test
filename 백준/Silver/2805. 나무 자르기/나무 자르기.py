"""
절단기에 높이 H를 지정해야 한다. 
적어도 M미터의 나무를 집에 가져가기 위해서 
절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램

1. 아이디어
이분탐색ㄷ
2. 시간복잡도
N이 100만개 => O(N)으로 풀어야한다.
3. 자료구조 / 변수
가장 짧은 나무, 가장 긴 나무 사이 == mid
while문과 for 문을 이용해 썰어준다
"""
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = list(map(int,input().split()))
min_tree=0
max_tree = max(arr)

while min_tree<=max_tree:
    mid = (min_tree+max_tree)//2
    length = 0
    for x in arr:
        if x>=mid:
            length+=x-mid
        if length>=M:
            min_tree = mid+1
            break
    if length < M:
        max_tree = mid-1
print(max_tree)        

    
