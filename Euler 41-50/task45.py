def triangle(index):
    return int(index * (index + 1) / 2)

def pentagonal(index):
    return int(index * (3 * index - 1) / 2)

def hexagonal(index):
    return int(index * (2 * index - 1))

T = [0]
P = [-1]
H = [-2]

result = [0]
index = 1

while result[-1] <= 40755:
    T.append(triangle(index))
    P.append(pentagonal(index))
    H.append(hexagonal(index))
    if T[index] in P and T[index] in H:
        result.append(T[index])
    index += 1


print(result[-1])