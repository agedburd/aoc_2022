from dataclasses import dataclass


@dataclass
class Rucksack:
    compartment_one: str
    compartment_two: str

    def __init__(self, items: str) -> None:
        items = list(items)
        self.compartment_one = "".join(items[:len(items) // 2])
        self.compartment_two = "".join(items[len(items) // 2:])

    @property
    def shared_items(self) -> set[str]:
        return set(self.compartment_one) & set(self.compartment_two)

    @property
    def bag_contents(self) -> str:
        return self.compartment_one + self.compartment_two
