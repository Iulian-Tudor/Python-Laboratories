import os
import sys

def main():
    try:
        dir_path = sys.argv[1]

        if not os.path.isdir(dir_path):
            raise NotADirectoryError(f"{dir_path} is not a valid directory")

        total_size = 0
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                try:
                    total_size += os.path.getsize(os.path.join(root, file))
                except Exception as e:
                    print(f"Error accessing file {file}: {str(e)}")

        print(f"Total size of all files: {total_size} bytes")

    except IndexError:
        print("Please provide a directory path as a command line argument.")
    except NotADirectoryError as e:
        print(str(e))
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
