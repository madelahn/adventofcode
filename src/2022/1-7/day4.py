"""
Advent of Code 2022
Day 4: Camp Cleanup
"""
pairs = []
with open('day4.txt') as f:
    for line in f.read().splitlines():
        elves = line.split(',')
        pair = []
        for elf in elves:
            elf_values = elf.split('-')
            elf_range = [i for i in (range(int(elf_values[0]), int(elf_values[1]) + 1))]
            pair.append(elf_range)
        pairs.append(pair)


def part1() -> int:
    """
    Part 1 of Day 4.
    Checks if the two elves in each pair are subsets of one another,
    and then adds 1 if True.
    Returns the number of pairs that are subsets of one another.
    """
    full_range = 0
    for group in pairs:
        elf1 = set(group[0])
        elf2 = set(group[1])
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            full_range += 1
    return full_range


def part2() -> int:
    """
    Part 2 of Day 4.
    Checks if the two elves in each pair have an intersection,
    and then adds 1 if True.
    Returns the number of pairs that share values.
    """
    new_range = 0
    for group in pairs:
        elf1 = set(group[0])
        elf2 = set(group[1])
        if elf1 & elf2:
            new_range += 1
    return new_range


if __name__ == '__main__':
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))



