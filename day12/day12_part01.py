from os import O_TRUNC

def find_path(path, graph):
    print("path", path)
    print(graph)
    possibilities = []
    removed = True
    while removed == True:
        removed = False
        for idx, line in enumerate(graph):
            for room in line:
                if room.find(path[-1]) != -1:
                    possibilities.append(line)
                    del graph[idx:idx+1]
                    removed = True
                    break
            if removed:
                break
    print(graph)
    print(possibilities)
    for line in possibilities:
        find_path(path + line, graph)

def main():
    fileObj = open("test.txt", "r")
    input = fileObj.read().splitlines()
    starts = []
    graph = []

    for line in input:
        if line.find("start") != -1:
            starts.append(line.split("-"))
        else:
            graph.append(line.split("-"))
    # for line in starts:
    find_path(starts[0], graph.copy())

if __name__ == "__main__":
    main()