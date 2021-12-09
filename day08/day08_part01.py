from os import O_TRUNC

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()
    parts = []
    for line in input:
        parts.append(line.split(' | ')[1])
    count = 0
    for line in parts:
        for code in line.split():
            if (len(code) == 2 or len(code) == 4 or len(code) == 3 or len(code) == 7):
                count += 1
    print(count)
    


if __name__ == "__main__":
    main()