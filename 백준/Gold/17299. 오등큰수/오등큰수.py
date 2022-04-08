import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
# F에 수열에 등장하는 원소들의 횟수를 모아놓는다(dict=> 값 : 위치 구조로 만든다)
# stack을 만들어 하나하나 검사한다
# 결과를 뽑는 배열을 -1로 arr길이만큼 초기화해놓는다
F = dict()
stack=[]
res = [-1]*n
for x in arr:
    F[x]= F.get(x,0)+1 # 원소 : 원소의 수
for i in range(n):
    while stack and F[arr[stack[-1]]] < F[arr[i]]:
        res[stack.pop()] = arr[i]
    stack.append(i)
print(*res)