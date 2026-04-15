import heapq

def astar(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start, [start])]  # (f, g, node, path)
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Optimal Path:", path)
            print("Total Cost:", g)
            return

        for neighbour, cost in graph.get(node, []):
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(pq, (new_f, new_g, neighbour, path + [neighbour]))

    print("Goal not reachable")


# -------- MAIN PROGRAM --------
n = int(input("Enter number of vertices: "))
graph = {}

for i in range(n):
    node = input("Enter node: ")
    neighbours = int(input(f"Enter number of neighbours of {node}: "))
    graph[node] = []

    for j in range(neighbours):
        neighbour, cost = input("Enter neighbour and cost: ").split()
        graph[node].append((neighbour, int(cost)))

heuristic = {}
print("Enter heuristic values:")
for i in range(n):
    node = input("Node: ")
    h = int(input("Heuristic value: "))
    heuristic[node] = h

start = input("Enter start node: ")
goal = input("Enter goal node: ")

astar(graph, heuristic, start, goal)