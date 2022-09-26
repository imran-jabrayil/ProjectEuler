from time import time


def calculate(triang):
    if len(triang) == 1:
        return triang[0][0]
    
    last_line = triang.pop(-1)

    for i in range(len(last_line) - 1):
        if last_line[i] > last_line[i + 1]:
            triang[-1][i] += last_line[i]
        else:
            triang[-1][i] += last_line[i + 1]
    
    return calculate(triang)


start = time()

f = open("triangle.txt", "r")
nums = [list(map(int, i.split())) for i in f.readlines()]
f.close()
print(calculate(nums))

print("Time {} s.".format(time() - start))