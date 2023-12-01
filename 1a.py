from aocd import data, submit

array = data.split("\n")

a, b = 0, 0

values = []

for line in array:
    for forwards in line:
        if forwards.isdigit():
            a = forwards
            break

    for backwards in reversed(line):
        if backwards.isdigit():
            b = backwards
            break
    values.append(int(a + b))


submit(sum(values))
