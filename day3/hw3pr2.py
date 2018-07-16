#
# hw3pr2.py
#
# Person or machine?  The rps-string challenge...
#
# This file should include your code for
#   + extract_features( rps ),               returning a dictionary of features from an input rps string
#   + score_features( dict_of_features ),    returning a score (or scores) based on that dictionary
#   + read_data( filename="rps.csv" ),       returning the list of datarows in rps.csv
#
# Be sure to include a short description of your algorithm in the triple-quoted string below.
# Also, be sure to include your final scores for each string in the rps.csv file you include,
#   either by writing a new file out or by pasting your results into the existing file
#   And, include your assessment as to whether each string was human-created or machine-created
#
#

"""
Short description of (1) the features you compute for each rps-string and
      (2) how you score those features and how those scores relate to "humanness" or "machineness"





"""


# Here's how to machine-generate an rps string.
# You can create your own human-generated ones!

import random

def gen_rps_string( num_characters ):
    """ return a uniformly random rps string with num_characters characters """
    result = ''
    for i in range( num_characters ):
        result += random.choice( 'rps' )
    return result

# Here are two example machine-generated strings:
rps_machine1 = gen_rps_string(200)
rps_machine2 = gen_rps_string(200)
# print those, if you like, to see what they are...
print(rps_machine1)
print(rps_machine2)

#this space is being used to test theories about the machine generated strings

def analyze(rps_machine_str):
    """This function is being used to test some theories about the rps_machine strings"""
    r_count = len(list(filter(lambda x: x=="r",rps_machine_str)))
    p_count = len(list(filter(lambda x: x=="p",rps_machine_str)))
    s_count = len(list(filter(lambda x: x=="s",rps_machine_str)))
    # print("\n","r count is",r_count,"\n","p count is",p_count,"\n","s count is",s_count)

    try:
        rp_ratio = r_count/p_count
    except:
        rp_ratio = 1000
    try:
        ps_ratio = p_count/s_count
    except:
        ps_ratio = 1000
    try:
        rs_ratio = r_count/s_count
    except:
        rs_ratio = 1000
    # print("\n","rp ratio is",rp_ratio,"\n","ps ratio is",ps_ratio,"\n","rs_ratio is",rs_ratio)
    return r_count,p_count,s_count,rp_ratio,ps_ratio,rs_ratio

def get_results(num_iterations = 1000):
    """This fuction will generate num_iterations rps strings and save their info to a csv file"""
    csv_info = []
    # labels = ["rps_string","r_count","p_count","s_count","rp_ratio","ps_ratio","rs_ratio"]
    # csv_info.append(labels)
    for i in range(1000):
        rps_machine_str = gen_rps_string(200)
        r_count,p_count,s_count,rp_ratio,ps_ratio,rs_ratio = analyze(rps_machine_str)
        csv_row = [i,r_count,p_count,s_count,rp_ratio,ps_ratio,rs_ratio]
        csv_info.append(csv_row)

    return csv_info

