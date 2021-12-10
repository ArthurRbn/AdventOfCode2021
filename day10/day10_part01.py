from os import O_TRUNC
from collections import deque
 
def main():
    fileObj = open("test.txt", "r")
    input = fileObj.read().splitlines()
    stack = deque()
    opening = "({[<"
    closing = ")}]>"
    score = 0
    removed = True

    while removed:
        removed = False
        for line in input:
            for char in line:
                if opening.find(char) != -1:
                    stack.append(char)
                elif closing.find(char) != -1:
                    wanted = stack.pop()
                    if opening.find(wanted) != closing.find(char):
                        input.remove(line)
                        removed = True
                        break
            if removed:
                break
    for i in input:
        print(i)
    
if __name__ == "__main__":
    main()