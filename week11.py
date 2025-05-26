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
    visited[i] = 1
    print(chr(ord('A') + i), end=' ')
    for j in range(len(g)):
        if not visited[j]:
            visited[j] = 1
            print(chr(ord('A') + j), end = ' ')
        pass

visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]

dfs(graph, 7, visited_dfs)
print()
bfs(graph, 4, visited_bfs) #GDBHCEFA