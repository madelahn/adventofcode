import re

def part1():
    f = open('input/day3.txt', 'r').read()

    mults = re.findall(
        r"""        
            mul\(       # "mul("
                (\d+)   # First num
                ,       # ,
                (\d+)   # Second num
            \)          # ")"
        """,        
        f, re.VERBOSE
    )
    total_sum = sum(int(x) * int(y) for x, y in mults)    

    print("Part 1 Solution: " + str(total_sum))


def part2():
    f = open('input/day3.txt', 'r').read()

    commands = re.findall(
        r"""        
            mul\((\d+),(\d+)\)  # "mul(x,y)", index 0 and 1
            |                   #
            (don't\(\))         # "don't()", index 2
            |                   #
            (do\(\))            # "do()", index 3
        """,        
        f, re.VERBOSE
    )

    total_sum = 0
    do = True
    for i in commands:
        if do and i[0]:
            total_sum += int(i[0]) * int(i[1])
        elif i[2]:
            do = False
        elif i[3]:
            do = True

    print("Part 2 Solution: " + str(total_sum))


if __name__ == "__main__":
    part1()
    part2()