from collections import deque

# Function to check if a state is already visited
def is_visited(state, visited):
    return state in visited

# BFS solution for Water Jug Problem
def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque()
    
    # Initial state (0, 0)
    queue.append((0, 0))
    
    while queue:
        a, b = queue.popleft()
        
        # If target reached
        if a == target or b == target:
            print("Solution found:")
            print((a, b))
            return
        
        if is_visited((a, b), visited):
            continue
        
        print("Visited:", (a, b))
        visited.add((a, b))
        
        # Possible next states
        next_states = [
            (jug1, b),       # Fill Jug1
            (a, jug2),       # Fill Jug2
            (0, b),          # Empty Jug1
            (a, 0),          # Empty Jug2
            # Pour Jug1 → Jug2
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),
            # Pour Jug2 → Jug1
            (a + min(b, jug1 - a), b - min(b, jug1 - a))
        ]
        
        for state in next_states:
            if state not in visited:
                queue.append(state)
    
    print("No solution found.")

# Example: Jug1 = 4L, Jug2 = 3L, Target = 2L
water_jug_bfs(4, 3, 2)
