def create_loadplan(lines) -> dict[int, list]:
    load_plan = {}
    end_of_diagram = 0
    for index, line in enumerate(lines):
        if line.strip() == "":
            end_of_diagram = index - 1
            break
    num_columns = len(lines[end_of_diagram].replace(" ", "").strip())
    pos = 1
    for i in range(num_columns):
        pack_list = []
        for line in reversed(lines[:num_columns-1]):
            if line[pos] == " ":
                break
            else:
                pack_list.append(line[pos])
        load_plan[i+1] = pack_list
        pos += 4
    return load_plan


def do_moves(start: int, lines: list, load_plan: dict) -> dict[int, list]:
    for line in lines[start:]:
        line = line.replace("move ", "").replace(
            " from ", "-").replace(" to ", "-").strip()
        commands = line.split("-")
        num_move = int(commands[0])
        from_move = int(commands[1])
        to_move = int(commands[2])
        for _ in range(num_move):
            item = load_plan[from_move].pop()
            load_plan[to_move].append(item)
    return load_plan


def part_one(f) -> str:
    with open(f, 'r') as input:
        result = ""
        lines = input.readlines()
        initial_plan = create_loadplan(lines)
        moves_start = len(initial_plan) + 1
        resulting_plan = do_moves(moves_start, lines, initial_plan)
        for _, v in resulting_plan.items():
            l = len(v)
            if l == 0:
                result += ""
            else:
                result += v[l-1]
    return result


if __name__ == "__main__":
    print(part_one("Python/5/input.txt"))
