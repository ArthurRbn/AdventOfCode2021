def array_sum(window):
    total = 0
    for x in window:
        total += int(x)
    return total

def main():
    fileObj = open("day01/input.txt", "r")
    words = fileObj.read().splitlines()
    increases = 0
    i = 1
    while i < len(words):
        sub1 = words[i - 1:i + 2]
        sub2 = words[i:i + 3]
        if (array_sum(sub1) < array_sum(sub2)):
            increases += 1
        i += 1
    print(increases)

if __name__ == "__main__":
    main()
