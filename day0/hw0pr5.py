import os
import os.path
import csv

"""
This code goes through all of the phone book files and stores all of the information found
into a csv
"""

def get_all_txt_files(path = "."):
    """This function walks through the subdirectories of the given path and returns a list of all
    the text file directories nested in this path as well as text files within the initial directory"""
    AllFiles = list(os.walk(path)) #getting all files into a data structure
    all_txt_files = []
    file_list = []

    for dir_tuple in AllFiles:
        file_list = dir_tuple[2]
        for file_name in file_list:
            if file_name[-3:] == 'txt':
                all_txt_files.append(dir_tuple[0]+'/'+file_name)
    return all_txt_files

def create_phone_book_csv(dir = "./phone_book.csv"):
    """
    This function goes through all of the text files in a given directory and
    the nested subdirectories and stores all relevant phone book information
    in a single csv file"""
    all_phone_files = get_all_txt_files("./phone_files")

    all_phone_info = []

    for phone_file in all_phone_files:
        f = open(phone_file,'r',encoding = 'latin1')
        contents = f.read()
        content_list = contents.split()

        if content_list[-2][-1] == ",":
            last_name = content_list[-2][:-1]
            first_name = content_list[-1]
        else:
            last_name = content_list[-1]
            first_name = content_list[-2]

        numbers = ['0','1','2','3','4','5','6','7','8','9']
        phone_number = ""
        for item in content_list:
            for character in item:
                if character in numbers:
                    phone_number += character

        phone_info = (last_name,first_name,phone_number)
        all_phone_info.append(phone_info)

    download_dir = "./phone_book.csv"
    csv = open(download_dir, "w")

    column_title_row = "Last Name, First Name, Phone Number (Digits Only)\n"
    csv.write(column_title_row)

    for phone_info in all_phone_info:
        csv_info = ','.join(map(str,phone_info))+"\n"
        csv.write(csv_info)

def print_phone_book_csv(dir = "./phone_book.csv"):
    """
    This function prints out line by line, the contents of
    a specified csv file"""
    with open(download_dir, 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

def main(dir):
