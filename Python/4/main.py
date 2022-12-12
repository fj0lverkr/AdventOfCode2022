def part_one(f) -> int:
    result = 0
    with open(f, 'r') as input:
        pairs = input.readlines()
        for pair in pairs:
            pair = pair.strip()
            split_pair = pair.split(',')
            elf_one = split_pair[0]
            elf_two = split_pair[1]
            elf_one_split = elf_one.split('-')
            elf_two_split = elf_two.split('-')
            elf_one_start = int(elf_one_split[0])
            elf_two_start = int(elf_two_split[0])
            elf_one_end = int(elf_one_split[1])
            elf_two_end = int(elf_two_split[1])
            if (elf_one_start <= elf_two_start and elf_one_end >= elf_two_end) or (elf_two_start <= elf_one_start and elf_two_end >= elf_one_end):
                result += 1
    return result


if __name__ == "__main__":
    print(part_one('Python/4/input.txt'))
