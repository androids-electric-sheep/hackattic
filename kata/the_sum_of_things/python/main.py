import sys


def is_hex(line):
    return line.startswith("0x")


def is_octal(line):
    return line.startswith("0o")


def is_binary(line):
    return line.startswith("0b")


def is_integer(line):
    try:
        int(line)
    except:
        return False
    else:
        return True


def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        count = 0
        for piece in line.split(" "):
            if is_hex(piece):
                count += int(piece, 16)
            elif is_octal(piece):
                count += int(piece, 8)
            elif is_binary(piece):
                count += int(piece, 2)
            elif is_integer(piece):
                count += int(piece)
            else:
                count += ord(piece)
        print(count)


if __name__ == "__main__":
    main()
