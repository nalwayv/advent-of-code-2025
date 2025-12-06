input_ranges: list[str] = []
with open('./day_five_input_ranges.txt', 'r') as file:
    while line := file.readline():
        input_ranges.append(line.strip())


input_ids: list[str] = []
with open('./day_five_input_ids.txt', 'r') as file:
    while line := file.readline():
        input_ids.append(line.strip())


def part1():
    result: int = 0
    for i in input_ids:
        is_fresh = False

        for j in input_ranges:
            lo, hi = j.split('-')

            # if value is within any of the ranges its considerd fresh
            if int(lo) <= int(i) < int(hi) + 1:
                is_fresh = True
                break

        if is_fresh:
            result += 1

    print(f'Part 1 Result: {result}')


def part2():
    # convert
    arr: list[tuple[int, int]] = []
    for x in input_ranges:
        a, b = x.split('-')
        arr.append((int(a), int(b)))

    # ranges need to be sorted
    sorted_ranges = sorted(arr)
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
    part1()
    part2()


if __name__ == '__main__':
    main()