PRIOS = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
         "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
         "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30,
         "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40,
         "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50,
         "Y": 51, "Z": 52}


def partOne(f) -> int:
    totalPrio = 0
    with open(f, 'r') as input:
        packs = input.readlines()
        for pack in packs:
            pack = pack.strip()
            commonItems = []
            compSize = int(len(pack)/2)
            firstComp = pack[0:compSize]
            secondComp = pack[compSize:]
            for x in firstComp:
                for y in secondComp:
                    if x == y:
                        commonItems.append(x)
            commonItems = set(commonItems)
            for item in commonItems:
                totalPrio += PRIOS[item]
    return totalPrio


def findBadge(packOne, packTwo, PackThree) -> str:
    result = list(set(packOne) & set(packTwo) & set(PackThree))
    return result[0]


def partTwo(f) -> int:
    totalPrio = 0
    currentLine = 0
    with open(f) as input:
        packs = input.readlines()
        while currentLine <= len(packs)-3:
            packsByGroup = packs[currentLine:currentLine+3]
            currentLine += 3
            badge = findBadge(packsByGroup[0].strip(
            ), packsByGroup[1].strip(), packsByGroup[2].strip())
            totalPrio += PRIOS[badge]
    return totalPrio


if __name__ == "__main__":
    print(partOne('Python/3/input.txt'))
    print(partTwo('Python/3/input.txt'))
