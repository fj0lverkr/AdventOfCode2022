def partOne(f) -> int:
    """
    A rock X 1
    B Paper Y 2
    C Scissors Z 3
    """
    score = 0
    with open(f, 'r') as input:
        lines = input.readlines()
        for line in lines:
            line = line.strip()
            actions = line.split(' ')
            myAction = actions[1].upper()
            theirAction = actions[0].upper()
            match myAction:
                case "X":
                    score += 1
                    match theirAction:
                        case "A":
                            score += 3
                        case "B":
                            score += 0
                        case "C":
                            score += 6
                case "Y":
                    score += 2
                    match theirAction:
                        case "A":
                            score += 6
                        case "B":
                            score += 3
                        case "C":
                            score += 0
                case "Z":
                    score += 3
                    match theirAction:
                        case "A":
                            score += 0
                        case "B":
                            score += 6
                        case "C":
                            score += 3
    return score

def partTwo(f) -> int:
    """
    A rock X 1 lose
    B Paper Y 2 draw
    C Scissors Z 3 win
    """
    score = 0
    with open(f, 'r') as input:
        lines = input.readlines()
        for line in lines:
            line = line.strip()
            actions = line.split(' ')
            expectedResult = actions[1].upper()
            theirAction = actions[0].upper()
            match theirAction:
                case "A":
                    match expectedResult:
                        case "X":
                            #expected to lose (0) against rock so play scissors (3)
                            score += 3
                        case "Y":
                            #expected to draw (3) against rock so play rock (1)
                            score += 4
                        case "Z":
                            #expected to win (6) against rock so play paper (2)
                            score += 8
                case "B":
                    match expectedResult:
                        case "X":
                            #expected to lose (0) against paper so play rock (1)
                            score += 1
                        case "Y":
                            #expected to draw (3) against paper so play paper (2)
                            score += 5
                        case "Z":
                            #expected to win (6) against paper so play scissors (3)
                            score += 9
                case "C":
                    match expectedResult:
                        case "X":
                            #expected to lose (0) against scissors so play paper (2)
                            score += 2
                        case "Y":
                            #expected to draw (3) against scissors so play scissors (3)
                            score += 6
                        case "Z":
                            #expected to win (6) against scissors so play rock (1)
                            score += 7
    return score

if __name__ == "__main__":
    print(partOne('Python/2/input.txt'))
    print(partTwo('Python/2/input.txt'))