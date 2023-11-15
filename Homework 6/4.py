import os
import sys
from collections import defaultdict

def main():
    try:
        dir_path = sys.argv[1]

        if not os.path.isdir(dir_path):
            raise NotADirectoryError(f"{dir_path} is not a valid directory")

        ext_counts = defaultdict(int)
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                ext = os.path.splitext(file)[1]
                ext_counts[ext] += 1

        for ext, count in ext_counts.items():
            print(f"{ext}: {count}")

    except IndexError:
        print("Nu ai dat argumente valide.")
    except NotADirectoryError as e:
        print(str(e))
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()