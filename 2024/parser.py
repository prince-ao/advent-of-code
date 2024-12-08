def day2(s: str) -> list[list[int]]:
    return [[int(num) for num in row.split(" ")] for row in s.split('\n') if row != '']

def day4(s: str) -> list[list[str]]:
    return [[c for c in row] for row in s.split('\n') if row != '']