fileObj = open("day01/input.txt", "r")
words = fileObj.read().splitlines()
increases = 0
i = 1
while i < len(words):
    if (int(words[i - 1]) < int(words[i])):
        increases += 1
    i += 1

print(increases)