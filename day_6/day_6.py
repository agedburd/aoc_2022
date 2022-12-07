from pathlib import Path

from elf_com import ElfCom

input_data = Path("input.txt").read_text()

round_1 = ElfCom()

# answer for part 1
for i in input_data:
    round_1.push_char(i)

    if round_1.start_of_packet:
        print(round_1.processed_char_count)
        break

round_2 = ElfCom()

# answer for part 2
for i in input_data:
    round_2.push_char(i)

    if round_2.start_of_message:
        print(round_2.processed_char_count)
        break