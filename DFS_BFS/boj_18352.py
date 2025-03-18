# 백준 18352번 문제: 특정 거리의 도시 찾기 
# 문제
# 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
# 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 
# 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

# 입력 
# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. 
# (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 
# 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 
# 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

# 출력
# X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
# 이때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.

from collections import deque

# 입력 받기 
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

# 도시 간 거리 초기화
city_distance = [-1]*(n+1)
city_distance[x] = 0

# 각 도시별 거리 계산하기 
from collections import deque
def find_cities(graph, v):
    queue = deque([v])

    while queue:
        q = queue.popleft()
        
        for i in graph[q]:
            if city_distance[i] == -1: # 방문하지 않은 도시만 탐색
                city_distance[i] = city_distance[q] + 1
                queue.append(i)
                
            
find_cities(graph, x)

# 거리가 k인 도시찾기
result = sorted([i for i in range(1, n+1) if city_distance[i]==k])
if result:
    print(" ".join(map(str, result)))
else:
    print(-1)

