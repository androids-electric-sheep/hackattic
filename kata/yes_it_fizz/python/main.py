import sys


def fizzbuzz(i):
    mod_3 = i % 3
    mod_5 = i % 5
    if mod_3 == 0 and mod_5 == 0:
        print("FizzBuzz")
    elif mod_3 == 0:
        print("Fizz")
    elif mod_5 == 0:
        print("Buzz")
    else:
        print(i)


def main():
    n, m = [int(i) for i in sys.stdin.read().strip().split()]
    for i in range(n, m + 1):
        fizzbuzz(i)


if __name__ == "__main__":
    main()
