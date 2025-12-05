import sys

D = [line for line in sys.stdin.read().split("\n\n")] 
fresh_ids = [[int(rng.split("-")[0]), int(rng.split("-")[1])] for rng in D[0].split("\n")] 
avl_ids = [int(id) for id in D[1].split("\n")]

def part_1():
    count = 0

    for id in avl_ids:
        for rng in fresh_ids:
            if rng[0] <= id <= rng[1]:
                count += 1
                break

    return count

def part_2():
    fresh_ids.sort()
    fresh = []
    count = 0
    
    for rng in fresh_ids:
        if not fresh:
            fresh.append(rng)
            continue
        if fresh[-1][1] >= rng[0]:
            fresh[-1][1] = max(fresh[-1][1], rng[1])
        else:
            fresh.append(rng)

    for rng in fresh:
        count += rng[1] - rng[0] + 1

    return count

if __name__ == "__main__":
    print(part_1())
    print(part_2())

