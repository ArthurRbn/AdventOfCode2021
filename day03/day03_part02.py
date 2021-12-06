def countOccurences(condition, toKeep, idx, input):
    one = 0
    zero = 0
    for x in input:
        if (x[idx] == "0"):
            zero += 1
        else:
            one += 1
    if (zero == one):
        return toKeep
    elif (condition == "More"):
        return "0" if zero > one else "1"
    elif (condition == "Less"):
        return "0" if zero < one else "1"

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()
    input2 = list(input)
    idx = 0
    while (len(input) > 1):
        most = countOccurences("More", "1", idx, input)
        input = list(filter(lambda x: (x[idx] == most), input))
        idx += 1
    # print("input", input)
    oxygen = input[0]

    idx = 0
    while (len(input2) > 1):
        most = countOccurences("Less", "0", idx, input2)
        input2 = list(filter(lambda x: (x[idx] == most), input2))
        idx += 1
    scrubber = input2[0]

    print(int(oxygen, 2) * int(scrubber, 2))

if __name__ == "__main__":
    main()