import sys


def main():
    file_name = None
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

    stream = sys.stdin
    if file_name is not None:
        stream = open(file_name, "r")
    with stream as s:
        for i, line in enumerate(s):
            print(f"{i + 1:6}\t{line}", end="")


if __name__ == "__main__":
    main()
