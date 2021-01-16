import sys
import getopt
import argparse
import os
import rarfile
import zipfile
from PIL import Image
from os import listdir
from os.path import isfile, join

class Reader():
    def concat_v(i1, i2):
        i3 = Image.new('RGB', (i1.width, i1.height + i2.height))
        i3.paste(i1, (0,0))
        i3.paste(i2, (0,i1.height))
        return i3

    def getfiles(path, fpath='') -> str:
        print(path)
        files = [f for f in listdir(path) if isfile(join(path, f))]
        return files
        #current file
        #files.insert(0, str(index(fpath)))

    def readfile(fp):
        def concat_v(i1, i2):
            i3 = Image.new('RGB', (i1.width, i1.height + i2.height))
            i3.paste(i1, (0,0))
            i3.paste(i2, (0,i1.height))
            return i3

        print(fp, 'received')
        rf = rarfile.RarFile(fp)
        i1 = Image.new('RGB', (0,0))
        image = None
        for f in rf.infolist():
            file = rf.extract(f.filename)
            print('unrar success')
            if image is None:
                image = Image.open(file)
            else:
                image = concat_v(image, Image.open(file))
            
            print(f.filename, f.file_size)

        return image


def main() -> None:
    argv = sys.argv[1:]

    ap = argparse.ArgumentParser(description='reads zip/rar type files and displays images found')

    # command-line arguments
    ap.add_argument('path', metavar='FP', type=str, nargs='*', default=[os.getcwd()],
        help='file paths to read')
    ap.add_argument('-a', action='store_true', default=False,
        help='read all files in specified directory starting from specified file')

    args = ap.parse_args()

    readfile('/home/abdul/Comics/images.rar')

    #if given path to directory rather than a file
    if isfile(args.path[0]) == False:
        args.a = True

    files = getfiles(args.path[0])

    

    for f in files:
        if os.path.splitext(f)[1] == '.rar':
            print('reading', f)
            i = readfile(args.path[0]+f)

    print(args)

