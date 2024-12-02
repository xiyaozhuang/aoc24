"--- Day 1: Historian Hysteria ---"


def part1(data_path: str) -> int:
    with open(data_path) as file:
        lines = [line.strip().split("   ") for line in file.readlines()]

    ids1 = sorted((int(ids[0]) for ids in lines))
    ids2 = sorted((int(ids[1]) for ids in lines))
    distances = (abs(ids1[i] - ids2[i]) for i in range(len(ids1)))

    total = sum(distances)

    return total


def part2(data_path: str) -> int:
    with open(data_path) as file:
        lines = [line.strip().split("   ") for line in file.readlines()]

    ids1 = sorted((int(ids[0]) for ids in lines))
    ids2 = sorted((int(ids[1]) for ids in lines))

    similarity_score = 0

    for i in range(len(ids1)):
        occurrences = 0

        for j in range(len(ids2)):
            if ids1[i] == ids2[j]:
                occurrences += 1

        similarity_score += ids1[i] * occurrences

    return similarity_score
