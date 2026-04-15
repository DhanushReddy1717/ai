import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    visited = set()
    pq = [(heuristic[start], start, [start])]  # (heuristic, node, path)

    while pq:
        h, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Path Found:", path)
            return

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                heapq.heappush(pq, (heuristic[neighbour], neighbour, path + [neighbour]))

    print("Goal not reachable")


# -------- MAIN PROGRAM --------
n = int(input("Enter number of vertices: "))
graph = {}

for i in range(n):
    node = input("Enter node: ")
    neighbours = input(f"Enter neighbours of {node} (space separated): ").split()
    graph[node] = neighbours

heuristic = {}
print("Enter heuristic values:")
for i in range(n):
    node = input("Node: ")
    h = int(input("Heuristic value: "))
    heuristic[node] = h

start = input("Enter start node: ")
goal = input("Enter goal node: ")

greedy_best_first_search(graph, heuristic, start, goal)