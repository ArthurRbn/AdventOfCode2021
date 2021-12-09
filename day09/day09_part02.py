from os import O_TRUNC

def cover_area(tab, line, char, size):
    if tab[line][char] == 'X':
        tab[line][char] = 'C'
        size += 1
        size = cover_area(tab, line, char, size)
    if line != 0 and tab[line - 1][char] == 'X':
        tab[line - 1][char] = 'C'
        size += 1
        size = cover_area(tab, line - 1, char, size)
    if line < len(tab) - 1 and tab[line + 1][char] == 'X':
        tab[line + 1][char] = 'C'
        size += 1
        size = cover_area(tab, line + 1, char, size)
    if char != 0 and tab[line][char - 1] == 'X':
        tab[line][char - 1] = 'C'
        size += 1
        size = cover_area(tab, line, char - 1, size)
    if char < len(tab[line]) - 1 and tab[line][char + 1] == 'X':
        tab[line][char + 1] = 'C'
        size += 1
        size = cover_area(tab, line, char + 1, size)
    return size

def findBassins(tab):
    sizes = []

    for line in range(len(tab)):
        for char in range(len(tab[line])):
            if (tab[line][char] == 'X'):
                sizes.append(cover_area(tab, line, char, 0))
    sizes.sort()
    total = 0
    for size in sizes[-3:]:
        if total == 0:
            total += size
        else:
            total *= size
    print(total)

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()

    intTab = []
    for line in input:
        lineArr = []
        for char in line:
            lineArr.append(int(char))
        intTab.append(lineArr)

    for i in range(len(intTab)):
        for j in range(len(intTab[i])):
            if intTab[i][j] < 9:
                intTab[i][j] = 'X'
    findBassins(intTab)
    
if __name__ == "__main__":
    main()