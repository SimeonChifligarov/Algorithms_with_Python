from collections import deque


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __repr__(self):
        return f'{self.first} -> {self.second}; {self.weight}'


trading_pairs = int(input())

graph = []
# print(graph)
all_edges = []

mapping = {}

i = 0
for _ in range(trading_pairs):
    line = input().split()
    from_currency, to_currency, price = line[0], line[1], float(line[2])
    edge = Edge(from_currency, to_currency, -price)

    if from_currency not in mapping:
        mapping[from_currency] = i
        i += 1

    graph.append(edge)
    all_edges.append(edge)

# print(graph)
# print(mapping)

target_currency = input()
possible_end_nodes = []
for edge in all_edges:
    if edge.second == target_currency:
        possible_end_nodes.append(mapping[edge.first])
# print(possible_end_nodes)

start_node_index = mapping[target_currency]

real_result = 1
real_path = []

nodes = len(mapping)
distance = [float('inf')] * (nodes + 1)
distance[start_node_index] = 1

parent = [None] * (nodes + 1)

for _ in range(nodes - 1):
    updated = False
    for edge in graph:
        if distance[mapping[edge.first]] == float('inf'):
            continue
        new_distance = -1 * abs(distance[mapping[edge.first]] * edge.weight)
        if new_distance < distance[mapping[edge.second]]:
            distance[mapping[edge.second]] = new_distance
            parent[mapping[edge.second]] = mapping[edge.first]
            updated = True

    if not updated:
        break

# print(distance)
# print(parent)
# print(possible_end_nodes)

real_result = -1
reap_path = []

for target in possible_end_nodes:
    path = deque()
    node = target
    parent[mapping[target_currency]] = None
    while node is not None:
        for k, v in mapping.items():
            if v == node:
                path.appendleft(k)
        node = parent[node]
    path.append(target_currency)

    if distance[mapping[target_currency]] < real_result:
        print('True')
        print(*path)

    else:
        distance[mapping[target_currency]] = -1
        print('False')
        for currency in mapping:
            print(f'{currency}: {-distance[mapping[currency]]:.3f}')
