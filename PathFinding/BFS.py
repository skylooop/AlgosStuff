from collections import deque

MAZE_ENV = [
    "##########",
    "# #     E#",
    "# # # ####",
    "# P # M  #",
    "### # ## #",
    "#   #    #"
    "## ## # ##",
    "#  #  #  #",
    "##########"
]

def is_valid(position):
    x, y = position
    
    return 0 <= x < len(MAZE_ENV[0]) \
        and 0 <= y < len(MAZE_ENV) \
        and MAZE_ENV[y][x] != "#"
        
def next_predator_states(position):
    x, y = position
    states = []
    
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        
        if is_valid((nx, ny)):
            states.append((nx, ny))
    return states

def next_states(state):
    t, m = state
    states = []
    
    for new_t in next_predator_states(t):
        new_m = next_minotaur_pos(new_t, m)
        
        if new_t == new_m:
            continue
        states.append((new_t, new_m))
    return states

def move_towards(m, t):
    return +1 if m < t else 0 if m == t else -1

def next_minotaur_pos(theseus, minotaur):
    tx, ty = theseus
    mx, my = minotaur
    
    for _ in range(2):
        dx = move_towards(mx, tx)
        if dx != 0 and is_valid((mx + dx, my)):
            mx += dx
            continue
        
        dy = move_towards(my, ty)
        if dy != 0 and is_valid((mx, my + dy)):
            my += dy
            continue
    return (mx, my)
    
def BFS(starting_state, stop_cond):
    queue = deque([starting_state])
    discovered = {starting_state: None}
    
    while len(queue) != 0:
        current = queue.popleft()
        
        if stop_cond(current):
            print("Found")
            path = [current]
            
            while discovered[current] is not None:
                current = discovered[current]
                path.append(current)
                
            for coordinate in reversed(path):
                print(coordinate)
            
        for next_state in next_states(current):
            if next_state not in discovered:
                queue.append(next_state)
                discovered[next_state] = current
    
    
def main():
    escape = None
    predator = None
    minatour = None
    
    for y, row in enumerate(MAZE_ENV):
        for x, char in enumerate(row):
            if char == "P":
                predator = (x, y)
            elif char == "E":
                escape = (x, y)
            elif char == "M":
                minatour = (x, y)
    BFS((predator, minatour), lambda state: state[0] == escape)
            
if __name__ == "__main__":
    main()