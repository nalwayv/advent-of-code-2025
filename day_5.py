input_ranges: list[str] = []
with open('./day_5_input_ranges.txt', 'r') as file:
    while line := file.readline():
        input_ranges.append(line.strip())


input_ids: list[str] = []
with open('./day_5_input_ids.txt', 'r') as file:
    while line := file.readline():
        input_ids.append(line.strip())


def part_1(ranges: list[tuple[int, int]], ids: list[int]):
    result: int = 0
    for i in ids:
        is_fresh = False

        for lo, hi in ranges:
            if lo <= i < hi + 1:
                is_fresh = True
                break

        if is_fresh:
            result += 1

    print(f'Part 1 Result: {result}')


def part_2(ranges: list[tuple[int, int]]):
    sorted_ranges = sorted(ranges)
    count: int = 0
    current_start, current_end = sorted_ranges[0]

    for i in range(1, len(sorted_ranges)):
        next_start = sorted_ranges[i][0]
        next_end = sorted_ranges[i][1]
        
        # if end overlaps next start then merge ranges
        if current_end + 1 >= next_start:
            current_end = max(current_end, next_end)
        else:
            count += current_end - current_start + 1
            current_start, current_end = next_start, next_end

    count += current_end - current_start + 1

    print(f'Part 2 Result: {count}')


def main():
    ranges: list[tuple[int, int]] = []
    for x in input_ranges:
        a, b = x.split('-')
        ranges.append((int(a), int(b)))

    ids: list[int] = [int(i) for i in input_ids]

    print('Day 5')
    part_1(ranges, ids)
    part_2(ranges)


if __name__ == '__main__':
    main()