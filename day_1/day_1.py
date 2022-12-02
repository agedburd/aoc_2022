from pathlib import Path

from elf import Elf

input_values = Path("input.txt").read_text()
input_values = input_values.split("\n")

calorie_values = []

while input_values:
    temp = []
    while input_values:
        i = input_values.pop()
        if len(i) > 0:
            temp.append(int(i))
        else:
            calorie_values.append(temp)
            break

elves = [Elf(i) for i in calorie_values if i]

# answer to part 1
print(max(i.calories for i in elves))

elves = sorted(elves, key=lambda e: e.calories)

# answer to part 2
print(sum(i.calories for i in elves[-3:]))
