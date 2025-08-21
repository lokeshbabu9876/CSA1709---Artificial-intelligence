from collections import deque

# State is represented as (M_left, C_left, Boat_side, M_right, C_right)
# Boat_side = 'L' (left) or 'R' (right)

def is_valid(state):
    M_left, C_left, _, M_right, C_right = state
    if (M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0):
        return False
    if (M_left > 0 and M_left < C_left):
        return False
    if (M_right > 0 and M_right < C_right):
        return False
    return True

def get_successors(state):
    M_left, C_left, boat, M_right, C_right = state
    successors = []
    
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]  # (Missionaries, Cannibals)
    
    for M, C in moves:
        if boat == 'L':  # Move from left to right
            new_state = (M_left - M, C_left - C, 'R', M_right + M, C_right + C)
        else:  # Move from right to left
            new_state = (M_left + M, C_left + C, 'L', M_right - M, C_right - C)
        
        if is_valid(new_state):
            successors.append(new_state)
    return successors

def bfs(start, goal):
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        visited.add(state)
        
        for successor in get_successors(state):
            if successor not in visited:
                queue.append((successor, path + [successor]))
    return None

# Initial state: 3 missionaries, 3 cannibals, boat on left
start = (3, 3, 'L', 0, 0)
goal = (0, 0, 'R', 3, 3)

solution = bfs(start, goal)

if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
