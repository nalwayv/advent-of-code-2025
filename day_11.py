input_data: list[str] = []
with open('./day_11_input.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line)


def generate_graph_from_data(data: list[str]) -> dict[str, list[str]] :
    graph: dict[str, list[str]] = {}
    for line in data:
        split_values: list[str] = line.split(':')
        if len(split_values) != 2:
            continue

        key: str = split_values[0].strip()
        values: list[str] = list(split_values[1].strip().split())
        graph[key] = values
        
    return graph


def memo_count1(graph: dict[str, list[str]], memo: dict[str, int], memo_data: str) -> int:
    if memo_data == 'out':
        return 1
    
    if memo_data in memo:
        return memo[memo_data]
    
    count = 0
    for val in graph[memo_data]:
        count += memo_count1(graph, memo, val)

    memo[memo_data] = count
    return count


def memo_count2(graph: dict[str, list[str]], memo: dict[tuple[str, bool, bool], int], memo_data: tuple[str, bool, bool]) -> int:
    node, dac, ftt = memo_data
    
    if node == 'out':
        return 1 if dac and ftt else 0
    
    if memo_data in memo:
        return memo[memo_data]
    
    count: int = 0
    for val in graph[node]:
        has_dac = dac or val == 'dac'
        has_ftt = ftt or val == 'fft'
        count += memo_count2(graph, memo, (val, has_dac, has_ftt))
    
    memo[memo_data] = count
    return count


def part_1() -> None:
    graph: dict[str, list[str]] = generate_graph_from_data(input_data)
    count: int = memo_count1(graph, {}, 'you')
    print(f'Result Part 1: {count}')


def part_2() -> None:
    graph: dict[str, list[str]] = generate_graph_from_data(input_data)
    count: int = memo_count2(graph, {}, ('svr', False, False))
    print(f'Result Part 2: {count}')


def main() -> None:
    print('Day 11: Reactor')
    part_1()
    part_2()


if __name__ == '__main__':
    main()