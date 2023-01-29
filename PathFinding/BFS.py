from collections import deque

MAZE_ENV = [
    "##########",
    "# #     E#",
    "# # # ####",
    "# P #    #",
    "#   #    #",
    "## ## # ##",
    "#  #  #  #",
    "##########"
]

def is_valid(position):
    x, y = position
    
    return 0 <= x < len(MAZE_ENV[0]) \
        and 0 <= y < len(MAZE_ENV) \
        and MAZE_ENV[y][x] != "#"
        
def next_states(position):
    x, y = position
    states = []
    
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        
        if is_valid((nx, ny)):
            states.append((nx, ny))
    return states

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
    
    for y, row in enumerate(MAZE_ENV):
        for x, char in enumerate(row):
            if char == "P":
                predator = (x, y)
            elif char == "E":
                escape = (x, y)
    BFS(predator, lambda state: state == escape)
            
if __name__ == "__main__":
    main()