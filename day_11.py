input_data: list[str] = []
with open('./day_11_input.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line)


def generate_graph_from_data(data: list[str]) -> dict[str, list[str]] :
    graph: dict[str, list[str]] = {}

    for line in data:
        # general assumptions that each key in input data is unique
        key: str = ''
        values: list[str] = []
        
        # parse
        for value in line.split():
            if value.endswith(':'):
                key = value[:-1]
            else:
                values.append(value)
        graph[key] = values

    return graph


def count_paths(graph: dict[str, list[str]], start: str, goal: str) -> int:
    def dfs(node: str, count: list[int]):
        if node == goal:
            count[0] += 1
        elif node in graph:
            for n in graph[node]:
                dfs(n, count)

    ref: list[int] = [0]
    dfs(start, ref)
    return ref[0]


def part_1() -> None:
    graph: dict[str, list[str]] = generate_graph_from_data(input_data)
    count: int = count_paths(graph, 'you', 'out')
    print(f'Result Part 1: {count}')


def main() -> None:
    print('Day 11: Reactor')
    part_1()


if __name__ == '__main__':
    main()