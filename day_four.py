input_data: list[list[str]] = []
with open('./day_four_input_data.txt', 'r') as file:
    while line := file.readline():
        input_data.append([x for x in line.strip()])


def part1(tiles: list[list[str]]):
    rows: int = len(tiles)
    cols: int = len(tiles[0])

    up = [0,1]
    down = [0,-1]
    left = [-1,0]
    right = [1,0]
    up_right = [1,1]
    down_right = [1, -1]
    up_left = [-1, 1]
    down_left = [-1, -1]
    directions: list[list[int]] = [up, down, left, right, up_right, up_left, down_right, down_left]

    count: int = 0
    for row in range(rows):
        for col in range(cols):
            if tiles[row][col] != '@':
                continue
            
            movable: int = 0
            for direction in directions:
                dir_x: int = row + direction[0]
                dir_y: int = col + direction[1]
                in_range: bool = 0 <= dir_x < rows and 0 <= dir_y < cols

                if in_range and tiles[dir_x][dir_y] == '@':
                    movable += 1

            if movable < 4:
                count += 1

    print(f'Result: {count}')


def part2(tiles: list[list[str]]):
    rows: int = len(tiles)
    cols: int = len(tiles[0])

    up = [0,1]
    down = [0,-1]
    left = [-1,0]
    right = [1,0]
    up_right = [1,1]
    down_right = [1, -1]
    up_left = [-1, 1]
    down_left = [-1, -1]
    directions: list[list[int]] = [up, down, left, right, up_right, up_left, down_right, down_left]
    count: int = 0

    while True:
        coords: list[list[int]] = []
        for row in range(rows):
            for col in range(cols):
                if tiles[row][col] != '@':
                    continue

                movable: int = 0
                for direction in directions:
                    dir_x: int = row + direction[0]
                    dir_y: int = col + direction[1]
                    in_range: bool = 0 <= dir_x < rows and 0 <= dir_y < cols

                    if in_range and tiles[dir_x][dir_y] == '@':
                        movable += 1

                if movable < 4:
                    coords.append([row, col])

        if not coords:
            print(f'Result: {count}')
            break
        
        # update and remove
        count += len(coords)
        for coord in coords:
            tiles[coord[0]][coord[1]] = '.'


def main() -> None:
    print('Day 4')

    part1(input_data)
    part2(input_data)


if __name__ == '__main__':
    main()