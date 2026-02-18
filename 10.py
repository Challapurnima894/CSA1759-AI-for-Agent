def a_star(graph, heuristic, start, goal):
    open_set = {start}
    closed_set = set()

    g = {start: 0}
    parent = {start: None}

    while open_set:
        current = min(open_set, key=lambda x: g[x] + heuristic[x])

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Path:", path)
            return

        open_set.remove(current)
        closed_set.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor in closed_set:
                continue

            new_g = g[current] + cost

            if neighbor not in open_set or new_g < g.get(neighbor, float('inf')):
                g[neighbor] = new_g
                parent[neighbor] = current
                open_set.add(neighbor)

    print("Path not found")

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 2},
    'F': {}
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0
}

a_star(graph, heuristic, 'A', 'F')
