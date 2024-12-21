"--- Day 5: Print Queue ---"


def sort(updates: list, rules: list) -> dict:
    sorted_updates = {"correct": [], "incorrect": []}

    for update in updates:
        rule_broken = False

        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    rule_broken = True
                    break

        if not rule_broken:
            sorted_updates["correct"].append(update)
        else:
            sorted_updates["incorrect"].append(update)

    return sorted_updates


def reorder(update: list, rules: list) -> list:
    rule_broken = False

    for rule in rules:
        if rule[0] in update and rule[1] in update:
            left_index = update.index(rule[0])
            right_index = update.index(rule[1])

            if left_index > right_index:
                update[left_index] = rule[1]
                update[right_index] = rule[0]
                rule_broken = True

    if rule_broken:
        update = reorder(update, rules)

    return update


def part1(data_path: str) -> int:
    with open(data_path) as file:
        manual = file.read().strip().split("\n\n")

    rules = [string.split("|") for string in manual[0].split("\n")]
    updates = [string.split(",") for string in manual[1].split("\n")]
    sorted_updates = sort(updates, rules)
    total = 0

    for correct_update in sorted_updates["correct"]:
        total += int(correct_update[(len(correct_update) - 1) // 2])

    return total


def part2(data_path: str) -> int:
    with open(data_path) as file:
        manual = file.read().strip().split("\n\n")

    rules = [string.split("|") for string in manual[0].split("\n")]
    updates = [string.split(",") for string in manual[1].split("\n")]
    sorted_updates = sort(updates, rules)
    total = 0

    for incorrect_update in sorted_updates["incorrect"]:
        correct_update = reorder(incorrect_update, rules)
        total += int(correct_update[(len(correct_update) - 1) // 2])

    return total
