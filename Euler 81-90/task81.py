from typing import List


def parse_data(filename: str) -> List[List[int]]:
    with open(filename, "r") as f:
        lines = f.readlines()

        matrix = [[int(number) for number in line.split(",")] for line in lines]

    return matrix


def get_min_sum(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows - 2, -1, -1):
        matrix[row][cols - 1] += matrix[row + 1][cols - 1]

    for col in range(cols - 2, -1, -1):
        matrix[rows - 1][col] += matrix[rows - 1][col + 1]

    for row in range(rows - 2, -1, -1):
        for col in range(cols - 2, -1, -1):
            bottom = matrix[row + 1][col]
            right  = matrix[row][col + 1]

            matrix[row][col] += bottom if bottom < right else right
    
    return matrix[0][0]


# print(get_min_sum([
#     [131, 673, 234, 103, 18],
#     [201, 96, 342, 965, 150],
#     [630, 803, 746, 422, 111],
#     [537, 699, 497, 121, 956],
#     [805, 732, 524, 37, 331]
# ]))

data = parse_data("p081_matrix.txt")
result = get_min_sum(data)
print(result)