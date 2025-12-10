input_data: list[str] = []
with open('./day_9_input.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line.strip())


def convert_input_data(data: list[str]) -> list[tuple[int, int]]:
    coords: list[tuple[int, int]] = []
    for line in data:
        values = line.split(',')
        if len(values) != 2:
            continue

        v1 = int(values[0])
        v2 = int(values[1])
        coords.append((v1, v2))
    return coords


def part_1(data: list[tuple[int, int]]) -> None:
    data_ln: int = len(data)
    max_area: int = 0
    for i in range(data_ln - 1):
        for j in range(i + 1, data_ln):
            coords_a: tuple[int, int] = data[i]
            coords_b: tuple[int, int] = data[j]

            width: int = abs(coords_a[0] - coords_b[0]) + 1
            height: int = abs(coords_a[1] - coords_b[1]) + 1

            max_area = max(max_area, width * height)
    
    print(f'Part 1 Result: {max_area}')


def main():
    print('Day 9')
    data = convert_input_data(input_data)
    part_1(data)


if __name__ == '__main__':
    main()