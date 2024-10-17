import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
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
plt.title("Transport Network Graph")
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

