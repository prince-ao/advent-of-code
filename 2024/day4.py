def count_horizontal(i: int, j: int, puzzle: list[list[str]]) -> int:
    count = 0
    place = 0
    left = ['M', 'A', 'S']

    old_j = j

    j += 1

    while j < len(puzzle[i]) and place < len(left):
        if puzzle[i][j] != left[place]:
            break
        place += 1
        j += 1
    
    if place == len(left):
        count += 1

    j = old_j
    place = 0
    j -= 1

    while j >= 0 and place < len(left):
        if puzzle[i][j] != left[place]:
            break
        place += 1
        j -= 1
    
    if place == len(left):
        count += 1

    return count


def count_vertical(i: int, j: int, puzzle: list[list[str]]) -> int:
    count = 0
    place = 0
    left = ['M', 'A', 'S']

    old_i = i

    i += 1

    while i < len(puzzle) and place < len(left):
        if puzzle[i][j] != left[place]:
            break
        place += 1
        i += 1

    if place == len(left):
        count += 1

    i = old_i
    place = 0

    i -= 1

    while i >= 0 and place < len(left):
        if puzzle[i][j] != left[place]:
            break
        place += 1
        i -= 1
    
    if place == len(left):
        count += 1

    return count

def count_diagonal(i: int, j: int, puzzle: list[list[str]]) -> int:
    count = 0
    place = 0
    left = ['M', 'A', 'S']

    old_i = i
    old_j = j

    i += 1
    j += 1

    while i < len(puzzle) and j < len(puzzle[i]) and place < len(left):
        if puzzle[i][j] != left[place]:
            break
        place += 1
        i += 1
        j += 1

    if place == len(left):
        count += 1

    i = old_i
    j = old_j
    place = 0

    i += 1
    j -= 1


    while i < len(puzzle) and j >= 0 and place < len(left):
        if puzzle[i][j] != left[place]:
            break
        place += 1

        i += 1
        j -= 1
    
    if place == len(left):
        count += 1


    i = old_i
    j = old_j
    place = 0

    i -= 1
    j += 1

    while i >= 0 and j < len(puzzle[i]) and place < len(left):
        if puzzle[i][j] != left[place]:
            break
        place += 1

        i -= 1
        j += 1
    
    if place == len(left):
        count += 1


    i = old_i
    j = old_j
    place = 0

    i -= 1
    j -= 1

    while i >= 0 and j >= 0 and place < len(left):
        if puzzle[i][j] != left[place]:
            break
        place += 1

        i -= 1
        j -= 1
    
    if place == len(left):
        count += 1

    return count



def count_times(i: int, j: int, puzzle: list[list[str]]) -> int:
    count = 0

    count += count_horizontal(i, j, puzzle)
    count += count_vertical(i, j, puzzle)
    count += count_diagonal(i, j, puzzle)

    return count

def day4_1(puzzle: list[list[str]]) -> int:
    result = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == "X":
                result += count_times(i, j, puzzle)
    return result


def day4_2(puzzle: list[list[str]]) -> int:
    rows, cols = len(puzzle), len(puzzle[0])
    count = 0
    
    def is_mas(s: str) -> bool:
        return s in ['MAS', 'SAM']
    
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if puzzle[r][c] == 'A':
                top_left = puzzle[r-1][c-1] + puzzle[r][c] + puzzle[r+1][c+1]
                top_right = puzzle[r-1][c+1] + puzzle[r][c] + puzzle[r+1][c-1]
                
                if is_mas(top_left) and is_mas(top_right):
                    count += 1
    
    return count
