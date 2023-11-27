import os
import sys

def main():
    try:
        dir_path = sys.argv[1]
        file_ext = sys.argv[2]

        if not os.path.isdir(dir_path):
            raise NotADirectoryError(f"{dir_path} is not a valid directory")

        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(file_ext):
                    try:
                        with open(os.path.join(root, file), 'r') as f:
                            print(f.read())
                    except Exception as e:
                        print(f"Error reading file {file}: {str(e)}")

    except IndexError:
        print("Please provide a directory path and a file extension as command line arguments.")
    except NotADirectoryError as e:
        print(str(e))
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
