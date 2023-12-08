from dataclasses import dataclass
from aocd import data, submit
import re

# find x1, x2 and y of each number
# find x and y of every symbol
# for each number
# for each symbol
# if symbol.x in number.range(x1, x2) and number.y == symbol.y

data = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''


@dataclass
class Number:
    value: int
    x1: int
    x2: int
    y: int


@dataclass
class Symbol:
    value: str
    x: int
    y: int


numbers = []
symbols = []

for y, row in enumerate(data.splitlines()):
    for match in re.finditer("\d+", row):
        numbers.append(Number(int(match.group(0)),
                       match.start(), match.end(), y))
    for match in re.finditer("[^.\d]", row):
        symbols.append(Symbol(match.group(0), match.start(), y))

part_numbers = []

for number in numbers:
    y_range = range(number.y - 1, number.y + 2)  # +2 because stop is exclusive
    x_range = range(number.x1 - 1, number.x2 + 2)
    for symbol in symbols:
        if symbol.x in x_range and symbol.y in y_range:
            part_numbers.append(number.value)
            break
    print(number.value, list(x_range), list(y_range))

print(sum(part_numbers))
