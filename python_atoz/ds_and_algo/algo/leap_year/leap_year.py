def is_leap_year(y):
    # case-1: century year -> must divisible by 400
    if y % 100 == 0 and y % 400 == 0:
        return f"{y} - leap"
    # case-2: non century year -> must divisible by 4
    elif y % 100 != 0 and y % 4 == 0:
        return f"{y} - leap"
    else:
        return f"{y} - x"


if __name__ == '__main__':
    for x in range(1989, 2025):
        print(is_leap_year(x))

