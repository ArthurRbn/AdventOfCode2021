fileObj = open("day02/input.txt", "r")
lines = fileObj.read().splitlines()
position = 0
depth = 0
aim = 0

for x in lines:
    if (x.find('forward') != -1):
        position += int(x.split(" ", 1)[1])
        depth += aim * int(x.split(" ", 1)[1])
    elif (x.find('down') != -1):
        # depth += int(x.split(" ", 1)[1])
        aim += int(x.split(" ", 1)[1])
    elif (x.find('up') != -1):
        # depth -= int(x.split(" ", 1)[1])
        aim -= int(x.split(" ", 1)[1])

print(position * depth)