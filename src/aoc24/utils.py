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
        data_paths = (directory + "day1a.txt",)
    else:
        data_paths = (directory + file for file in listdir(directory))

    solutions = {}

    for module in get_modules(aoc24, "day", test):
        parts = get_modules(module, "part", test=False)

        for data_path in data_paths:
            solutions[data_path] = (
                parts[0](data_path),
                parts[1](data_path),
            )

    return solutions
