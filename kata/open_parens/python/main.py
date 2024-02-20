import sys


def process_line(line):
    stack = []
    for char in line:
        if char == ")":
            if stack[-1] != "(":
                print("no")
                return
            stack.pop()
        else:
            stack.append(char)
    if stack != []:
        print("no")
        return
    print("yes")


def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        process_line(line)


if __name__ == "__main__":
    main()
