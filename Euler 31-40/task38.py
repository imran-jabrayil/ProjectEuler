def combine(num):
    result = ''
    for i in range(1, 987654321):
        result += str(num * i)
        if len(result) > 9:
            return False
        if len(set(result)) == 9 and '0' not in result:
            return int(result)

answer = 0

for i in range(1, 100000):
    print(i)
    temp = combine(i)
    if temp > answer:
        answer = temp


print(answer)