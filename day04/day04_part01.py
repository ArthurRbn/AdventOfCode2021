def win(matrix, y ,k):
    i = 0
    while i < len(matrix[y]):
        if matrix[y][i] != '-1':
            return False
        i += 1
    if i == len(matrix[y]):
        return True
    i = 0
    while i < len(matrix):
        if matrix[i][k] != '-1':
            return False
    if i == len(matrix):
        return True

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

    while idx < len(input):
        if len(input[idx]) > 0:
            new_grid.append(input[idx].split())
        if len(input[idx]) == 0:
            grids.append(new_grid)
            new_grid = []
        idx += 1
    grids.append(new_grid)

    for nbr in numbers:
        for i in range(len(grids)):
            for y in range(len(grids[i])):
                for k in range(len(grids[i][y])):
                    if (grids[i][y][k] == nbr):
                        grids[i][y][k] = '-1'
                    if win(grids[i], y, k):
                        winning_grid(grids[i], nbr)

if __name__ == "__main__":
    main()