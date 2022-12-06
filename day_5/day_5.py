from pathlib import Path


def initialize_stacks(starter: list[str]) -> dict[str, list[str]]:
    keys = starter.pop()
    keys = [int(i) for i in keys.split(" ") if i]
    output = {i: [] for i in keys}

    starter.reverse()
    starter = [[j[i:i+3] for i in range(0, len(j), 4)] for j in starter]

    for i in starter:
        for k in output:
            temp = i[k-1][1]

            if temp != " ":
                output[k].append(temp)

    return output


def parse_move_instruction(instruction: str) -> tuple[int]:
    instruction = instruction.split(" ")
    return tuple(int(i) for i in instruction if i.isdigit())


def CrateMover9000(stacks: dict[str, list[str]], containers: int, start: int, end: int) -> dict[str, list[str]]:
    for _ in range(containers):
        stacks[end].append(stacks[start].pop())

    return stacks


def CrateMover9001(stacks: dict[str, list[str]], containers: int, start: int, end: int):
    stacks[end].extend(stacks[start][len(stacks[start])-containers:])
    stacks[start] = stacks[start][:len(stacks[start])-containers]

    return stacks


input_data = Path("input.txt").read_text()
input_data = input_data.split("\n")
move_data = [i for i in input_data if "move" in i]
stack_data = [i for i in input_data if "move" not in i and i]
stacks = initialize_stacks(stack_data.copy())

for move in move_data:
    stacks = CrateMover9000(stacks, *parse_move_instruction(move))

# answer for part 1
print("".join(stacks[k][-1] for k in stacks))

stacks = initialize_stacks(stack_data.copy())

for move in move_data:
    stacks = CrateMover9001(stacks, *parse_move_instruction(move))

# answer for part 2
print("".join(stacks[k][-1] for k in stacks))
