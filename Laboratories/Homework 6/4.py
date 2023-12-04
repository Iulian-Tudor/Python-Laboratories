import os
import sys
import collections


def count_file_extensions(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        raise ValueError(f"Directory {directory} does not exist")

    # Check if the directory is readable
    if not os.access(directory, os.R_OK):
        raise PermissionError(f"No read permissions for directory {directory}")

    # Get a list of all files in the directory
    files = os.listdir(directory)

    # If the directory is empty, raise an error
    if not files:
        raise ValueError(f"Directory {directory} is empty")

    # Use collections.Counter to count the file extensions
    cnt = collections.Counter(os.path.splitext(filename)[1] for filename in files)

    return cnt


def main():
    # Check if a directory path was provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    try:
        # Get the count of file extensions
        counts = count_file_extensions(directory)

        # Print the counts
        for ext, count in counts.items():
            print(f"{ext}: {count}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
