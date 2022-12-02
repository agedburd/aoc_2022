from dataclasses import dataclass

@dataclass
class Elf:
    food_inv: list[int]

    @property
    def calories(self) -> int:
        return sum(self.food_inv, 0)