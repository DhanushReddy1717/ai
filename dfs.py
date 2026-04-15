def dfs(graph, start, visited):
    visited.add(start)
    print(start, end=" ")

    for neighbour in graph.get(start, []):  # safe access
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


# -------- MAIN PROGRAM --------
n = int(input("Enter number of vertices: "))
graph = {}

for i in range(n):
    node = input("Enter node: ")
    neighbours = input(f"Enter neighbours of {node} (space separated): ").split()
    graph[node] = neighbours

start_node = input("Enter starting node: ")

print("DFS Traversal:", end=" ")
visited = set()
dfs(graph, start_node, visited)