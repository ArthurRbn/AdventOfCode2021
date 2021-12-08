from os import O_TRUNC

def toAgeArray(input):
    tab = []
    for i in range(9):
        tab.append(0)
    for fish in input:
        tab[fish] += 1
    return tab

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()
    fish = input[0].split(',')

    i = 0
    while i < len(fish):
        fish[i] = int(fish[i])
        i += 1
    ages = toAgeArray(fish)
    for i in range(256):
        newFish = ages[0]
        for y in range(len(ages) - 1):
            ages[y] = ages[y + 1]
        ages[6] += newFish
        ages[8] = newFish
    print(sum(ages))


if __name__ == "__main__":
    main()