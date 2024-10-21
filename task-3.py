import heapq
import matplotlib.pyplot as plt
import networkx as nx

# Створення графа з вагами для завдання 3
weighted_edges = [
    ('Station A', 'Station B', 7),
    ('Station A', 'Station C', 9),
    ('Station B', 'Station D', 10),
    ('Station C', 'Station D', 6),
    ('Station D', 'Station E', 5),
    ('Station E', 'Station F', 2),
    ('Station B', 'Station F', 15)
]

# Створимо граф у вигляді словника
graph = {
    'Station A': {'Station B': 7, 'Station C': 9},
    'Station B': {'Station A': 7, 'Station D': 10, 'Station F': 15},
    'Station C': {'Station A': 9, 'Station D': 6},
    'Station D': {'Station B': 10, 'Station C': 6, 'Station E': 5},
    'Station E': {'Station D': 5, 'Station F': 2},
    'Station F': {'Station E': 2, 'Station B': 15}
}

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація початкових змінних
    shortest_paths = {vertex: float('inf') for vertex in graph}  # Всі шляхи нескінченні
    shortest_paths[start] = 0  # Відстань до стартової точки = 0
    previous_nodes = {vertex: None for vertex in graph}  # Для збереження попередніх вершин
    priority_queue = [(0, start)]  # Містить (відстань, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Обробляємо кожного сусіда поточного вузла
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда, оновлюємо
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths, previous_nodes

# Функція для побудови шляху
def get_shortest_path(previous_nodes, start, goal):
    path = []
    current_node = goal
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    return path

# Використання алгоритму Дейкстри для пошуку найкоротшого шляху між 'Station A' і 'Station F'
start_node = 'Station A'
goal_node = 'Station F'

shortest_paths, previous_nodes = dijkstra(graph, start_node)
shortest_path = get_shortest_path(previous_nodes, start_node, goal_node)

# Виведення результатів
print(f"Найкоротший шлях з {start_node} до {goal_node}: {shortest_path}")
print(f"Довжина шляху: {shortest_paths[goal_node]}")

# Візуалізація графа з вагами
G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from(weighted_edges)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G_weighted)
nx.draw(G_weighted, pos, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=700)
edge_labels = nx.get_edge_attributes(G_weighted, 'weight')
nx.draw_networkx_edge_labels(G_weighted, pos, edge_labels=edge_labels)
plt.title("Transport Network Graph (З вагами)")
plt.show()
