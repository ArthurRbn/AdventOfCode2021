from os import O_TRUNC

def same_segments(code, ref):
    count = 0
    for char in ref:
        if code.find(char) != -1:
            count += 1
    return count

def find_digits(line):
    mixed = line.split()
    found = []
    for i in range(10):
        found.append("")
    basics = 0
    while basics < 4:
        for code in mixed:
            if len(code) == 2:
                found[1] = code
                mixed.remove(code)
                basics += 1
            elif len(code) == 4:
                found[4] = code
                mixed.remove(code)
                basics += 1
            elif len(code) == 3:
                found[7] = code
                mixed.remove(code)
                basics += 1
            elif len(code) == 7:
                found[8] = code
                mixed.remove(code)
                basics += 1
    while len(mixed) > 0:
        for code in mixed:
            if len(code) == 6 and same_segments(code, found[1]) == 1:
                found[6] = code
                mixed.remove(code)
            elif len(code) == 6 and same_segments(code, found[1]) == len(found[1]):
                if same_segments(code, found[4]) == len(found[4]):
                    found[9] = code
                    mixed.remove(code)
                else:
                    found[0] = code
                    mixed.remove(code)
            elif len(code) == 5 and same_segments(code, found[4]) == 2:
                found[2] = code
                mixed.remove(code)
            elif len(code) == 5 and same_segments(code, found[1]) == len(found[1]):
                found[3] = code
                mixed.remove(code)
            elif len(code) == 5 and same_segments(code, found[4]) == 3:
                found[5] = code
                mixed.remove(code)
    return found

def find_value(digits, toFind):
    ok = True
    value = 0
    for digit in digits:
        ok = True
        for char in toFind:
            if digit.find(char) == -1:
                ok = False
        if ok and len(digit) == len(toFind):
            return value
        value += 1

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()
    digits = []
    parts = []
    decoded = 0
    total_decoded = 0
    for line in input:
        parts.append(line.split(' | ')[0])
        digits.append(line.split(' | ')[1])
    for line, number in zip(parts, digits):
        solved = find_digits(line)
        decoded = 0
        for nbr in number.split():
            decoded = decoded * 10 + find_value(solved, nbr)
        total_decoded += decoded
    print(total_decoded)

if __name__ == "__main__":
    main()