#
# starting examples for cs35, week1 "Web as Input"
#

import requests
import string
import json

"""
Examples to run for problem 1:

Web scraping, the basic command (Thanks, Prof. Medero!)

#
# basic use of requests:
#
url = "https://www.cs.hmc.edu/~dodds/demo.html"  # try it + source
result = requests.get(url)
text = result.text   # provides the source as a large string...

#
# try it for another site...
#




#
# let's try the Open Google Maps API -- also provides JSON-formatted data
#   See the webpage for the details and allowable use
#
# Try this one by hand - what are its parts?
# http://maps.googleapis.com/maps/api/distancematrix/json?origins=%22Claremont,%20CA%22&destinations=%22Seattle,%20WA%22&mode=%22walking%22
#
# Take a look at the result -- perhaps using this nice site for editing + display:
#
# A nice site for json display and editing:  https://jsoneditoronline.org/
#
#
"""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# Problem 1
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#
# example of calling the google distance API
#
def google_api(Sources, Dests):
    """ Inputs: Sources is a list of starting places
                Dests is a list of ending places

        This function uses Google's distances API to find the distances
             from all Sources to all Dests.
        It saves the result to distances.json

        Problem: right now it only works with the FIRST of each list!
    """
    print("Start of google_api")

    url="http://maps.googleapis.com/maps/api/distancematrix/json"

    if len(Sources) < 1 or len(Dests) < 1:
        print("Sources and Dests need to be lists of >= 1 city each!")
        return

    start = ('|').join(Sources)
    end = ('|').join(Dests)
    my_mode="driving"  # walking, biking

    inputs={"origins":start,"destinations":end,"mode":my_mode}
    result = requests.get(url,params=inputs)
    print('\n\n\n The json contains\n',result.text,'\n\n\n')
    data = result.json()

    #
    # save this json data to the file named distances.json
    #
    filename_to_save = "distances.json"
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file
    f.close()                                   # and closes the file
    print("\nFile", filename_to_save, "written.\n")
    # no need to return anything, since we're better off reading it from file later...
    return



#
# example of handling json data via Python's json dictionary
#
def json_process():
    """ This function reads the json data from "distances.json"

        It should build a formatted table of all pairwise distances.
        _You_ decide how to format that table (better than JSON!)
    """
    filename_to_read = "distances.json"
    f = open( filename_to_read, "r" )
    string_data = f.read()
    JD = json.loads( string_data )  # JD == "json dictionary"

    num_starts = len(JD["rows"])
    num_ends = len(JD["rows"][0]["elements"])

    start_list = JD["origin_addresses"]
    end_list = JD["destination_addresses"]

    print("Getting some distances:\n")
    row_count = 0
    for n in range(num_starts):
        element_count = 0
        print("From "+start_list[row_count])

        for m in range(num_ends):
            print(" ... to "+end_list[element_count]+" ==  "+JD["rows"][row_count]["elements"][element_count]["distance"]["text"])
            element_count += 1

        row_count += 1

    print("\nGetting some travel times:\n")
    row_count = 0
    for n in range(num_starts):
        element_count = 0
        print("From "+start_list[row_count])

        for m in range(num_ends):
            print(" ... to "+end_list[element_count]+" ==  "+JD["rows"][row_count]["elements"][element_count]["duration"]["text"])
            element_count += 1

        row_count += 1

    # we may want to continue operating on the whole json dictionary
    # so, we return it:
    return JD

#
# a main function for lab problem 1 (the multicity distance problem)
#
def main():
    """ top-level function for testing problem 1
    """

    Dests = ['Seattle,WA','Miami,FL','Boston,MA']  # starts
    Sources = ['Claremont,CA','Seattle,WA','Philadelphia,PA'] # ends
    #if 1:  # do we want to run the API call?
    google_api(Sources, Dests)  # get file
    json_process()

    Dests1 = ["Needham,MA","Saint Louis,MI"]
    Sources1 = ["Long Beach,CA","Claremont,CA"]

    google_api(Sources1, Dests1)
    json_process()


if __name__ == "__main__":
    main()
