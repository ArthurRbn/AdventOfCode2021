from os import O_TRUNC

global flashes
    
def recurse(tab, i, j):
    global flashes

    if (tab[i][j][1] == True):
        return tab
    temp_i = i - 1 if i > 0 else i
    temp_j = j - 1
    if (tab[i][j][0] > 9 and tab[i][j][1] == False):
        tab[i][j] = (0, True)
        flashes += 1
    while temp_i <= i + 1:
        temp_j = j - 1 if j > 0 else j
        if temp_i == len(tab):
            return tab
        while temp_j <= j + 1:
            if temp_j == len(tab[i]):
                break
            if tab[temp_i][temp_j][1] == False:
                tab[temp_i][temp_j] = (tab[temp_i][temp_j][0] + 1, tab[temp_i][temp_j][1])
            if tab[temp_i][temp_j][0] > 9 and tab[temp_i][temp_j][1] == False:
                tab = recurse(tab, temp_i, temp_j)
            temp_j += 1
        temp_i += 1
    return tab

def processFlash(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j][0] > 9 and tab[i][j][1] == False:
                tab = recurse(tab, i, j)
    return tab

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()
    tab = []
    global flashes
    flashes = 0

    for line in input:
        newLine = []
        for char in line:
            newLine.append((int(char), False))
        tab.append(newLine)
    for z in range (100):
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                tab[i][j] = (tab[i][j][0] + 1, False)
        tab = processFlash(tab)
    print(flashes, "flashes")
    
if __name__ == "__main__":
    main()