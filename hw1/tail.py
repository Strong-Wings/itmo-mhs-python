import sys
from collections import deque


def main():
    file_names = [None]
    lines_number = 17
    if len(sys.argv) > 1:
        file_names = sys.argv[1:]
        lines_number = 10

    for i in range(len(file_names)):
        stream = sys.stdin
        file_name = file_names[i]
        if file_name is not None:
            stream = open(str(file_name), "r")

        with stream as s:
            last_lines = deque(s, lines_number)

        if len(file_names) > 1:
            if i > 0:
                print()
            print(f"==> {file_name} <==")

        for line in last_lines:
            print(line, end="")


if __name__ == "__main__":
    main()
