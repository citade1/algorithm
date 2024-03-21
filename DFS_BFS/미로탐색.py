import sys
from collections import deque

input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
graph = [[0]*M for _ in range(N)]
for i in range(N):
    temp = input().rstrip()
    for idx, char in enumerate(temp):
        if int(char)==1:
            graph[i][idx] = 1


# [좌, 우, 상, 하]에 따른 좌표 움직임 리스트
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque([(x,y)])

    while queue:
        x, y = queue.popleft()
        # print(x, y) # for sanity check
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < M and graph[nx][ny]==1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[N-1][M-1]

print(bfs(0,0))
