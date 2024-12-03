"--- Day 2: Red-Nosed Reports ---"


def get_distances(report: list) -> list:
    distances = []

    for i in range(len(report) - 1):
        distance = int(report[i + 1]) - int(report[i])
        distances.append(distance)

    return distances


def get_condition(report_distances: list) -> bool:
    increasing = any(distance > 0 for distance in report_distances)
    decreasing = any(distance < 0 for distance in report_distances)
    stationary = any(distance == 0 for distance in report_distances)
    spike = any(abs(distance) > 3 for distance in report_distances)

    return not (increasing and decreasing or stationary or spike)


def part1(data_path: str) -> int:
    with open(data_path) as file:
        reports = [line.strip().split(" ") for line in file.readlines()]

    all_report_distances = [get_distances(report) for report in reports]
    safe_reports = 0

    for report_distances in all_report_distances:
        if get_condition(report_distances):
            safe_reports += 1

    return safe_reports


def part2(data_path: str) -> int:
    with open(data_path) as file:
        reports = [line.strip().split(" ") for line in file.readlines()]

    all_report_distances = [get_distances(report) for report in reports]
    safe_reports = 0

    for i in range(len(all_report_distances)):
        if get_condition(all_report_distances[i]):
            safe_reports += 1
            continue

        for j in range(len(all_report_distances[i]) + 1):
            component1 = reports[i][:j]
            component2 = reports[i][j + 1 :]

            new_report = component1 + component2
            new_report_distances = get_distances(new_report)

            if get_condition(new_report_distances):
                safe_reports += 1
                break

    return safe_reports
