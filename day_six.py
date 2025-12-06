input_data: list[str] = []
with open('./day_six_input_data.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line)


def part_1():
    input_numbers: list[list[str]] = []
    for line in input_data[:-1]:
        input_numbers.append([value.strip() for value in line.split(' ') if value != ''])


    input_symbols: list[str] = []
    for s in input_data[-1].split(' '):
        s = s.strip()
        if s != '':
            input_symbols.append(s.strip())

    rows: int = len(input_numbers)
    cols: int = len(input_numbers[0])
    result: int = 0
    for c in range(cols):
        if input_symbols[c] == '+':
            total = 0
            for r in range(rows):
                total += int(input_numbers[r][c])
            result += total
        elif input_symbols[c] == '*':
            total = 1
            for r in range(rows):
                total *= int(input_numbers[r][c])
            result += total

    print(f'Result: {result}')


def part_2():
    ## use gap between each symbol on bottom row to help break up the data
    syms = input_data[-1]
    p1 = 0
    chunks: list[int] = []
    for p2 in range(1, len(syms)):
        if syms[p2] in ['+', '*']:
            chunks.append(p2 - p1)
            p1 = p2
    chunks.append(len(syms) - p1 + 1)

    ## get values using chunks
    values: list[list[str]] = []
    for line in input_data[:-1]:
        i: int = 0
        current: list[str] = []
        for c in chunks:
            current.append(line[i:i+c-1])
            i += c
        values.append(current)

    ## get result
    result: int = 0
    rows: int = len(values)
    cols: int = len(values[0])
    symbols: list[str] = [v for v in input_data[-1] if v in ['+', '*']]
    for c in range(cols):
        numbers: list[str] = []

        # build str number
        for r in range(rows):
            if not numbers:
                numbers = [''] * len(values[r][c])
            for i, v in enumerate(values[r][c]):
                numbers[i] += v

        # calculate
        if symbols[c] == '+':
            total = 0
            for n in numbers:
                total += int(n)
        else:
            total = 1
            for n in numbers:
                total *= int(n)

        result += total

    print(f'Result: {result}')


def main():
    print('Day 6')
    part_1()
    part_2()


if __name__ == '__main__':
    main()
