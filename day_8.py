input_data: list[str] = []
with open('./day_8_input.txt', 'r') as file:
    while line := file.readline():
        input_data.append(line)


class Edge:
    def __init__(self, i: int, j: int, dist: int) -> None:
        self.i: int = i
        self.j: int = j
        self.dist: int = dist


class DisjointSet:
    def __init__(self):
        self.parent: dict[int, int] = {}
        self.size: dict[int, int] = {} 

    def make_set(self, x: int) -> None:
        self.parent[x] = x
        self.size[x] = 1 

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
    

def sub(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def magnitude_sq(a: tuple[int, int, int]) -> int:
    return (a[0] * a[0]) + (a[1] * a[1]) + (a[2] * a[2])


def distance_to_sq(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return magnitude_sq(sub(b, a))


def get_coords_from_data(data: list[str]) -> list[tuple[int, int, int]]:
    coords: list[tuple[int, int, int]] = []
    for line in data:
        values = line.split(',')
        if len(values) != 3:
            continue
        coords.append((int(values[0]), int(values[1]), int(values[2])))
    return coords


def part_1() -> None:
    coords = get_coords_from_data(input_data)
    edges: list[tuple[int, int, int]] = []
    coords_length: int = len(coords)
    for i in range(coords_length - 1):
        for j in range(i + 1, coords_length):
            c1 = coords[i]
            c2 = coords[j]
            edge = (i, j, distance_to_sq(c1, c2))
            edges.append(edge)
    edges.sort(key=lambda x: x[2])

    dsu = DisjointSet()
    for i in range(coords_length):
        dsu.make_set(i)

    edges_length: int = len(edges)
    for i in range(min(1000, edges_length)):
        dsu.union(edges[i][0], edges[i][1])

    circuits: list[int] = []
    for i in range(coords_length):
        if dsu.parent.get(i, -1) == i:
            circuits.append(dsu.size[i])

    circuits.sort()
    result = 0 if len(circuits) < 3 else circuits[-1] * circuits[-2] * circuits[-3]
    
    print(f'Part 1 Result: {result}')


def main() -> None:
    print('Day 8: Playground')
    part_1()


if __name__ == "__main__":
    main()