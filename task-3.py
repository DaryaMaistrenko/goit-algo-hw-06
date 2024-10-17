import networkx as nx
import matplotlib.pyplot as plt

# Створення графа з вагами для завдання 3
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

# Створимо граф із вагами
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
