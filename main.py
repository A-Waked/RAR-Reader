import sys
import getopt
import argparse
import os
from os import listdir
from os.path import isfile, join
import rarfile
import zipfile

def getfiles(path) -> str:
    print(path)
    return [f for f in listdir(path) if isfile(join(path, f))]

def readfile(fp):
    rf = rarfile.RarFile(fp)
    for f in rf.infolist():
        print(f.filename, f.file_size)
        if f.filename == "README":
            print(rf.read(f))

def main() -> None:
    argv = sys.argv[1:]

    ap = argparse.ArgumentParser(description='reads zip/rar type files and displays images found')

    ap.add_argument('path', metavar='FP', type=str, nargs='*', default=[os.getcwd()],
        help='file paths to read')
    ap.add_argument('-a', action='store_true', default=False,
        help='read all files in specified directory if specified or current directory if not provided')

    args = ap.parse_args()

    if isfile(args.path[0]) == False:
        args.a = True

    print(getfiles(args.path[0]))

    print(args)
    
if __name__ == "__main__":
    main()
