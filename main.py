import sys
import rarfile

def readfile(fp):
    rf = rarfile.RarFile(fp)
    for f in rf.infolist():
        print(f.filename, f.file_size)
        if f.filename == "README":
            print(rf.read(f))

def main() -> None:
    print(f"Arguments count: {len(sys.argv)}")

    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

    fp = sys.argv[1]
    print(fp)

    readfile(fp)

if __name__ == "__main__":
    main()
