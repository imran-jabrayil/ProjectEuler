from typing import List


def get_sudokus(filename: str) -> List[List[int]]:
    sudokus = []

    with open(filename, "r") as f:
        for i in range(50):
            f.readline()
            sudoku = [
                [int(char) for char in f.readline().strip()] for i in range(9)
            ]
            sudokus.append(sudoku)

    return sudokus


def sudoku_solver(puzzle: List[List[int]]) -> List[List[int]]:
    pair = find_zero(puzzle)

    if pair == (-1, -1):
        return puzzle

    for num in range(1, 10):
        if is_valid(puzzle, pair, num):
            puzzle[pair[0]][pair[1]] = num
            sudoku_solver(puzzle)
            if find_zero(puzzle) == (-1, -1):
                break
        puzzle[pair[0]][pair[1]] = 0
    
    if puzzle[0][0] == 0:
        raise BaseException

    return puzzle


def find_zero(puzzle: List[List[int]]) -> (int, int):
    for i in range(len(puzzle)):
        if 0 in puzzle[i]:
            return i, puzzle[i].index(0)

    return -1, -1


def is_valid(puzzle: List[List[int]], pair: (int, int), number: int) -> bool:
    return number not in puzzle[pair[0]] and number not in [puzzle[i][pair[1]] for i in range(len(puzzle))] and\
        number not in [puzzle[pair[0] - pair[0] % 3 + i][pair[1] - pair[1] % 3 + j] for i in range(3) for j in range(3)]


if __name__ == "__main__":
    sudokus = get_sudokus("p096_sudoku.txt")

    result = 0
    for sudoku in sudokus:
        solved = sudoku_solver(sudoku)
        result += solved[0][0] * 100 + solved[0][1] * 10 + solved[0][2]

    print(result)
    
