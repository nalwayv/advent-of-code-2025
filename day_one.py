input_data: list[str] = []
with open('./day_one_input_data.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line.strip())


def convert_input_data(data: list[str]) -> list[tuple[str, int]]:
    return [(line[0], int(line[1:])) for line in data]


def main():
    dial: int = 50
    frequency: dict[int, int] = {}
    click: int = 0
    max_frequency: int = 0

    values = convert_input_data(input_data)

    for dir, number in values:
        if dir == 'R':
            for _ in range(number):
                if dial == 0:
                    click += 1

                dial += 1
                if dial > 99:
                    dial = 0
        elif dir == 'L':
            for _ in range(number):
                if dial == 0:
                    click += 1

                dial -= 1
                if dial < 0:
                    dial = 99
                    
        frequency[dial] = frequency.get(dial, 0) + 1
        if frequency[dial] > max_frequency:
            max_frequency = frequency[dial]

    print('Day 1')
    print(f'Part 1 Result: {max_frequency}')
    print(f'Part 2 Result: {click}')


if __name__ == '__main__':
    main()