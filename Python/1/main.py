def partOne(f) -> str:
    maxCalories = 0
    elfCalories = 0
    with open(f, 'r') as input:
        lines = input.readlines()
        for line in lines:
            line = line.strip()
            if line != '':
                elfCalories += int(line)
            else:
                if elfCalories > maxCalories: maxCalories = elfCalories
                elfCalories = 0
    return f"Max calories: {maxCalories}"

def partTwo(f) -> str:
    topThreeCalories = 0
    elves = []
    elfCalories = 0
    with open(f, 'r') as input:
        lines = input.readlines()
        for line in lines:
            line = line.strip()
            if line != '':
                elfCalories += int(line)
            else:
                elves.append(elfCalories)
                elfCalories = 0
    elves.sort(reverse=True)
    topThreeCalories = elves[0] + elves[1] + elves[2]
    return f"Total of top three: {topThreeCalories}"


if __name__ == "__main__":
    print(partOne('Python/1/input.txt'))
    print(partTwo('Python/1/input.txt'))
