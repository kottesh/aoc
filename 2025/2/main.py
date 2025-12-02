import sys
import re

prod_id_ranges = [
    (int(item.split("-")[0]), int(item.split("-")[1])) for item in sys.stdin.read().strip().split(",")
]
print(prod_id_ranges)

def part_1():
    ans = 0
    for start, end in prod_id_ranges:
        for i in range(start, end + 1):
            num = str(i)
            mid = len(num) // 2

            if num[:mid] == num[mid:]:
                ans += i
    
    return ans

def part_2():
    ans = 0

    # for start, end in prod_id_ranges:
    #     for i in range(start, end + 1):
    #         num = str(i)
    #         if re.fullmatch(r"(.+)\1+", num):
    #             ans += i

    for start, end in prod_id_ranges:
        for i in range(start, end + 1):
            num = str(i)
            
            def repeating(s):
                for size in range(1, len(num) // 2 + 1):
                    if s == s[:size] * (len(num) // size):
                        return True

                return False
            
            if repeating(num):
                ans += i
    
    return ans

if __name__ == "__main__":
    # print(part_1())
    print(part_2())

