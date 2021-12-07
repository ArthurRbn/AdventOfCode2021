def win(matrix):
    x = 0
    while x < len(matrix):
        i = 0
        while i < len(matrix[x]):
            if matrix[x][i] != '-1':
                break
            i +=1
        if i == len(matrix[x]):
            return True
        x += 1
    
    i = 0
    while i < len(matrix[0]):
        x = 0
        while x < len(matrix):
            if matrix[x][i] != '-1':
                break
            x += 1
        if x == len(matrix):
            return True
        i += 1
    return False

def winning_grid(matrix, number):
    total = 0
    for i in range(len(matrix)):
        for y in range(len(matrix[i])):
            if (matrix[i][y] != '-1'):
                total += int(matrix[i][y])
    print(total * int(number))
    exit (0)

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()

    numbers = input[0].split(",")
    input = input[2:];
    grids= []
    new_grid = []
    idx = 0
    last_win = []
    last_win_nbr = 0

    while idx < len(input):
        if len(input[idx]) > 0:
            new_grid.append(input[idx].split())
        if len(input[idx]) == 0:
            grids.append(new_grid)
            new_grid = []
        idx += 1
    grids.append(new_grid)

    for nbr in numbers:
        i = 0
        while i < len(grids):
            for y in range(len(grids[i])):
                for k in range(len(grids[i][y])):
                    if (grids[i][y][k] == nbr):
                        grids[i][y][k] = '-1'
            if win(grids[i]):
                last_win = grids[i]
                last_win_nbr = nbr
                del grids[i:i+1]
                i -= 1
            i += 1
    winning_grid(last_win, last_win_nbr)

if __name__ == "__main__":
    main()