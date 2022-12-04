"""
Advent of Code 2022
Day 1: Calorie Counting
"""

# Reads the text file and creates the lists used for Part 1 and 2.
elfList = []
with open('day1.txt') as f:
    lines = f.read().splitlines()
    lst = []
    for line in lines:
        if line.strip() == '':
            elfList.append(lst)
            lst = []
        else:
            lst.append(int(line))
    elfList.append(lst)

listSums = [sum(elf) for elf in elfList]


def part1() -> int:
    """
    Part 1 of Day 1.
    Takes in all sums of the elves' calories and returns the highest value.
    """
    highest = 0
    for oneSum in listSums:
        if oneSum > highest:
            highest = oneSum
    return highest


def part2() -> int:
    """
    Part 2 of Day 1.
    Takes the top 3 elves' calorie amounts and returns the sum.
    """
    top_lst = sorted(listSums, reverse=True)
    top_calories = 0
    for i in range(0, 3):
        top_calories += top_lst[i]
    return top_calories


if __name__ == '__main__':
    print("Part 1: " + str(part1()))
    print("Part 2: " + str(part2()))
