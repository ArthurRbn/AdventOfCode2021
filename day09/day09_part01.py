from os import O_TRUNC

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()

    intTab = []
    for line in input:
        lineArr = []
        for char in line:
            lineArr.append(int(char))
        intTab.append(lineArr)

    riskLevel = 0
    for i in range(len(intTab)):
        for j in range(len(intTab[i])):
            if i != 0 and intTab[i][j] >= intTab[i - 1][j]:
                continue
            if i < len(intTab) - 1 and intTab[i][j] >= intTab[i + 1][j]:
                continue
            if j != 0 and intTab[i][j] >= intTab[i][j - 1]:
                continue
            if j < len(intTab[i]) - 1 and intTab[i][j] >= intTab[i][j + 1]:
                continue
            riskLevel += intTab[i][j] + 1
    print(riskLevel)
    
if __name__ == "__main__":
    main()