import sys
import math
from pprint import pprint
from functools import lru_cache

D = [list(line) for line in sys.stdin.read().strip().split("\n")]

def part_1():
    count = 0
    splits = set()
    splits.add((0, len(D[0]) // 2))
    
    for row in range(1, len(D)):
        new_splits = set()
        for x, y in splits:
            if D[row][y] == '^':
                count += 1
                new_splits.add((row, y - 1))
                new_splits.add((row, y + 1))
            elif D[row][y] == '.':
                new_splits.add((row, y))

        splits = new_splits

    return count
    
    
def part_2():
    @lru_cache(maxsize=None)
    def navigate(row = 1, col = len(D[0]) // 2):
        if row == len(D) - 1:
            return 1
        
        timelines = 0
        if D[row][col] == "^":
            timelines += navigate(row + 1, col - 1) + navigate(row + 1, col + 1)
        elif D[row][col] == ".":
            timelines += navigate(row + 1, col)

        return timelines
    
    return navigate()

if __name__ == "__main__":
    # print(part_1())
    print(part_2())
