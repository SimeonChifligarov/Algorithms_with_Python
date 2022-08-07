# Kruskal's Algorithm
nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    first, second, weight = [int(el) for el in input().split(' - ')]
    graph.append((first, second, weight))

parent = [num for num in range(nodes)]
total_cost = 0


def find_root(parent, node):
    while not node == parent[node]:
        node = parent[node]
    return node


for first, second, weight in sorted(graph, key=lambda t: t[2]):
    first_node_root = find_root(parent, first)
    second_node_root = find_root(parent, second)

    if first_node_root == second_node_root:
        continue

    parent[first_node_root] = second_node_root
    total_cost += weight

print(f'Total cost: {total_cost}')
