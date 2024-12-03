from os import listdir

import aoc24
from aoc24 import *


def get_modules(module: object, pattern: str, test: bool = False) -> list:
    """Returns all the modules that have the start of their name matching the pattern.
    If test is True, it only returns the `aoc24.day1` module."""

    if test:
        return [aoc24.day1]

    modules = []

    for name in dir(module):
        if name.startswith(pattern):
            modules.append(getattr(module, name))

    return modules


def get_solutions(directory: str, test: bool = False) -> dict:
    """Returns the solution of the given data using the aoc24 package.
    If test is True, it only returns the test solutions for the first day."""

    if test:
        data_paths = [directory + "day1a.txt"]

    else:
        data_paths = [directory + file for file in listdir(directory)]

    modules = get_modules(aoc24, "day", test)
    solutions = {}

    for i in range(len(modules)):
        parts = get_modules(modules[i], "part", test=False)

        solutions[data_paths[i]] = (
            parts[0](data_paths[i]),
            parts[1](data_paths[i]),
        )

    return solutions
