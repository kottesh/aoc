import sys

D = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in sys.stdin.read().strip().split("\n")]

def part_1():
    ans = float("-inf")

    for x in D:
        for y in D:
            if x != y and x[0] != y[0] and x[1] != y[1]:
                w = abs(x[0] - y[0]) + 1
                h = abs(x[1] - y[1]) + 1
                a = w * h
                ans = max(ans, a)

    return ans

if __name__ == "__main__":
    print(part_1())