def store_results(csv_info,csv_name = "results.csv"):
    """
    Inputs:
    csv_info - list of nested lists where each nested list contains important data for one datapoint
    csv_name - name of the csv this function will write to
    Output:
    None

    This function takes in a list of nested lists and writes them to a csv file"""
    import csv
    with open(csv_name,'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in csv_info:
            writer.writerow(row)

def read_in_csv(csv_name = "results.csv"):
    """
    Inputs:
    csv_name - directory path to the csv file to be read in
    Output:
    csv_data - data read in from csv file as a list of lists

    This function reads in data from a csv file as a list of lists
    """

    import csv
    csv_data = []
    with open(csv_name) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            csv_data.append(row)
    return csv_data

csv_info = get_results(100000000)
store_results(csv_info)
csv_data = read_in_csv()

import numpy as np
rp_ratio = []
ps_ratio = []
rs_ratio = []

for row in csv_data:
    rp_ratio.append(float(row[4]))
    ps_ratio.append(float(row[5]))
    rs_ratio.append(float(row[6]))

print("\n")
print("max rp_ratio is", max(rp_ratio))
print("min rp_ratio is", min(rp_ratio))
print("avg rp_ratio is", np.average(rp_ratio))
print("standard deviation for rp_ratio is", np.std(rp_ratio))

print("\n")
print("max ps_ratio is", max(ps_ratio))
print("min ps_ratio is", min(ps_ratio))
print("avg ps_ratio is", np.average(ps_ratio))
print("standard deviation for ps_ratio is", np.std(ps_ratio))

print("\n")
print("max rs_ratio is", max(rs_ratio))
print("min rs_ratio is", min(rs_ratio))
print("avg rs_ratio is", np.average(rs_ratio))
print("standard deviation for rs_ratio is", np.std(rs_ratio))

# machine_info = ([max(rp_ratio),min(rp_ratio),np.average(rp_ratio),np.std(rp_ratio)],[max(ps_ratio),min(ps_ratio),np.average(ps_ratio),np.std(ps_ratio)],[max(rs_ratio),min(rs_ratio),np.average(rs_ratio),np.std(rs_ratio)]
machine_info = [rp_ratio,ps_ratio,rs_ratio]
csv_actual_info = read_in_csv("rps18.csv")

def classify(rps_str,machine_info,t = 1):
    """
    Inputs:
    rps_str - this is an rps string either human or machine generated
    machine_info - simulation generated data on how a machine generates an rps string
    t - the threshold within the rps string is machine
    Outputs:
    True or False - True is Human, False is Machine

    This function classifies a string as human generated or machine generated"""
    rp_ratio_list = machine_info[0]
    ps_ratio_list = machine_info[1]
    rs_ratio_list = machine_info[2]

    r_count,p_count,s_count,rp_ratio,ps_ratio,rs_ratio = analyze(rps_str)

    if np.average(rp_ratio_list) - t*np.std(rp_ratio_list) <= rp_ratio <= np.average(rp_ratio_list) + t*np.std(rp_ratio_list):
        if np.average(ps_ratio_list) - t*np.std(ps_ratio_list) <= rp_ratio <= np.average(ps_ratio_list) + t*np.std(ps_ratio_list):
            if np.average(rs_ratio_list) - t*np.std(rs_ratio_list) <= rp_ratio <= np.average(rs_ratio_list) + t*np.std(rs_ratio_list):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

M_or_H = []
for row in csv_actual_info:
    M_or_H.append(classify(row[1],machine_info))

num_H = len(list(filter(lambda x: x==True,M_or_H)))
print("Number of human rps_strings:",num_H)
num_M = len(list(filter(lambda x: x==False,M_or_H)))
print("Number of machine rps_strings:",num_M)




# from collections import defaultdict
#
# #
# # extract_features( rps ):   extracts features from rps into a defaultdict
# #
# def extract_features( rps ):
#     """ <include a docstring here!>
#     """
#     d = defaultdict( float )  # other features are reasonable
#     number_of_s_es = rps.count('s')  # counts all of the 's's in rps
#     d['s'] = 42                      # doesn't use them, however
#     return d   # return our features... this is unlikely to be very useful, as-is
#
#
#
#
#
#
# #
# # score_features( dict_of_features ): returns a score based on those features
# #
# def score_features( dict_of_features ):
#     """ <include a docstring here!>
#     """
#     d = dict_of_features
#     random_value = random.uniform(0,1)
#     score = d['s'] * random_value
#     return score   # return a humanness or machineness score
#
#
#
#
#
#
#
# #
# # read_data( filename="rps.csv" ):   gets all of the data from "rps.csv"
# #
# def read_data( filename="rps.csv" ):
#     """ <include a docstring here!>
#     """
#     # you'll want to look back at reading a csv file!
#     List_of_rows = []   # for now...
#     return List_of_rows
#
#
#
#
#
# #
# # you'll use these three functions to score each rps string and then
# #    determine if it was human-generated or machine-generated
# #    (they're half and half with one mystery string)
# #
# # Be sure to include your scores and your human/machine decision in the rps.csv file!
# #    And include the file in your hw3.zip archive (with the other rows that are already there)
# #
