import math
from os import O_TRUNC
from collections import deque
 
def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()
    stack = deque()
    opening = "({[<"
    closing = ")}]>"
    score = 0
    total_score = []
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
    while len(stack) > 0:
        stack.pop()
    for line in input:
        for char in line:
            if opening.find(char) != -1:
                stack.append(char)
            elif closing.find(char) != -1:
                stack.pop()
        score = 0
        while len(stack) > 0:
            char = closing[opening.find(stack.pop())]
            if char == ")":
                score *= 5
                score += 1
            elif char == "]":
                score *= 5
                score += 2
            elif char == "}":
                score *= 5
                score += 3
            elif char == ">":
                score *= 5
                score += 4
        total_score.append(score)
    total_score.sort()
    print(total_score[math.floor(len(total_score) / 2)])
    
    
if __name__ == "__main__":
    main()