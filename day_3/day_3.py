from pathlib import Path

from rucksack import Rucksack


def get_priority_value(letter: str) -> int:
    return ord(letter) - 96 if letter.islower() else ord(letter) - 38


data = Path("input.txt").read_text()
data = [i for i in data.split("\n") if i]
bags = [Rucksack(i) for i in data]

# answer for part 1
print(sum(sum(map(get_priority_value, i.shared_items)) for i in bags))

# answer for part 2
print(
    sum(
        get_priority_value(
            list(
                set.intersection(*[set(j.bag_contents) for j in bags[i:i+3]])
            )[0]
        )
        for i in range(0, len(bags), 3)
    )
)
