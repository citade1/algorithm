# 문제 boj 2178번: 미로탐색
# N×M크기의 배열로 표현되는 미로가 있다.

# 1	 0	1	1	1	1
# 1	 0	1	0	1	0
# 1	 0	1	0	1	1
# 1	 1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# 예제 입력     예제 출력
# 4 6         15
# 101111
# 101010
# 101011
# 111011

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
