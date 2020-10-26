def calculate():
    count = 0
    power = 1
    for num in range(1, 10):
        while True:
            if len(str(num ** power)) < power:
                break
            power += 1
            count += 1
        power = 1
    return count


print(calculate())
