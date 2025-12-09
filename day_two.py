input_data: list[str] = []
with open('./day_two_input_data.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line.strip())


def convert_data(data: list[str]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    for line in data:
        values = line.split('-')
        if len(values) != 2:
            continue
        result.append((int(values[0]), int(values[1])))
    return result


def p1_is_invalid(s: str):
    """
    Checks if the given string can be split into two equal halves that are identical.
    """
    if len(s) % 2 == 0:
        half = len(s) // 2
        if s[half:] == s[:half]:
            return True
    return False


def p2_is_invalid(s: str):
    """
    Determines if a string is composed of a repeating pattern.
    """
    for length in range(1, len(s) // 2 + 1):
        pattern = s[:length]
        if pattern * (len(s) // length) == s:
            return True
    return False


def part_1(data: list[tuple[int, int]]):
    total: int = 0
    for lo, hi in data:
        for i in range(lo, hi + 1):
            if p1_is_invalid(str(i)):
                total += i
    print(f'Part 1 Result: {total}')


def part_2(data: list[tuple[int, int]]):
    total: int = 0
    for lo, hi in data:
        for i in range(lo, hi + 1):
            if p1_is_invalid(str(i)) or p2_is_invalid(str(i)):
                total += i

    print(f'Part 2 Result: {total}')


def main() -> None:
    print('Day 2')

    data = convert_data(input_data)

    part_1(data)
    part_2(data)


if __name__ == '__main__':
    main()