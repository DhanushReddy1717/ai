def print_state(state):
    print(state)
def is_goal(state, goal):
    return state == goal
def state_to_tuple(state):
    return tuple(tuple(stack) for stack in state)
def move_block(state, from_stack, to_stack):
    new_state = [stack[:] for stack in state]
    if not new_state[from_stack]:
        return None
    block = new_state[from_stack].pop()
    if to_stack == -1:
        new_state.append([block])
    else:
        new_state[to_stack].append(block)
    new_state = [s for s in new_state if s]
    return new_state
def block_world(initial, goal):
    visited = set()
    current = initial
    steps = 0
    print("\nInitial State:")
    print_state(current)
    while not is_goal(current, goal):
        visited.add(state_to_tuple(current))
        moved = False
        for i in range(len(current)):
            for j in range(len(current)):
                if i != j:
                    new_state = move_block(current, i, j)
                    if new_state and state_to_tuple(new_state) not in visited:
                        print(f"\nStep {steps+1}: Move block from stack {i} to {j}")
                        print_state(new_state)
                        current = new_state
                        steps += 1
                        moved = True
                        break
            if moved:
                break
        if not moved:
            for i in range(len(current)):
                new_state = move_block(current, i, -1)
                if new_state and state_to_tuple(new_state) not in visited:
                    print(f"\nStep {steps+1}: Move block from stack {i} to table")
                    print_state(new_state)
                    current = new_state
                    steps += 1
                    moved = True
                    break
        if not moved:
            print("\nNo solution found (stuck state).")
            return
    print("\nGoal State Reached!")
    print_state(current)

initial = eval(input("Enter initial state: "))
goal = eval(input("Enter goal state: "))

block_world(initial, goal)
