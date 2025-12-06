input_data: list[str] = []
with open('./day_six_input_data.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line)


def part_1(input_numbers: list[list[str]], input_symbols: list[str]):
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

    print(f'Part 1 Result: {result}')


def part_2(input_numbers: list[list[str]], input_symbols: list[str]):
    ## get result
    rows: int = len(input_numbers)
    cols: int = len(input_numbers[0])

    result: int = 0
    for c in range(cols):
        # build str number
        numbers: dict[int, str] = {}
        for r in range(rows):
            for i, v in enumerate(input_numbers[r][c]):
                if i not in numbers:
                    numbers[i] = ''
                numbers[i] += v

        # calculate
        total: int = 0
        if input_symbols[c] == '+':
            for n in numbers.values():
                total += int(n)
        elif input_symbols[c] == '*':
            total = 1
            for n in numbers.values():
                total *= int(n)
        result += total

    print(f'Part 2 Result: {result}')


def main():
    ## Format Data
    last_line: str = input_data[-1]

    p1: int = 0
    chunks: list[int] = []
    for p2 in range(1, len(last_line)):
        if last_line[p2] in ['+', '*']:
            chunks.append(p2 - p1)
            p1 = p2
    chunks.append(len(last_line) - p1 + 1)

    input_numbers: list[list[str]] = []
    for line in input_data[:-1]:
        i: int = 0
        current: list[str] = []
        for c in chunks:
            current.append(line[i:i + c - 1])
            i += c
        input_numbers.append(current)

    input_symbols: list[str] = [v for v in last_line if v in ['+', '*']]

    print('Day 6')
    part_1(input_numbers, input_symbols)
    part_2(input_numbers, input_symbols)


if __name__ == '__main__':
    main()
