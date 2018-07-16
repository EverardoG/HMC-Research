#
# starter file for hw1pr2, cs35 spring 2017...
#

import csv
import numpy

#
# readcsv is a starting point - it returns the rows from a standard csv file...
#
def readcsv( csv_file_name ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( csv_file_name, newline='' )  # open for reading
        csvrows = csv.reader( csvfile )              # creates a csvrows object

        all_rows = []                               # we need to read the csv file
        for row in csvrows:                         # into our own Python data structure
            all_rows.append( row )                  # adds only the word to our list

        del csvrows                                  # acknowledge csvrows is gone!
        csvfile.close()                              # and close the file
        return all_rows                              # return the list of lists

    except FileNotFoundError as e:
        print("File not found: ", e)
        return []



#
# write_to_csv shows how to write that format from a list of rows...
#  + try   write_to_csv( [['a', 1 ], ['b', 2]], "smallfile.csv" )
#
def write_to_csv( list_of_rows, filename ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( filename, "w", newline='' )
        filewriter = csv.writer( csvfile, delimiter=",")
        for row in list_of_rows:
            filewriter.writerow( row )
        csvfile.close()

    except:
        print("File", filename, "could not be opened for writing...")

def csv_analysis(csv_file="wds.csv"):
    """
    Inputs:
    csv_file - csv where each row is some word info, the first element is the word, and the second is the amount of times it shows up
    Outputs:
    rel_freq_dict - this is a dicitonary containing letters of the alphabet as keys and their relative frequency as values
    """

    csv_list = readcsv(csv_file)

    data = numpy.array(csv_list) #turning data into numpy array
    total = numpy.sum(data[:,1].astype(float)) #this is the total amount of times all words are used

    # data[:,1] = data[:,1].astype(numpy.float32) #This was an attempt at a more elegant solution, but for whatever reason I can't get all the numbers to be float types
    # print("data[:,1] is\n",data[:,1])
    #test_count = 0
    letter_dict = {}
    for row in data:
        letter = row[0][0]
        rel_freq = float(row[1])/total
        try:
            letter_dict[letter] += rel_freq
        except:
            letter_dict[letter] = rel_freq
        #test_count += rel_freq  #The purpose of test_count was to be sure all the values added up to 1. They do :)
    #print(test_count)
    return letter_dict

#
# csv_to_html_table_starter
#
#   Shows off how to create an html-formatted string
#   Some newlines are added for human-readability...
#
def csv_to_html_table_starter( csvdata ):
    """ csv_to_html_table_starter
           + an example of a function that returns an html-formatted string
        Run with
           + result = csv_to_html_table_starter( "example_chars.csv" )
        Then run
           + print(result)
        to see the string in a form easy to copy-and-paste...
    """
    # probably should use the readcsv function, above!

    csv_file = readcsv(csvdata)

    html_string = '<table>\n'    # start with the table tag
    for row in csv_file:
        html_string+="<tr>\n"
        for element in row:
            html_string += "<th>"+element+"</th>\n"
        html_string += "</tr>\n"
    html_string +="</table>\n"

    # html_string += '<tr>\n'
    #
    #
    # html_string += "place your table rows and data here!\n" # from list_of_rows !
    #
    # html_string += '</tr>\n'
    html_string += '</table>\n'
    return html_string


def main():
    """ run this file as a script """
    # LoL = readcsv( "wds.csv" )
    # print(LoL[:10])
    #
    # # test writing
    # write_to_csv( LoL[:10], "tenrows.csv" )
    #
    # # text csv_to_html_table_starter
    # output_html = csv_to_html_table_starter( "wds.csv" )
    # print("output_html is", output_html)

    print(csv_analysis())

if __name__ == "__main__":
    main()
