#
# hw0pr2.py ~ phonebook analysis
#
# Name(s):
#

#
# be sure your file runs from this location,
# relative to the "phonebook" directories
#

import os
import os.path
import shutil


def how_many_txt_files(path):
    """ walks a whole directory structure
        and returns how many txt files are in it!

        call it with: how_many_txt_files(".")

        the (v1) (v2) etc. are different versions, to illustrate
        the process of _trying things out_ and _taking small steps_
    """
    # return 42  # just to check that it's working (v1)

    AllFiles = list(os.walk(path))
    # print(AllFiles)    # just to check out what's up (v2)

    print("AllFiles has length: ", len(AllFiles), "\n")

    for item in AllFiles:
        # print("item is", item, "\n")    (v3)
        foldername, LoDirs, LoFiles = item   # cool!
        print("In", foldername, "there are", end=" ")

        count = 0
        for dir_tuple in AllFiles:
            list_of_files = dir_tuple[2]
            for file_name in list_of_files:
                if file_name[-3:] == "txt":
                    count += 1
        print(count, ".txt files")
    return count   # fixed!

def get_depth(path):
    """
    This function takes in a file path and spits out how far into the subdirectories
    this path is
    """
    return path.count('/')

def find_deepest_dir(path):
    """
    This function walks through an entire directory and all subdirectories
    to find the subdirectory the deepest into the starting path
    """
    AllFiles = list(os.walk(path)) #getting all files
    max_depth = 0 #initializing values
    deepest_dir = '.'

    for dir_tuple in AllFiles:
        depth = get_depth(dir_tuple[0])
        if depth > max_depth:
            max_depth = depth
            deepest_dir = dir_tuple[0]
    return deepest_dir

def get_all_txt_files(path = "."):
    """This function walks through the subdirectories of the given path and returns a list of all
    the text file directories nested in this path"""
    AllFiles = list(os.walk(path)) #getting all files into a data structure
    all_txt_files = []
    file_list = []

    for dir_tuple in AllFiles:
        file_list = dir_tuple[2]
        for file_name in file_list:
            if file_name[-3:] == 'txt':
                all_txt_files.append(dir_tuple[0]+"/"+file_name)
    return all_txt_files

def find_most_digits(path = "."):
    """
    This function will walk through the given directory and all of its subdirectories
    to find the phone number in the directory with the greatest number of digits
    """
    phone_files = list(filter(lambda x: x[2:13] == 'phone_files', all_txt_files))
    most_digits = 0
    longest_number = "This variable is intentionally left blank"

    for phone_file in phone_files:
        f = open(phone_file,'r',encoding = 'latin1')
        contents = f.read()
        num_digits = count_digits_alt(contents)

        if num_digits > most_digits:
            most_digits = num_digits
            longest_number = phone_file
    return longest_number

def main():
    """ overall function to run all examples """

    print("Start of main()\n")

    # num_txt_files = how_many_txt_files(".")
    # print("num_txt_files in . and all subdirectories is", num_txt_files)

    print(find_deepest_dir('.'),'\n'*3)

    print("End of main()\n")


if __name__ == "__main__":
    main()
