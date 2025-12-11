import sys


class Stats:
    lines: int = 0
    words: int = 0
    bytes: int = 0
    filename = None

    def __init__(self, l, w, b, f):
        self.lines = l
        self.words = w
        self.bytes = b
        self.filename = f

    def __add__(self, other: "Stats") -> "Stats":
        return Stats(
            self.lines + other.lines,
            self.words + other.words,
            self.bytes + other.bytes,
            self.filename,
        )

    def __str__(self) -> str:
        data = f"{self.lines:8}{self.words:8}{self.bytes:8}"
        if self.filename:
            data = f"{data} {self.filename}"
        return data


def main():
    file_names = [None]
    if len(sys.argv) > 1:
        file_names = sys.argv[1:]

    total_stats = Stats(0, 0, 0, "total")
    for file_name in file_names:
        stream = sys.stdin
        if file_name is not None:
            stream = open(file_name, "r")

        stats = Stats(0, 0, 0, file_name)
        with stream as s:
            for line in s:
                stats.lines += line.endswith("\n")
                stats.words += len(line.split())
                stats.bytes += len(line)

        total_stats += stats
        print(stats)

    if len(file_names) > 1:
        print(total_stats)


if __name__ == "__main__":
    main()
