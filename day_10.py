from collections import deque

input_data: list[str] = []
with open('./day_10_input.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line.strip())


def parse_lights(line: str):
    for values in line.split(' '):
        if values[0] != '[':
            continue
        return values[1:-1]
    return ''


def parse_buttons(line: str):
    result: list[list[int]] = []
    for values in line.split(' '):
        if values[0] != '(':
            continue

        current: list[int] = []
        for val in values[1:-1].split(','):
            current.append(int(val))
        result.append(current)

    return result


def parse_jolts(line: str):
    result: list[int] = []
    for values in line.split(' '):
        if values[0] != '{':
            continue

        for val in values[1:-1].split(','):
            result.append(int(val))
        return result
    
    return result


def min_steps_to_target(target: str, buttons: list[list[int]]) -> int:
    start: str = '.' * len(target)
    queue: deque[tuple[str, int]] = deque()
    queue.append((start, 0))

    seen: set[str] = set()
    seen.add(start)

    while queue:
        light, count = queue.popleft()

        if light == target:
            return count

        for button in buttons:
            new_light = list(light)

            for val in button:
                if new_light[val] == '#':
                    new_light[val] = '.'
                else:
                    new_light[val] = '#'

            new_light_str = ''.join(new_light)
            if new_light_str not in seen:
                seen.add(new_light_str)
                queue.append((new_light_str, count + 1))
                
    return -1


def part_1() -> None:
    # example_lines = [
    #     '[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}',
    #     '[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}',
    #     '[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}']

    total_count: int = 0
    for line in input_data:
        lights: str = parse_lights(line)
        buttons: list[list[int]] = parse_buttons(line)
        current_count: int = min_steps_to_target(lights, buttons)
        if current_count != -1:
            total_count += current_count

    print(f'Part 1 Result: {total_count}')


def main():
    print('Day 10')
    part_1()


if __name__ == '__main__':
    main()