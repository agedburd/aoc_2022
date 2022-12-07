from dataclasses import dataclass

@dataclass
class ElfCom():
    def __init__(self) -> None:
        self.marker_window = []

    def push_char(self, char: str) -> None:
        self.marker_window.append(char)

    @property
    def start_of_packet(self) -> bool:
        return len(self.marker_window) >= 4 and len(set(self.marker_window[-4:])) == 4

    @property
    def start_of_message(self) -> bool:
        return len(self.marker_window) >= 14 and len(set(self.marker_window[-14:])) == 14

    @property
    def processed_char_count(self) -> bool:
        return len(self.marker_window)