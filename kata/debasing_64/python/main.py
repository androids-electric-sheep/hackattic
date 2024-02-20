import base64
import sys


def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        print(base64.b64decode(line).decode("utf-8"))


if __name__ == "__main__":
    main()
