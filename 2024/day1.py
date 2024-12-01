from collections import defaultdict

def day1_1(s: str) -> int:
    left: list[int] = []
    right: list[int]  = []
    result = 0

    for row in s.split('\n'):
        if row == '':
            continue
        nums = row.split("   ")

        left.append(int(nums[0]))
        right.append(int(nums[1]))

    left.sort()
    right.sort()

    for l, r in zip(left, right):
        result += abs(l - r)

    return result

def day1_2(s: str) -> int:
    result = 0

    left: list[int] = []
    right_map: dict[int, int] = defaultdict(int)

    for row in s.split('\n'):
        if row == '':
            continue
        nums = row.split("   ")

        left.append(int(nums[0]))
        right_map[int(nums[1])] += 1
    
    for l in left:
        result += l * right_map[l]
    
    return result
