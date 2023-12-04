import os
import sys


def read_files_from_directory(directory):
    files = os.listdir(directory)
    longest_file_name = shortest_file_name = None
    first_file_second_c = first_file_last_c = None

    for file in files:

        if (longest_file_name is None) or len(file) > len(longest_file_name):
            longest_file_name = file
        elif (shortest_file_name is None) or len(file) < len(shortest_file_name):
            shortest_file_name = file

        if file[1] == 'c' and first_file_second_c is None:
            first_file_second_c = file
        elif first_file_second_c == None:
            first_file_second_c = 'No file with second letter c'

        if file[-1] == 'c' and first_file_last_c is None:
            first_file_last_c = file
        elif first_file_last_c == None:
            first_file_last_c = 'No file with last letter c'

    count_c = 0
    count_py = 0
    count_txt = 0
    count_docx = 0

    for files in files:
        if files.endswith('.c'):
            count_c += 1
        elif files.endswith('.py'):
            count_py += 1
        elif files.endswith('.txt'):
            count_txt += 1
        elif files.endswith('.docx'):
            count_docx += 1

    sorted_extensions = {
        '.c': count_c,
        '.py': count_py,
        '.txt': count_txt,
        '.docx': count_docx
    }

    with open('output.txt', 'w') as f:
        f.write('longest_file_name:' + longest_file_name + '\n')
        f.write('shortest_file_name:' + shortest_file_name + '\n')
        f.write('first_file_second_c:' + first_file_second_c + '\n')
        f.write('first_file_last_c:' + first_file_last_c + '\n')
        f.write('sorted_extensions:' + str(sorted_extensions) + '\n')


def main():
    directory = sys.argv[1]
    read_files_from_directory(directory)


main()

# python Partial.py C:\Users\scuta\Downloads\wetransfer_directory_2023-11-26_1228\directory
