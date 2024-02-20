import sys


def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        index = len(line) - 1
        count = 0
        for char in line:
            if char == "#":
                count += pow(2, index)
            index -= 1
        print(count)


if __name__ == "__main__":
    main()
