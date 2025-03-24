# boj 2583: 영역 구하기

# 문제
# 눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 
# 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.
# M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 
# 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 
# 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 
# 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

# 출력
# 첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.

from collections import deque

# Get inputs
m, n, k = map(int, input().split())  # m: height (rows), n: width (cols)

# Initialize map
rectangle_map = [[0]*n for _ in range(m)]
# Fill in rectangles
for _ in range(k):
    x0, y0, x1, y1 = map(int, input().split())
    for y in range(y0, y1):       # y좌표는 행 (세로)
        for x in range(x0, x1):   # x좌표는 열 (가로)
            rectangle_map[y][x] += 1  # 채움 표시

# Directions: Up, Right, Down, Left
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# BFS
def bfs(x, y):
    queue = deque([(x, y)])
    rectangle_map[y][x] = -1
    area = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and rectangle_map[ny][nx] == 0:
                rectangle_map[ny][nx] = -1
                queue.append((nx, ny))
                area += 1

    return area

# Run BFS for all unvisited cells
areas = []
num_area = 0

for y in range(m):
    for x in range(n):
        if rectangle_map[y][x] == 0:
            num_area += 1
            areas.append(bfs(x, y))

areas.sort()
print(num_area)
print(*areas)




