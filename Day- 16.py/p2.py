from collections import deque
def build_graph(n,edges):
    graph=[[0]*n for i in range(n)]
    for u,v in edges:
        graph[u][v]=1
        graph[v][u]=1
    return graph
edges=[[1,0],[2,3],[1,2]]
graph=build_graph(4,edges)
def print_graph(graph):
    print("Adjacency Matrix:")
    for row in graph:
        print(row)
print_graph(graph)
def dfs(graph,start):
    n=len(graph)
    visited=[False]*n
    stack=[start]
    print("DFS Traversal:")
    while  stack:
        node=stack.pop()
        if not visited[node]:
            visited[node]=True
            print(node,end="")


def bfs(graph, start):
    n = len(graph)
    visited = [False] * n
    q = deque([start])
    visited[start] = True
    print("BFS Traversal:")
    while q:
        node = q.popleft()
        print(node, end=" ")
        for i in range(n):
            if graph[node][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
    print()