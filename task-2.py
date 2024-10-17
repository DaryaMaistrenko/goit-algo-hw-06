import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Пошук у глибину (DFS)
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for node in graph[start]:
        if node not in path:
            new_path = dfs(graph, node, goal, path)
            if new_path:
                return new_path
    return None

# Пошук у ширину (BFS)
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node in visited:
            continue
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    return None

# Застосування DFS і BFS для пошуку шляху між 'Station A' і 'Station E'
dfs_path = dfs(G, 'Station A', 'Station E')
bfs_path = bfs(G, 'Station A', 'Station E')

print(f"Шлях, знайдений за допомогою DFS: {dfs_path}")
print(f"Шлях, знайдений за допомогою BFS: {bfs_path}")