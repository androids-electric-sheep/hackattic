import sys
from datetime import datetime, timedelta

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def main():
    baseline = datetime(day=1, month=1, year=1970)
    for line in sys.stdin.readlines():
        count = int(line.strip())
        delta = timedelta(days=count)
        new_date = baseline + delta
        print(days[new_date.weekday()])


if __name__ == "__main__":
    main()
