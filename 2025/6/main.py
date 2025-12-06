import sys
import re

D = [line for line in sys.stdin.read().strip().split("\n")]

nums = D[:-1]
ops = re.split(r"\s+", D[-1])

def prod(nums):
    x = 1
    for num in nums:
        x *= num

    return x

def part_1():
    global nums
    nums = [list(map(int, line.split())) for line in nums]
    total = 0 
    
    for col in range(len(ops)):
        nos = [num[col] for num in nums]
        total += prod(nos) if ops[col] == "*" else sum(nos)

    return total

def part_2():
    global nums
    nums = list(map(list, nums)) 
    total = 0
    
    idx = len(nums[0]) - 1
    nos = []
    while idx >= 0: 
        s = "".join(line[idx] for line in nums)

        if n := s.strip():
            nos.append(int(n))
        
        if not s.strip() or idx == 0:
            op = ops.pop()
            total += prod(nos) if op == "*" else sum(nos)
            nos.clear()
        
        idx -= 1
    
    return total


if __name__ == "__main__":
    # print(part_1())
    print(part_2())
