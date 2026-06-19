# Reading a file with the open function and read method:
# The provided file shouldn’t be as big as twice of the system’s memory.
# By default, the open function opens the given file in read ('r') mode.

with open('file_name.txt', 'r') as temporary_filename:
    print('The file has been opened.')
    file_content = temporary_filename.read()
    print(file_content)
    
print('The file has been closed.')

# O/p:
# The file has been opened.
# file_data
# The file has been closed.

# Why is the 'with' keyword used ?
# It ensures that Python performs clean-up processes when handling the file.
# Otherwise, it is possible for the program to run into an error midway through execution,
# not close the file, and end up with corrupted content.

# Also, while using the "with" command, in the back end, it calls the dunder methods __enter__() and
# __exit__() respectively to perform the file operations.

# By default, the open function will search the file in the same directory as the .py file.
# If the mentioned file doesn't exist on the system, FileNotFound error will get populated.

# Reading a file line-by-line:

with open('file_name.txt', 'r') as temporary_filename:
    print('The file has been opened.')
    for line in temporary_filename:
        print(line)  # To get the same output as above but with single lines, instead of a whole paragraph.

with open('file_name.txt', 'r') as temporary_filename:
    print('The file has been opened.')
    for line in temporary_filename:
        print(line.rstrip())  # To remove the right side spaces from the output.

# Writing to a file: If the file is not present, it’ll be created and if present, it’ll be over-written.

with open('file_name.txt', 'w') as temporary_filename:
    temporary_filename.write('Hello Python !!!')  # The file file_name.txt will be created if not present, or else will be over-written.

# Appending to a file (Adding data to an already present file):

with open('file_name.txt', 'a') as temporary_filename:
    temporary_filename.write('Bye Python !!!')  # The file file_name.txt will be created if not present, or else the data will be updated at the end of the file.
