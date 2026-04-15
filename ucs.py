import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [])]   # (cost, node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == goal:
            print("Least Cost Path:", path)
            print("Total Cost:", cost)
            return

        for neighbour, weight in graph.get(node, []):
            if neighbour not in visited:
                heapq.heappush(pq, (cost + weight, neighbour, path))

    print("Goal not reachable")


# -------- MAIN PROGRAM --------
n = int(input("Enter number of vertices: "))
graph = {}

for i in range(n):
    node = input("Enter node: ")
    neighbours_count = int(input(f"Enter number of neighbours of {node}: "))
    graph[node] = []

    for j in range(neighbours_count):
        neighbour, cost = input("Enter neighbour and cost: ").split()
        graph[node].append((neighbour, int(cost)))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

ucs(graph, start, goal)