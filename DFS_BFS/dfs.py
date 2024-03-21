
def dfs(graph, v, visited):
    """
    기본 깊이 우선 탐색(depth-first search) 알고리즘. 재귀함수 사용.
    탐색한 노드를 차례로 프린트.

    parameter
    ---------
    graph: 그래프를 구현한 2차원 인접 리스트
    v: 현재 탐색하는 대상
    visited: 방문한 노드를 true/false로 나타내는 1차원 리스트
    """

    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def dfs_stack(graph, start, visited):
    """
    스택을 사용한 깊이 우선 탐색(depth-first search) 알고리즘.
    탐색한 노드를 차례로 프린트.

    parameter
    ---------
    graph: 그래프를 구현한 2차원 인접 리스트
    start: 탐색을 시작할 노드
    visited: 방문한 노드를 true/false로 나타내는 1차원 리스트
    """

    stack = [start]

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            
            for i in reversed(graph[v]): # 그래프를 거꾸로 탐색하여 스택의 상단(끝)에 인접 노드가 먼저 오도록 함.
                if not visited[i]:
                    stack.append(i)


# execution
graph = [[], [2,5,9], [3], [4], [], [6,8], [7], [], [], [10], []]
visited = [False] * len(graph)

dfs(graph, 1, visited)
dfs_stack(graph, 1, visited)
