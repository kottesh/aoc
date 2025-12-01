import sys

rotations = []
curr = 50

for line in sys.stdin.read().split():
    rotations.append((line[0], int(line[1: ])))

def part_1():
    global curr
    ans = 0

    for dir, value in rotations:
        if dir == 'L':
            value = -value
        curr = (curr + value) % 100

        if curr == 0:
            ans += 1

    return ans

def part_2():
    global curr
    ans = 0

    for dir, value in rotations:
        # move step-by-step
        for _ in range(value):
            if dir == "L":
                curr = (curr - 1) % 100
            else:
                curr = (curr + 1) % 100

            if curr == 0:
                ans += 1

    return ans


if __name__ == "__main__":
    # print(part_1())
    print(part_2())

