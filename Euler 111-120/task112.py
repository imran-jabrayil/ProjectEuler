def is_bouncy(number: int) -> bool:
    number_str = str(number)
    up = down = False

    for i in range(len(number_str) - 1):
        if number_str[i] > number_str[i + 1]:
            down = True
        elif number_str[i] < number_str[i + 1]:
            up = True

    return down and up


current_number = 1

bouncies = 0

while bouncies * 100 != current_number * 99:
    current_number += 1
    if is_bouncy(current_number):
        bouncies += 1

print(current_number)
