from os import O_TRUNC

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()
    starts = []

    for line in input:
        if line.find("start") != -1:
            starts.append(line)
    print(starts)

if __name__ == "__main__":
    main()