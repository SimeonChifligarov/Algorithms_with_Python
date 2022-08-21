class Edge:
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node


def dfs(node, graph, visited, component):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    line = [int(el) for el in input().split()]
    node_one, node_two = line
    edge = Edge(node_one, node_two)
    graph[node_one].append(node_two)

# print(graph)

start_node = int(input())

visited = [False] * (nodes + 1)
component = []
dfs(start_node, graph, visited, component)

result = []

for node in range(1, nodes + 1):
    if node not in component:
        result.append(node)

print(*result)
