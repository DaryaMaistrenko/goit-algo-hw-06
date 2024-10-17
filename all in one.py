## З'єднаний код для всіх трьох завдань:

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Створення графа для завдань 1 і 2 (без ваг)
G = nx.Graph()

# Додавання вершин (районів або станцій)
nodes = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F']
G.add_nodes_from(nodes)

# Додавання ребер (маршрутів між районами)
edges = [
    ('Station A', 'Station B'),
    ('Station A', 'Station C'),
    ('Station B', 'Station D'),
    ('Station C', 'Station D'),
    ('Station D', 'Station E'),
    ('Station E', 'Station F'),
    ('Station B', 'Station F')
]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700)
plt.title("Transport Network Graph (Без ваг)")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, centrality in degree_centrality.items():
    print(f"{node}: {centrality:.2f}")

# Завдання 2: Реалізація алгоритмів DFS і BFS
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

# Завдання 3: Алгоритм Дейкстри з вагами
# Додавання ваг до ребер (ваги можуть представляти довжину маршруту)
weighted_edges = [
    ('Station A', 'Station B', 7),
    ('Station A', 'Station C', 9),
    ('Station B', 'Station D', 10),
    ('Station C', 'Station D', 6),
    ('Station D', 'Station E', 5),
    ('Station E', 'Station F', 2),
    ('Station B', 'Station F', 15)
]

# Створимо граф із вагами для завдання 3
G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from(weighted_edges)

# Візуалізація графа з вагами
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G_weighted)  # Фіксуємо позиції для візуалізації
nx.draw(G_weighted, pos, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=700)
edge_labels = nx.get_edge_attributes(G_weighted, 'weight')
nx.draw_networkx_edge_labels(G_weighted, pos, edge_labels=edge_labels)
plt.title("Transport Network Graph (З вагами)")
plt.show()

# Алгоритм Дейкстри для пошуку найкоротшого шляху
def dijkstra(graph, start, goal):
    return nx.dijkstra_path(graph, start, goal), nx.dijkstra_path_length(graph, start, goal)

# Застосування Дейкстри для пошуку шляху між 'Station A' і 'Station F'
dijkstra_path, dijkstra_length = dijkstra(G_weighted, 'Station A', 'Station F')

print(f"Найкоротший шлях за Дейкстрою: {dijkstra_path}")
print(f"Довжина шляху: {dijkstra_length}")
