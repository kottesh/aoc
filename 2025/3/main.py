import sys

bank = [battery for battery in sys.stdin.read().strip().split()]

def part_1():
    ans = 0
    
    for battery in bank:
        l_max = float('-inf')
        for i in range(1, len(battery)):
            l_max = max(l_max, int(max(battery[:i]) + max(battery[i:])))
        ans += l_max

    return ans

def part_2():
    ans = 0
    
    # this will take a zillion year to get the result.
    # max_joltage = ""
    # def findSubSeq(idx, s, curr=""):
    #     nonlocal max_joltage
    #     if idx == len(s):
    #         if len(curr) == 12:
    #             print(curr)
    #             max_joltage = max(int(max_joltage or 0), int(curr))
    #         return

    #     curr += s[idx]

    #     findSubSeq(idx + 1, s, curr)

    #     curr = curr[:-1]

    #     findSubSeq(idx + 1, s, curr)

    # for battery in bank:
    #     max_joltage = ""
    #     findSubSeq(0, battery)
    #     if max_joltage != "":
    #         ans += int(max_joltage)
    
    for battery in bank:
        stack = []
        for idx, item in enumerate(battery):
            while stack and (len(battery) - idx) > (12 - len(stack)) and item > stack[-1]:
                stack.pop()
            if len(stack) < 12:
                stack.append(item)
            
        ans += int("".join(stack))

    return ans

if __name__ == "__main__":
    # print(part_1())
    print(part_2())

