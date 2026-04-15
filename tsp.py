import copy

def calculate_cost(tour, distance):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance[tour[i]][tour[i + 1]]

    cost += distance[tour[-1]][tour[0]]
    return cost

def generate_neighbors(tour):
    neighbors = []
    for i in range(1, len(tour) - 1):
        for j in range(i + 1, len(tour)):
            new_tour = copy.deepcopy(tour)
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            neighbors.append(new_tour)
    return neighbors

def hill_climbing(distance):
    n = len(distance)
    
    current_tour = list(range(n))
    current_cost = calculate_cost(current_tour, distance)

    print("\nInitial Tour:", current_tour)
    print("Initial Cost:", current_cost)
    print("-" * 50)

    while True:
        neighbors = generate_neighbors(current_tour)

        best_neighbor = current_tour
        best_neighbor_cost = current_cost

        for neighbor in neighbors:
            cost = calculate_cost(neighbor, distance)
            print("Checking Neighbor:", neighbor, "Cost:", cost)

            if cost < best_neighbor_cost:
                best_neighbor = neighbor
                best_neighbor_cost = cost

        print("-" * 50)

        if best_neighbor_cost >= current_cost:
            break
        
        current_tour = best_neighbor
        current_cost = best_neighbor_cost
        print("Move Accepted")
        print("New Tour:", current_tour)
        print("New Cost:", current_cost)
        print("-" * 50)
    return current_tour, current_cost
if __name__ == "__main__":
    n = int(input("Enter number of cities: "))

    print("Enter distance matrix row by row:")
    distance = []

    for i in range(n):
        row = list(map(int, input().split()))
        distance.append(row)

    final_tour, final_cost = hill_climbing(distance)

    print("\nFinal Solution")
    print("Best Tour:", final_tour)
    print("Best Cost:", final_cost)
