from pathlib import Path


def get_scores(*args: str) -> tuple[int]:
    """Returns two ints. First int is score for first arg, second int is score for second arg."""
    positions = ["Rock", "Paper", "Scissors"]
    score_one = positions.index(args[0]) + 1
    score_two = positions.index(args[1]) + 1
    winner = ["hand_one", "hand_two", "draw"][
        (positions.index(args[0]) - positions.index(args[1]) + 2) % 3
    ]

    if winner == "hand_one":
        score_one += 6
    elif winner == "hand_two":
        score_two += 6
    else:
        score_one += 3
        score_two += 3

    return score_one, score_two


def throw_game(*args: str) -> int:
    positions = ["Rock", "Paper", "Scissors"]

    if args[1] == "Draw":
        return 4 + positions.index(args[0])
    elif args[1] == "Win":
        return 7 + (positions.index(args[0]) + 1) % 3
    else:
        return 1 + (positions.index(args[0]) - 1) % 3


input_values = Path("input.txt").read_text()
input_values = input_values.replace("A", "Rock")
input_values = input_values.replace("B", "Paper")
input_values = input_values.replace("C", "Scissors")

decode_one = input_values.replace("X", "Rock")
decode_one = decode_one.replace("Y", "Paper")
decode_one = decode_one.replace("Z", "Scissors")
decode_one = decode_one.split("\n")
decode_one = [i for i in decode_one if i]
scores = [get_scores(*i.split(" ")) for i in decode_one]

# part 1 answer
print(sum(i[1] for i in scores))

decode_two = input_values.replace("X", "Lose")
decode_two = decode_two.replace("Y", "Draw")
decode_two = decode_two.replace("Z", "Win")
decode_two = decode_two.split("\n")
decode_two = [i for i in decode_two if i]

# part 2 answer
print(sum(throw_game(*i.split(" ")) for i in decode_two))
