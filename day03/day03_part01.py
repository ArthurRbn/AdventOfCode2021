fileObj = open("input.txt", "r")
lines = fileObj.read().splitlines()
one = 0
zero = 0
result = ""
invert_result = ""

for idx in range(len(lines[0])):
    for x in lines:
        if (x[idx] == "0"):
            zero += 1
        else:
            one += 1
    if (zero > one):
        result = result + "0"
    else:
        result = result + "1"
    zero = 0
    one = 0

for c in result:
    if (c == "1"):
        invert_result = invert_result + "0"
    else:
        invert_result = invert_result + "1"

print(int(result, 2) * int(invert_result, 2))