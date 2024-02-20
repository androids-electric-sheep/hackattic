import re
import string
import sys


def process_line(line):
    # Remove all prefixes whihc could be types
    matches = re.findall("^[a-z]{1,2}[0-9]*[A-Z]", line)
    if matches:
        line = line.replace(matches[0], "")
        line = matches[0][-1] + line

    # Convert remaining section to snake case
    new_string = line[0].lower()
    for char in line[1:]:
        if char in string.ascii_uppercase:
            new_string += "_" + char.lower()
        else:
            new_string += char
    print(new_string)


def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        process_line(line)


if __name__ == "__main__":
    main()
