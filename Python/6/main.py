def isUniqueChars(st):
    char_set = [False] * 128
    for i in range(0, len(st)):
        val = ord(st[i])
        if char_set[val]:
            return False
        char_set[val] = True
    return True


def solve(f, packet_len) -> int:
    with open(f, 'r') as input:
        line = input.readline()
        start = 0
        end = packet_len
        code = line[start:end]
        while not isUniqueChars(code):
            start += 1
            end += 1
            code = line[start:end]
        print(code)
        return end


if __name__ == '__main__':
    print(solve('Python/6/input.txt', 4))
    print(solve('Python/6/input.txt', 14))
