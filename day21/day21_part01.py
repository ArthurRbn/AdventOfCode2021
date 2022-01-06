from os import O_TRUNC
import posix

class Player:
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos
        self.score = 0

    def addScore(self, result):
        self.pos += result
        if self.pos % 10 == 0:
            self.pos = 10
        else:
            self.pos = self.pos % 10
        self.score += self.pos

    def dump_info(self):
        print("Player", self.id, "is at position", self.pos, "with a score of", self.score)

def check_end(players):
    for i in players:
        if i.score >= 1000:
            return False
    return True

def main():
    fileObj = open("input.txt", "r")
    input = fileObj.read().splitlines()
    players = []
    dice = 0

    for line in input:
        players.append(Player(int(line[7]), int(line[-1])))

    while check_end(players):
        for i in players:
            tour = (dice % 100) + 1 + (dice % 100) + 2 + (dice % 100) + 3
            dice += 3
            i.addScore(tour)
            if not check_end(players):
                for i in players:
                    i.dump_info()
                    if i.score < 1000:
                        print('solution is', dice * i.score)
                exit(0)


if __name__ == "__main__":
    main()