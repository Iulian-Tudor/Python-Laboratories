import os
import sys

def main():
    try:
        dir_path = sys.argv[1]

        if not os.path.isdir(dir_path):
            raise NotADirectoryError(f"{dir_path} is not a valid directory")

        i = 1
        for filename in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, filename)):
                base, ext = os.path.splitext(filename)
                new_filename = f"file{i}{ext}"
                try:
                    os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))
                    i += 1
                except Exception as e:
                    print(f"Error renaming file {filename}: {str(e)}")

    except IndexError:
        print("Please provide a directory path as a command line argument.")
    except NotADirectoryError as e:
        print(str(e))
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
