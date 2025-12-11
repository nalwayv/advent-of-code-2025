from collections import deque

input_data: list[str] = []
with open('./day_10_input.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line.strip())


def parse_lights(line: str) -> str:
    for value in line.split():
        if value.startswith('[') and value.endswith(']'):
            return value[1:-1]
    return ''


def parse_buttons(line: str) -> list[list[int]]:
    result: list[list[int]] = []
    for value in line.split():
        if value.startswith('(') and value.endswith(')'):
            buttons = value[1:-1].split(',')
            current = [int(val) for val in buttons]
            result.append(current)
    return result


def parse_jolts(line: str) -> list[int]:
    result: list[int] = []
    for value in line.split():
        if value.startswith('{') and value.endswith('}'):
            jolts = value[1:-1].split(',')
            result.extend(int(jolt) for jolt in jolts)
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
    total_count: int = 0
    for line in input_data:
        lights: str = parse_lights(line)
        buttons: list[list[int]] = parse_buttons(line)
        count: int = min_steps_to_target(lights, buttons)
        
        if count != -1:
            total_count += count

    print(f'Part 1 Result: {total_count}')


def main() -> None:
    print('Day 10: Factory')
    part_1()


if __name__ == '__main__':
    main()