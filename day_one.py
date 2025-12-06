input_data: list[str] = []
with open('./day_one_input_data.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line.strip())


def main():
    dial: int = 50
    frequency: dict[int, int] = {}
    click: int = 0
    max_frequency: int = 0


    for rot in input_data:
        dir: str = rot[0]
        number = int(rot[1:])
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