def part1():
    list_a = []
    list_b = []

    f = open('day1.txt', 'r')
    for line in f:
        ints = line.split('   ')
        list_a.append(int(ints[0]))
        list_b.append(int(ints[1]))
    f.close()
    
    list_a.sort()
    list_b.sort()

    distance = 0
    for i in range(len(list_a)):
        distance += abs(list_a[i] - list_b[i])
    
    print("Part 1 Solution: " + str(distance) + "\n")


def part2():
    list_a = []
    list_b = []

    f = open('day1.txt', 'r')
    for line in f:
        ints = line.split('   ')
        list_a.append(int(ints[0]))
        list_b.append(int(ints[1]))
    f.close()

    # Store counts of each number in list_b as dict
    count_b = {}
    for num in list_b:
        if num in count_b:
            count_b[num] += 1
        else:
            count_b[num] = 1
    
    sim = 0
    for num in list_a:
        if num in count_b:
            sim += num * count_b[num]

    print("Part 2 Solution: " + str(sim) + "\n")


if __name__ == "__main__":
    part1()
    part2()