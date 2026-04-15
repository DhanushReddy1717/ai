import heapq
import math

def is_solvable(capA, capB, target):
    """Check if solution is mathematically possible"""
    if target > max(capA, capB):
        return False
    return target % math.gcd(capA, capB) == 0

def water_jug_a_star(capA, capB, target):
    start = (0, 0)

    pq = []
    heapq.heappush(pq, (0, 0, start, []))
    
    visited = set()

    while pq:
        f, g, (a, b), path = heapq.heappop(pq)
        
        # Goal check
        if a == target or b == target:
            return path + [(a, b)]
        
        if (a, b) in visited:
            continue
        
        visited.add((a, b))

        next_states = [
            (capA, b), # Fill A
            (a, capB), # Fill B
            (0, b), # Empty A
            (a, 0), # Empty B
            # Pour A -> B
            (a - min(a, capB - b), b + min(a, capB - b)),
            # Pour B -> A
            (a + min(b, capA - a), b - min(b, capA - a))
        ]
        
        for na, nb in next_states:
            if (na, nb) not in visited:
                h = min(abs(na - target), abs(nb - target))
                heapq.heappush(
                pq,
                (g + 1 + h, g + 1, (na, nb), path + [(a, b)]))
    return None
if __name__ == "__main__":
    print("\nWATER JUG PROBLEM USING A* ALGORITHM\n")
    
    capA = int(input("Enter capacity of Jug A: "))
    capB = int(input("Enter capacity of Jug B: "))
    target = int(input("Enter target amount: "))
    
    if not is_solvable(capA, capB, target):
        print("\nNo solution possible mathematically.")
    else:
        solution = water_jug_a_star(capA, capB, target)
        
        if solution:
            print("\nSolution Steps:")
            step = 0
            for a, b in solution:
                print(f"Step {step}: Jug A = {a}, Jug B = {b}")
                step += 1
        else:
            print("\nNo solution found.")
