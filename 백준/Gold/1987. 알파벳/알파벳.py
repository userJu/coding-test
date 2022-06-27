"""
세로 R칸, 가로 C칸
각 칸에는 대문자 알파벳이 하나씩 적혀 있고
1,1은 말
 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오
 
 * 조건
 말이 지나는 칸은 좌측 상단의 칸도 포함된다.
 
 1.아이디어
 BFS를 통해 dx,dy를 주고 탐색하며 풀자 (DFS도 상관없을듯)
 갈곳이 없으면 끝내면 된다
 2. 시간복잡도
 20까지이기 때문에 둘다 열심히 돌아도 상관없음
 3. 자료구조 / 변수
 변수로 말이 위치한 곳을 넣어주고 돌리면 됨
 말이 방문한 알파벳은 저장. visited
"""
import sys
input = sys.stdin.readline
R,C = map(int,input().split())
board = [list(input()) for _ in range(R)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def BFS(x,y):
    answer =1
    dq = set([])
    dq.add((x,y,board[x][y]))
    while dq:
        xx,yy,visited = dq.pop()
        for i in range(4):
            nx = xx+dx[i]
            ny = yy+dy[i]
            if 0<=nx<R and 0<=ny<C and board[nx][ny] not in visited:
                dq.add((nx,ny,visited+board[nx][ny]))
                answer = max(answer,len(visited)+1)
    print(answer)
        
BFS(0,0)
