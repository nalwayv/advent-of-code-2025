input_data: list[str] = []
with open('./day_3_input.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line.strip())


def biggest_number(num: str, k: int):
    amount: int = len(num) - k
    stk: list[str] = []
    for digit in num:
        while k > 0 and stk and stk[-1] < digit:
            stk.pop()
            k -= 1
        stk.append(digit)
    return ''.join(stk[:amount])


def part_1(data: list[str]):
    result: int = 0
    for nums in data:
        arr = [int(i) for i in nums]
        max_num: int = 0
        
        p1: int = 0
        for p2 in range(1, len(arr)):
            if arr[p2] > arr[p1]:
                max_num = max(max_num, (arr[p1] * 10) + arr[p2])
                p1 = p2
            else:
                max_num = max(max_num, (arr[p1] * 10) + arr[p2])
        result += max_num
    print(f'Part 1 Result: {result}')


def part_2(data: list[str]):
    total: int = 0
    for num in data:
        total += int(biggest_number(num, 88))
    print(f'Part 2 Result: {total}')


def main():
    print('Day 3: Lobby')
    part_1(input_data)
    part_2(input_data)


if __name__ == '__main__':
    main()