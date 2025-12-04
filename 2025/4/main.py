import sys
import copy

grid = [list(line) for line in sys.stdin.read().strip().split("\n")]
copy_grid = copy.deepcopy(grid)

def remove_rolls():
    count = 0
    visited = set() 
    stack = [(0, 0)]
    visited.add((0, 0))

    while stack:
        curr = stack.pop()

        dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)] # 8 directions
        
        near_rolls = 0
        for x, y in dirs:
            if 0 <= curr[0] + x < len(grid) and 0 <= curr[1] + y < len(grid[0]) and grid[curr[0] + x][curr[1] + y] == '@':
                near_rolls += 1

        if near_rolls < 4 and grid[curr[0]][curr[1]] == "@":
            count += 1
            copy_grid[curr[0]][curr[1]] = 'x'

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            x, y = curr[0] + dx, curr[1] + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited:
                visited.add((x, y))
                stack.append((x, y))

    return count

def part_1():
    return remove_rolls() 

def part_2():
    global grid
    count = 0
    
    while cnt:= remove_rolls():
        count += cnt
        grid = copy.deepcopy(copy_grid)
    
    return count

if __name__ == "__main__":
    # print(part_1())
    print(part_2())
    
