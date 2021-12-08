from os import O_TRUNC

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()
    crabs = input[0].split(',')

    for i in range(len(crabs)):
        crabs[i] = int(crabs[i])
    nearest  = min(crabs)
    furthest = max(crabs)

    fuel = 10000000
    for i in range (nearest, furthest + 1):
        newTry = 0
        for crab in crabs:
            newTry += abs(i - crab)
        if newTry < fuel:
            fuel = newTry
    print(fuel)


if __name__ == "__main__":
    main()