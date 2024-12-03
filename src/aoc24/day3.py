import re


def part1(data_path: str) -> int:
    with open(data_path) as file:
        program = file.read().strip()

    instructions = re.findall(r"mul\(\d+,\d+\)", program)
    total = 0

    for instruction in instructions:
        numbers = re.findall(r"\d+", instruction)
        total += int(numbers[0]) * int(numbers[1])

    return total


def part2(data_path: str) -> int:
    with open(data_path) as file:
        program = file.read().strip()

    enabled = True
    instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", program)
    total = 0

    for instruction in instructions:

        if "do(" in instruction:
            enabled = True
        elif "don" in instruction:
            enabled = False

        if enabled and "mul(" in instruction:
            numbers = re.findall(r"\d+", instruction)
            total += int(numbers[0]) * int(numbers[1])

    return total
