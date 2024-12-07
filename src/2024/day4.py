def part1():
    f = open('input/day4.txt', 'r')
    board = []
    for l in f:
        board.append(list(l.strip()))

    appearances = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if (board[y][x] == 'X'):
                appearances += 1 if ''.join(board[y][x : x+4]) == "XMAS" else 0  # Right
                appearances += 1 if ''.join(board[y][x-3 : x+1]) == "SAMX" else 0  # Left
                # Down
                if y+3 < len(board):
                    appearances += 1 if ''.join([board[y+i][x] for i in range(4)]) == "XMAS" else 0
                    # Down Right
                    if x+3 < len(board[y]):
                        appearances += 1 if ''.join([board[y+i][x+i] for i in range(4)]) == "XMAS" else 0
                    # Down Left
                    if(x-3 >= 0):
                        appearances += 1 if ''.join([board[y+i][x-i] for i in range(4)]) == "XMAS" else 0
                # Up
                if y-3 >= 0:
                    appearances += 1 if ''.join([board[y-i][x] for i in range(4)]) == "XMAS" else 0
                    # Up Right
                    if x+3 < len(board[y]):
                        appearances += 1 if ''.join([board[y-i][x+i] for i in range(4)]) == "XMAS" else 0
                    # Up Left
                    if(x-3 >= 0):
                        appearances += 1 if ''.join([board[y-i][x-i] for i in range(4)]) == "XMAS" else 0

    print("Part 1 Solution: " + str(appearances))


def part2():
    f = open('input/day4.txt', 'r')
    board = []
    for l in f:
        board.append(list(l.strip()))

    appearances = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if (board[y][x] == 'A' and 0 < y < len(board) - 1 and 0 < x < len(board[y]) - 1):
                diagonal1 = board[y+1][x+1] + board[y-1][x-1] 
                diagonal2 = board[y+1][x-1] + board[y-1][x+1]

                if diagonal1 in {"MS", "SM"} and diagonal2 in {"MS", "SM"}:
                    appearances += 1

    print("Part 2 Solution: " + str(appearances))


if __name__ == "__main__":
    part1()
    part2()