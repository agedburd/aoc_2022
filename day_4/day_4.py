from pathlib import Path


def elf_to_range(elf: str) -> set[int]:
    temp = [int(i) for i in elf.split("-")]
    return set(range(temp[0], temp[1]+1))


def total_eclipse(elf_one: str, elf_two: str) -> bool:
    range_one = elf_to_range(elf_one)
    range_two = elf_to_range(elf_two)

    return any((set.issubset(range_one, range_two), set.issubset(range_two, range_one)))


def partial_eclipse(elf_one: str, elf_two: str) -> bool:
    range_one = elf_to_range(elf_one)
    range_two = elf_to_range(elf_two)

    return len(range_one & range_two) > 0


input_data = Path("input.txt").read_text()
input_data = [i.split(",") for i in input_data.split("\n") if i]

# part 1 answer
print(sum(1 if total_eclipse(i[0], i[1]) else 0 for i in input_data))

# part 2 answer
print(sum(1 if partial_eclipse(i[0], i[1]) else 0 for i in input_data))