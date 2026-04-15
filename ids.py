def dls(graph, node, goal, depth, visited):
    if depth == 0 and node == goal:
        return [node]

    if depth > 0:
        visited.add(node)

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                path = dls(graph, neighbour, goal, depth - 1, visited)
                if path:
                    return [node] + path

    return None


def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        path = dls(graph, start, goal, depth, visited)

        if path:
            print("Path Found:", path)
            print("Depth:", depth)
            return

    print("Goal not found within depth limit")


# -------- MAIN PROGRAM --------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

start = 'A'
goal = 'F'
max_depth = 3

ids(graph, start, goal, max_depth)