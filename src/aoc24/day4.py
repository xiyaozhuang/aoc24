def search_perimeter(character: str, coordinates: tuple, grid: list) -> dict:
    x, y = coordinates
    positions = []
    directions = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[i]):
                if character in grid[x + i][y + j]:
                    positions.append((x + i, y + j))
                    directions.append((i, j))

    return {"positions": positions, "directions": directions}


def search_direction(character: str, perimeter: dict, grid: list) -> dict:
    positions = []
    directions = []

    for i in range(len(perimeter["positions"])):
        x = perimeter["positions"][i][0] + perimeter["directions"][i][0]
        y = perimeter["positions"][i][1] + perimeter["directions"][i][1]

        if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
            if character in grid[x][y]:
                positions.append((x, y))
                directions.append(perimeter["directions"][i])

    return {"positions": positions, "directions": directions}


def search_top_left(coordinates: tuple, grid: list) -> bool:
    x, y = coordinates

    conditions = (
        "M" in grid[x - 1][y - 1] and "S" in grid[x + 1][y + 1],
        "M" in grid[x + 1][y + 1] and "S" in grid[x - 1][y - 1],
    )

    if any(conditions):
        return True

    return False


def search_top_right(coordinates: tuple, grid: list) -> bool:
    x, y = coordinates

    conditions = (
        "M" in grid[x - 1][y + 1] and "S" in grid[x + 1][y - 1],
        "M" in grid[x + 1][y - 1] and "S" in grid[x - 1][y + 1],
    )

    if any(conditions):
        return True

    return False


def part1(data_path: str) -> int:
    with open(data_path) as file:
        word_search = [line.strip() for line in file.readlines()]

    total = 0

    for i in range(len(word_search)):
        for j in range(len(word_search[i])):
            if "X" in word_search[i][j]:
                x_perimeter = search_perimeter("M", (i, j), word_search)
                m_perimeter = search_direction("A", x_perimeter, word_search)
                a_perimeter = search_direction("S", m_perimeter, word_search)

                total += len(a_perimeter["positions"])

    return total


def part2(data_path: str) -> int:
    with open(data_path) as file:
        word_search = [line.strip() for line in file.readlines()]

    total = 0

    for i in range(1, len(word_search) - 1):
        for j in range(1, len(word_search[i]) - 1):
            conditions = (
                "A" in word_search[i][j],
                search_top_left((i, j), word_search),
                search_top_right((i, j), word_search),
            )

            if all(conditions):
                total += 1

    return total
