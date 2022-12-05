"""
Advent of Code 2022
Day 3: Rucksack Organization
"""
sacks = []
with open('day3.txt') as f:
    for line in f.read().splitlines():
        sacks.append(line)


def part1() -> int:
    """
    Part 1 of Day 3.
    Takes in the elves' sacks and splits it into a list for each half.
    Then, finds the shared character and adds it to the priority. Finally, returns total priority.
    """
    priority = 0
    split_sacks = []
    for i in sacks:
        split_sacks.append([
            i[0:len(i) // 2],  # first half
            i[len(i) // 2:len(i)]  # second half
        ])

    for sack in split_sacks:
        half1 = set(sack[0])
        half2 = set(sack[1])
        shared = ''.join(half1 & half2)
        if shared.isupper():
            priority += ord(shared) - 38
        else:
            priority += ord(shared) - 96
    return priority


def part2() -> int:
    """
    Part 2 of Day 3.
    Makes groups into lists of 3 elves' sacks, then finds the common character between
    each group, adding it to the new priority. Returns the total new priority.
    """
    new_priority = 0
    groups = []
    for i in range(len(sacks) // 3):  # the number of groups
        groups.append([
            sacks[3 * i],
            sacks[3 * i + 1],
            sacks[3 * i + 2]
        ])

    for group in groups:
        elf1 = set(group[0])
        elf2 = set(group[1])
        elf3 = set(group[2])

        shared = ''.join(elf1 & elf2 & elf3)
        if shared.isupper():
            new_priority += ord(shared) - 38
        else:
            new_priority += ord(shared) - 96
    return new_priority


if __name__ == '__main__':
    print("Part 1: " + str(part1()))
    print("Part 2: " + str(part2()))
