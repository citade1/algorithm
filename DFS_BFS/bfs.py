from collections import deque

def bfs(graph, start, visited):
    """
    큐로 너비 우선 탐색(breadth-first search) 알고리즘 구현.
    탐색된 노드 순서로 프린트.

    parameter
    ---------
    graph: 그래프를 2차원 인접리스트로 구현
    start: 탐색 시작 노드
    visited: 방문한 노드의 true/false를 표시한 1차원 리스트
    """

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# execution
graph = [[], [2,3,4], [5], [6,7], [8], [9], [10], [], [], [], []]
visited = [False] * len(graph)

bfs(graph, 1, visited)
