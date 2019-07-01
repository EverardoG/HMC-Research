import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import math
import statistics

Mean_Rent = {"Bay Ridge":[1338,1651], "Bedford-Stuyvesant":[1314, 2037], "Boerum Hill":[2027,2820],
"Buschwick": [1764, 2134], "Clinton Hill": [1868, 2389],
"Cobble Hill": [2011, 2767], "Crown Heights": [1123, 1894], "DUMBO": [3282, 4088],
"Fort Greene": [2233, 3032], "Greenpoint": [2092, 2559], "Park Slope": [2036, 2616],
"Williamsburg": [2356, 3217]}

percent_of_POC_2010 = {"Bay Ridge": 34, "Bedford-Stuyvesant":74, "Boerum Hill":58,
"Buschwick": 90, "Clinton Hill": 64,
"Cobble Hill": 25, "Crown Heights": 86, "DUMBO": 56,
"Fort Greene": 28,  "Greenpoint": 23, "Park Slope": 33,
"Williamsburg": 14}

percent_of_POC_2016 = {"Bay Ridge":28, "Bedford-Stuyvesant":84, "Boerum Hill":43,
"Buschwick": 58, "Clinton Hill": 53,
"Cobble Hill":21, "Crown Heights":21, "DUMBO":36,
"Fort Greene": 58, "Greenpoint": 31, "Park Slope": 23,
"Williamsburg": 31}

def percent_increase(initial_dict, final_dict):
    """
    finds the percent increase in mean rent of different zip codes in
    Brooklyn from 2010 to 2016

    output: a dictionary with a key of zip codes and values of percent increase of mean rents"""
    increase_dict = {}
    for key, value in initial_dict.items():
        initial_value = initial_dict[key]
        final_value = final_dict[key]
        percent_increase = (final_value-initial_value)/initial_value * 100
        increase_dict[key] = percent_increase
    return increase_dict

def graph_percent_increase(initial_dict, final_dict):
    """
    graphs the percent increae in mean rent of different zip codes in
    Brooklyn from 2010 to 2016
    """
    dictionary = plt.figure()

    D = percent_increase(initial_dict, final_dict)

    plt.bar(range(len(D)), D.values(), align='center', color='steelblue')
    plt.xticks(range(len(D)), D.keys(), rotation='vertical')
    plt.xlabel('Percent Difference')
    plt.ylabel('Brooklyn Neighborhoods')
    plt.title('Percent Increase of Rent in Brooklyn between 2010 and 2016')
    plt.tight_layout()
    plt.show()

'''
Which area experienced the largest increase in Rent?

Williamsburg
'''

def max_percent_increase(increase_dict):
    """
    finds the zip code that experienced the largest percent increase
    input (dict): increase_dict - dictionary of percent increases
    output: The zip code whose rent increased the most by percent value.
    """
    increase_list = list(d.values())
    largest_increase = max(increase_list)




def remove_least_POC(threshold, dict):
    """
    input: a dictionary, dict, that contains percentage of POC in different Brookly neighborhoods
           a value, threshold, which represents a percentage
    output: a dictionary with the elements of dict whose values are higher than threshold
    """

    return_dict = dict.copy()
    for values in dict:
        if return_dict[values] < threshold:
            del return_dict[values]

    return return_dict

"""
1. Which neighborhoods had a population consisting of more than 50% minorities in 2010?
   WRITE ANSWER HERE

2. Which neighborhoods then had a population of consisting more than 50% minorities in 2016?
   WRITE ANSWER HERE

3. Is it all the same neighborhoods for 2010 and 2016? If not, what reasons do you think contributed to this change?
   WRITE ANSWER HERE
"""




def percent_diff_POC():
    """
    output: returns a dictionary with Brooklyn neighborhoods as keys and values being the difference
    in people of color between 2010 and 2016.
    """


def find_diff(neighborhood):
    """
    input: neighborhood, a string that is a key in Mean_Rent
    output: a 2-tuple with the first entry being the percent increase in rent and the second entry being
    the percent difference in people of color
    """



def graph_POC_diff():
    """
    graphs the difference in percent of people of color of different zip codes in
    Brooklyn from 2010 to 2016
    """


"""
Which neighborhood experienced the largest decrease in the percentage of people of color?

For this neighborhood, what was the percentage increase of rent (HINT: Use find_diff())?
"""

"""
ANSWER REFLECTION QUESTIONS HERE
"""
print(percent_increase(percent_of_POC_2010,percent_of_POC_2016))
graph_percent_increase(percent_of_POC_2010,percent_of_POC_2016)
