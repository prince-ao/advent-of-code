from functools import reduce
import operator
import re

def day3_1(inp: str) -> int:
    search = r"mul\(\d{1,3},\d{1,3}\)"
    result = 0

    for pat in re.findall(search, inp):
        result += reduce(operator.mul, [int(s) for s in pat[4:-1].split(",")])
    
    return result


def day3_2(inp: str) -> int:
    search = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    result = 0
    do = True


    for pat in re.findall(search, inp):
        if pat[:3] == "mul" and do:
            result += reduce(operator.mul, [int(s) for s in pat[4:-1].split(",")])
        elif pat == "don't()":
            do = False
        elif pat == "do()":
            do = True
    
    return result
