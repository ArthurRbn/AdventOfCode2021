from os import O_TRUNC

def main():
    fileObj = open("test.txt", "r")
    input = fileObj.read().splitlines()

if __name__ == "__main__":
    main()