import os
import shutil
from pathlib import Path
import argparse

def sort_files(path_from, path_to):
    for element in path_from.iterdir():
        try:
            if element.is_file():
                ext = element.suffix
                if ext:
                    path_to_ext = path_to / ext[1:]
                    if not path_to_ext.exists():
                        path_to_ext.mkdir()
                    shutil.move(element, path_to_ext / element.name)
            elif element.is_dir():
                sort_files(element, path_to)
        except Exception as e:
            print(f'An error occurred while processing {element}: {e}. Moving to the next element')
            continue

def main():
    parser = argparse.ArgumentParser(description='Sort files by extension')
    parser.add_argument('path_from', type=str, help='Path to the directory for sorting')
    parser.add_argument('--path_to', type=str, help='Path to the sorted directory (default: "dist")', default='dist')
    args = parser.parse_args()
    path_from = Path(args.path_from)
    path_to = Path(args.path_to)
    if not path_from.exists():
        print(f'Path {path_from} does not exist')
        return
    if not path_to.exists():
        path_to.mkdir()

    sort_files(path_from, path_to)

if __name__ == '__main__':
    main()
    