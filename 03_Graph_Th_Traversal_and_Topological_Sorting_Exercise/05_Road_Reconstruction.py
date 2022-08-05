def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count)]

# edges = set()
edges = []

for _ in range(edges_count):
    first, second = [int(el) for el in input().split(' - ')]
    graph[first].append(second)
    graph[second].append(first)
    # edges.add((min(first, second), max(first, second)))
    edges.append((min(first, second), max(first, second)))

important_streets = []

for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * nodes_count
    dfs(0, graph, visited)

    if not all(visited):
        important_streets.append((first, second))

    graph[first].append(second)
    graph[second].append(first)

# print(important_streets)

print('Important streets:')
[print(first, second) for (first, second) in important_streets]
