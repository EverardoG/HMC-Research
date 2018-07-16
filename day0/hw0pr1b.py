#
# hw0pr1b.py
#

import os
import os.path
import shutil
import doctest

# Example 1: How many top-level directories are there in the inclass folder
#
def find_dirs():
    """ returns the number of directories in the "." folder,
        which is the "inclass folder"
    """
    path = "."
    # get ALL contents
    ListOfContents = os.listdir( path )
    print("Contents of", path, ":")
    print(ListOfContents)

    # check for directories
    ListOfDirectories = [] # start empty...
    for item in ListOfContents:
        newpath = path + "/" + item  # create path name: ./item
        if os.path.isdir( newpath ):
            print("Found a directory:", newpath)
            ListOfDirectories.append( item ) # add to our list!

    # yay!
    return ListOfDirectories

# Example 1: How many top-level directories are there in the inclass folder
#
def find_dirs1(path):
    """ returns the number of directories in the path folder,
        Note how close this is to the above!
    """
    # get ALL contents
    ListOfContents = os.listdir( path )
    print("Contents of", path, ":")
    print(ListOfContents)

    # check for directories
    ListOfDirectories = [] # start empty...
    for item in ListOfContents:
        newpath = path + "/" + item  # create path name: ./item
        if os.path.isdir( newpath ):
            print("Found a directory:", newpath)
            ListOfDirectories.append( item ) # add to our list!

    # yay!
    return ListOfDirectories

def num_top_level_files():
    """
    Input: None
    Output: number of files in the day1 folder
    This function counts the number of _files_ present in the top level folder.
    """
    list_dir = os.listdir(".")
    list_files = list(filter(lambda x: os.path.isfile(x), list_dir))
    num_files = len(list_files)
    return num_files

def num_top_level_files_arg(directory):
    """
    Input: directory - file path for folder
    Output: number of top level files in specified folder
    This function finds the number of top level files in the specified folder
    >>> num_top_level_files_arg(".")
    4
    """
    list_dir = os.listdir(directory)
    list_files = list(filter(lambda x: os.path.isfile(x), list_dir))
    num_files = len(list_files)
    return num_files

def find_most_files(current_dir,most = 0):
    """
    Inputs:
    current_dir - the current directory
    most - the current highest number of files in a folder
    Output:
    new_dir - the directory with the highest number of files
    new_most - the highest number of files in a directory
    """
    list_dir = os.listdir(current_dir)
    list_files = list(filter(lambda x: os.path.isfile(x), list_dir))
    list_subdir = list(filter(lambda x: os.path.isfile(x) == False, list_dir))
    num_files = len(list_files)

    if num_files > most:
        new_most = num_files
        new_dir = os.path.abspath(current_dir)
        print(new_dir)

    else:
        new_most = most
        new_dir = current_dir

    for subdir in list_subdir:
        find_most_files(subdir,new_most)

    return new_dir, new_most

# An example main() function - to keep everything organized!
#
def main():
    """ main function for organizing -- and printing -- everything """

    # sign on
    print("\n\nStart of main()\n\n")

    find_most_files(".")

    # sign off
    print("\n\nEnd of main()\n\n")

# This conditional will run main() when this file is executed:
#
if __name__ == "__main__":
    main()

# ++ The challenges:  Create and test as many of these five functions as you can.
#
# These are the lab challenges:

# hw0pr1b.py
# Displaying hw0pr1b.py.
