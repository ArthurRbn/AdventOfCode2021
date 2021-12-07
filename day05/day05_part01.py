def init_tab(size, fill):
    tab = []
    for r in range(size):
        row = []
        for c in range(size):
            row.append(fill)
        tab.append(row)
    return tab

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()
    tab = init_tab(1000, 0)    
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0

    for line in input:
        vectors = [line.split(' ')[0]] + [line.split(' ')[-1]]
        start_x = int(vectors[0].split(',')[0])
        start_y = int(vectors[0].split(',')[1])
        end_x = int(vectors[1].split(',')[0])
        end_y = int(vectors[1].split(',')[1])
        offset_x = +1 if start_x - end_x < 0 else -1
        offset_y = +1 if start_y - end_y < 0 else -1
        while start_x != end_x or start_y != end_y:
            tab[start_y][start_x] += 1
            if start_x != end_x:
                start_x += offset_x
            if start_y != end_y:
                start_y += offset_y
        tab[start_y][start_x] += 1
    overlapping = 0
    for line in tab:
        for char in line:
            if char > 1:
                overlapping += 1
    print(overlapping)    

if __name__ == "__main__":
    main()