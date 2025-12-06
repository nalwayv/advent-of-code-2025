input_data: list[str] = []
with open('./day_six_input_data.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line)


def part_1():
    symbols: list[str] = [v for v in input_data[-1] if v in ['+', '*']]
    values: list[list[str]] = []
    for line in input_data[:-1]:
        values.append([v for v in line.split(' ') if v != ''])

    rows: int = len(values)
    cols: int = len(values[0])

    total_sum = 0
    for c in range(cols):
        if symbols[c] == '+':
            current_sum = 0
            for r in range(rows):
                current_sum += int(values[r][c])
            total_sum += current_sum

        else:
            current_sum = 1
            for r in range(len(values)):
                current_sum *= int(values[r][c])
            total_sum += current_sum

    print(f'Part 1 Result: {total_sum}')


def part_2():
    values: list[list[str]] = []
    for line in input_data:
        values.append([x for x in line])

    rows: int = len(values)
    cols: int = len(values[0])

    total_sum: int = 0
    current_sum: int = 0
    current_sym: str = '+'

    for c in range(cols):
        str_build = ''
        for r in range(rows):
            str_build += values[r][c]
        
        if str_build.isspace():
            continue

        if '*' in str_build:
            total_sum += current_sum
            current_sum = 1
            current_sym = '*'
            str_build = ''.join(x for x in str_build if x != '*')

        if '+' in str_build:
            total_sum += current_sum
            current_sum = 0
            current_sym = '+'
            str_build = ''.join(x for x in str_build if x != '+')

        if current_sym == '*':
            current_sum *= int(str_build)
        
        if current_sym == '+':
            current_sum += int(str_build)
    
    total_sum += current_sum

    print(f'Part 2 Result: {total_sum}')


def main():
    print('Day 6')
    part_1()
    part_2()


if __name__ == '__main__':
    main()
