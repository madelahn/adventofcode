"""
Advent of Code 2022
Day 2: Rock Paper Scissors
"""

# Reads the text file and creates the lists used in part 1 and 2.
moves = []
with open('day2.txt') as f:
    for line in f.read().splitlines():
        moves.append([i for i in line if i.strip() != ''])


def part1() -> int:
    """
    Part 1 of Day 2.
    Takes each set of moves and determines the number of points for each round.
    Returns the total score.
    """
    total_score = 0

    for move in moves:
        if move[1] == 'X':  # rock
            if move[0] == 'A':  # tie
                total_score += 3
            elif move[0] == 'B':  # loss
                pass
            else:  # win
                total_score += 6
            total_score += 1

        if move[1] == 'Y':  # paper
            if move[0] == 'A':  # win
                total_score += 6
            elif move[0] == 'B':  # tie
                total_score += 3
            else:  # loss
                pass
            total_score += 2

        if move[1] == 'Z':  # scissors
            if move[0] == 'A':  # loss
                pass
            elif move[0] == 'B':  # win
                total_score += 6
            else:  # tie
                total_score += 3
            total_score += 3

    return total_score


def part2() -> int:
    """
    Part 2 of Day 2.
    Similar to Part 1, but instead calculate using X,Y,Z as status (W/T/L) instead of the move.
    Returns the new total score.
    """
    new_score = 0

    for move in moves:
        if move[1] == 'X':  # loss
            if move[0] == 'A':  # rock/scissors
                new_score += 3
            elif move[0] == 'B':  # paper/rock
                new_score += 1
            else:  # scissors/paper
                new_score += 2

        if move[1] == 'Y':  # tie
            if move[0] == 'A':  # rock/rock
                new_score += 1
            elif move[0] == 'B':  # paper/paper
                new_score += 2
            else:  # scissors/scissors
                new_score += 3
            new_score += 3

        if move[1] == 'Z':  # win
            if move[0] == 'A':  # rock/paper
                new_score += 2
            elif move[0] == 'B':  # paper/scissors
                new_score += 3
            else:  # scissors/rock
                new_score += 1
            new_score += 6

    return new_score


if __name__ == '__main__':
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))
