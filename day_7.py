input_data: list[str] = []
with open('day_7_input.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line.strip())


def part_1():
    data: list[list[str]] = [[v for v in line] for line in input_data]
    beams: dict[int, bool] = {i: True for i, s in enumerate(data[0]) if s == 'S'}
    rows: int = len(data)
    cols: int = len(data[0])
    count: int = 0

    for r in range(rows):
        for c in range(cols):
            if data[r][c] != '^':
                continue

            if c in beams and beams[c]:
                beams[c] = False
                count += 1

                for offset in [-1, 1]:
                    if 0 <= c + offset < cols:
                        beams[c + offset] = True

    print(f'Part 1 Result: {count}')


def part_2():
    data: list[list[str]] = [[v for v in line] for line in input_data]
    rows: int = len(data)
    cols: int = len(data[0])

    current_vals: list[int] = [0] * cols
    next_values: list[int] = [0] * cols

    for i, val in enumerate(data[0]):
        if val == 'S':
            current_vals[i] = 1

    for r in range(rows):
        for c in range(cols):

            if current_vals[c] == 0:
                continue
            
            if data[r][c] == '^':
                for offset in [-1, 1]:
                    if 0 <= c + offset < cols:
                        next_values[c + offset] += current_vals[c]
            else:
                next_values[c] += current_vals[c]

        for i in range(cols):
            current_vals[i] = next_values[i]
            next_values[i] = 0

    count: int = sum(current_vals)
    print(f'Part 2 Result: {count}')


def main():
    print('Day 7: Laboratories')
    part_1()
    part_2()


if __name__ == '__main__':
    main()