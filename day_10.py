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


def part_1() -> None:
    total_count: int = 0

    for line in input_data:
        lights: str = parse_lights(line)
        buttons: list[list[int]] = parse_buttons(line)

        len_lights: int = len(lights)
        target: int = 0
        for i in range(len_lights):
            if lights[i] == '#':
                target ^= 1 << (len(lights) - 1 - i)

        queue: deque[tuple[int, int]] = deque()
        queue.append((0, 0))
        seen: set[int] = set([0])

        while queue:
            light, count = queue.popleft()

            if light == target:
                total_count += count
                continue
            
            for button in buttons:
                new_light = light

                # flip bits
                for i in button:
                    new_light ^= 1 << (len_lights - 1 - i)
                    
                if new_light not in seen:
                    seen.add(new_light)
                    queue.append((new_light, count + 1))
        
    print(f'Part 1 Result: {total_count}')


def main() -> None:
    print('Day 10: Factory')
    part_1()


if __name__ == '__main__':
    main()