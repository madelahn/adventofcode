def check_safe(line):
    asc = True if line[1] - line[0] > 0 else False

    for i in range(1, len(line)):
        diff = line[i] - line[i-1]
        if (asc and diff < 0) or (not asc and diff > 0) or not (1 <= abs(diff) <= 3):
            return False
    return True


def part1():
    f = open('input/day2.txt', 'r')
    num_safe = 0

    for l in f:
        line = [int(x) for x in l.split()]
        if check_safe(line):
            num_safe += 1
    print("Part 1 Solution: " + str(num_safe))


def part2():
    f = open('input/day2.txt', 'r')
    num_safe = 0

    for l in f:
        line = [int(x) for x in l.split()]
        if check_safe(line):
            num_safe += 1
        # See if dampening makes the line safe
        else:
            for i in range(len(line)):
                # Take out one element from the line
                dampened_line = line[:i] + line[i+1:]
                if check_safe(dampened_line):
                    num_safe += 1
                    break

    print("Part 2 Solution: " + str(num_safe))


if __name__ == "__main__":
    part1()
    part2()
