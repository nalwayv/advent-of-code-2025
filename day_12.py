input_data: list[str] = []
with open('./day_12_input_data.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line.strip())


def parse_shapes(lines: list[str]) -> list[list[str]]:
    arr: list[str] = []
    for line in lines:
        if line.startswith('#') or line.startswith('.'):
            arr.append(line)

    result: list[list[str]] = []

    for i in range(0, len(arr), 3):
        result.append([arr[i], arr[i + 1], arr[i + 2]])

    return result


def parse_regions(lines: list[str]) -> list[list[int]]:
    result: list[list[int]] = []
    for line in lines:
        if not line or not (line[0].isdigit() and line[-1].isdigit()):
            continue

        reg_values = line.split(':')
        if len(reg_values) != 2:
            continue

        size_values = reg_values[0].split('x')
        if len(size_values) != 2:
            continue

        current = [size_values[0], size_values[1]] + reg_values[1].split()
        result.append([int(val) for val in current])

    return result


def part_1() -> None:
    regions: list[list[int]] = parse_regions(input_data)

    count: int = 0
    for values in regions:
        rows: int = values[0]
        cols: int = values[1]
        sum_total: int = sum(values[2:])

        # total * shape_size - 1 < area
        if sum_total * 8 < rows * cols:
            count += 1
        
    print(f'Result Part 1: {count}')


def main() -> None:
    print('Day 12: Christmas Tree Farm')
    part_1()


if __name__ == '__main__':
    main()

