import sys


def handle_concat(compressed_string, current_char, current_count):
    if current_count <= 2:
        compressed_string += current_count * current_char
    else:
        compressed_string += str(current_count) + current_char
    return compressed_string


def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        current_char = line[0]
        current_count = 1
        compressed_string = ""
        for char in line[1:]:
            if char == current_char:
                current_count += 1
                continue
            compressed_string = handle_concat(
                compressed_string, current_char, current_count
            )
            current_char = char
            current_count = 1
        compressed_string = handle_concat(
            compressed_string, current_char, current_count
        )
        print(compressed_string)


if __name__ == "__main__":
    main()
