from collections import deque

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

#깊이 우선 탐색
def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A')+i), end =' ') #방문 노드 출력
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

#너비 우선 탐색
def bfs(g, i, visited):
    queue = deque([i]) # popleft,left append
    visited[i] = True
    while queue:
        i = queue.popleft()
        print(chr(ord('A') + i), end=' ')
        for j in range(len(g)):
            if g[i][j] == 1 and not visited[j]:
                queue.append(j)
                visited[j] = True

visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [False for _ in range(len(graph))]

dfs(graph, 6, visited_dfs)
print("\n---------------")
bfs(graph, 1, visited_bfs) #GDHBCEFA