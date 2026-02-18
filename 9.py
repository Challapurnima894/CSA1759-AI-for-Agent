import itertools

def tsp(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    min_cost = float('inf')
    best_path = []

    for path in itertools.permutations(nodes):
        cost = 0
        current = start

        for city in path:
            cost += graph[current][city]
            current = city

        cost += graph[current][start]

        if cost < min_cost:
            min_cost = cost
            best_path = [start] + list(path) + [start]

    print("Minimum cost:", min_cost)
    print("Path:", best_path)

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

tsp(graph, 'A')
