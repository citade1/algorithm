# boj 14502 연구소 문제

# 문제
# 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다
# 이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.
# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
# 빈 칸의 개수는 3개 이상이다.

# 출력
# 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.


import copy
from itertools import combinations
from collections import deque

# Get inputs
n,m = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(n)]

# Get all empty spaces where walls can be built
wall_candidates = [(i,j) for i in range(n) for j in range(m) if lab_map[i][j]==0]
wall_candidates_combs = list(combinations(wall_candidates, 3))

# BFS for widespread
def bfs(map_copy):
    queue = deque()

    # Add all virus position to the queue
    for r in range(n):
        for c in range(m):
            if map_copy[r][c]==2:
                queue.append((r,c))

    # Directions (Up, Right, Down, Left)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # BFS spread simulation
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # Check bounds
            if 0<=nx<n and 0<=ny<m:
                if map_copy[nx][ny]==0:
                    map_copy[nx][ny]=2 # spread virus
                    queue.append((nx,ny))

# Try all combinations and count max safe area
max_safe_area = 0

for walls in wall_candidates_combs:
    # make a deep copy of the original map
    map_copy = copy.deepcopy(lab_map)

    # build walls
    for r,c in walls:
        map_copy[r][c]=1

    # spread virus
    bfs(map_copy)

    # count safe area
    safe_area = sum(row.count(0) for row in map_copy)
    max_safe_area = max(max_safe_area, safe_area)

# print the maximum possible safe area
print(max_safe_area)
