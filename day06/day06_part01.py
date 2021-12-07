from os import O_TRUNC

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()
    fish = input[0].split(',')

    i = 0
    while i < len(fish):
        fish[i] = int(fish[i])
        i += 1
    day = 0
    while day < 80:
        i = 0
        toAdd = 0
        while i < len(fish):
            if (fish[i] == 0):
                fish[i] = 6
                toAdd += 1
            else:
                fish[i] -= 1
            i += 1
        while toAdd > 0:
            fish.append(8)
            toAdd -= 1
        day += 1
    print(len(fish))

if __name__ == "__main__":
    main()