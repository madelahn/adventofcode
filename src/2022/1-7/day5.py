"""
Advent of Code 2022
Day 5: Supply Stacks
"""
import pprint as pp

file = open('day5.txt')
f = file.read().splitlines()
file.close()

# Gets stacks
stacks = []
for i in range(0, 9):  # column
    temp_stack = []
    for line in f[0:8]:  # row
        crate = line.rstrip().split(',')[i]
        if crate != '[ ]':
            temp_stack.append(crate)
    stacks.append(temp_stack)

# Gets moves
moves = []
for line in f[10:]:
    print(line)
    temp_move = line.rstrip().split(' ')
    add_move = []
    for i in temp_move:
        if not i.isalpha():
            add_move.append(int(i))
    moves.append(add_move)

# pp.pprint(stacks)
print(moves)


def part1() -> list:
    top_crates = []
    for m in moves:
        print(m[2], "'s old # of crates: ", len(stacks[m[2]]))

        for _ in range(0, m[0]):  # number of boxes moved
            stacks[m[2]].insert(0, stacks[m[1]][0])  # inserts top box from m[1] to m[2]

            if len(stacks[m[1]]) == 0:
                pass
            else:
                stacks[m[1]].pop(0)  # gets rid of the top box from m[1]

        print(m[2], "'s new # of crates: ", len(stacks[m[2]]))

    for new_stack in stacks:
        if len(new_stack) == 0:
            pass
        else:
            top_crates.append(new_stack[0])
    return top_crates


if __name__ == '__main__':
    print(part1())
