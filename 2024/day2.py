def day2_1(l: list[list[int]]) -> int:
    counter = 0

    def is_valid(nums: list[int]) -> bool:
        diff = nums[1] - nums[0]

        if diff == 0:
            return False
        
        increase = diff > 0

        if abs(diff) > 3:
            return False
        
        for i in range(1, len(nums)):
            curr_diff = nums[i] - nums[i-1]

            if increase and diff <= 0:
                return False
            if not increase and diff >= 0:
                return False
            
            if abs(curr_diff) < 1 or abs(curr_diff) > 3:
                return False
            
        return True

    for row in l:
        if is_valid(row):
            counter += 1

    return counter


def day2_2(l: list[list[int]]) -> int:
    counter = 0
    
    def is_valid_sequence(nums: list[int]) -> int:
        if len(nums) < 2:
            return -1
            
        diff = nums[1] - nums[0]
        if abs(diff) < 1 or abs(diff) > 3:
            return 1
            
        increasing = diff > 0
        
        for i in range(2, len(nums)):
            curr_diff = nums[i] - nums[i-1]
            if abs(curr_diff) < 1 or abs(curr_diff) > 3:
                return i
            if (increasing and curr_diff <= 0) or (not increasing and curr_diff >= 0):
                return i
                
        return -1

    def check_sequence_with_dampener(nums: list[int]) -> bool:
        invalid_index = is_valid_sequence(nums)
        if invalid_index == -1:
            return True
            
        indices_to_try = {invalid_index - 1, invalid_index}
        if invalid_index < len(nums) - 1:
            indices_to_try.add(invalid_index + 1)
            
        for i in indices_to_try:
            if i < 0:
                continue
            new_sequence = nums[:i] + nums[i+1:]
            if is_valid_sequence(new_sequence) == -1:
                return True
                
        return False

    for row in l:
        if check_sequence_with_dampener(row):
            counter += 1
            
    return counter