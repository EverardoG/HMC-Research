#
# digits5: modeling the digits data with DTs and RFs
#


import numpy as np
import pandas as pd

from sklearn import tree      # for decision trees
from sklearn import ensemble  # for random forests

try: # different imports for different versions of scikit-learn
    from sklearn.model_selection import cross_val_score   # simpler cv this week
except ImportError:
    try:
        from sklearn.cross_validation import cross_val_score
    except:
        print("No cross_val_score!")

#
# The "answers" to the 20 unknown digits, labeled -1:
#
all_answers = [9,9,5,5,6,5,0,9,8,9,8,4,0,1,2,3,4,5,6,7]
answers = all_answers[0:9]


print("+++ Start of pandas' datahandling +++\n")
# df here is a "dataframe":
df = pd.read_csv('digits5.csv', header=0)    # read the file w/header row #0
print(df.head())
print(df.info())
# remove_rows = np.linspace(0,19,20)
# df = df_og.drop(remove_rows)
# print(df.head())
# print(df.head())                            # first five lines
# df.info()                                 # column details
print("\n+++ End of pandas +++\n")


print("+++ Start of numpy/scikit-learn +++\n")
# Data needs to be in numpy arrays - these next two lines convert to numpy arrays
X_all = df.iloc[:,0:64].values        # iloc == "integer locations" of rows/cols
y_all = df[ '64' ].values      # individually addressable columns (by name)

X_data_full = X_all[0:,:]  #
y_data_full = y_all[0:]    #

#This is all of the code for a decision tree classifier
scores_avgs = []
max_depths = []
for max_depth in range(1,30):
    # create our classifier
    dtree = tree.DecisionTreeClassifier(max_depth=max_depth)
    #
    # cross-validate to tune our model (this week, all-at-once)
    #
    scores = cross_val_score(dtree, X_data_full, y_data_full, cv=15) #This function separates training and testing data on its own
    average_cv_score = scores.mean()
    scores_avgs.append(average_cv_score)
    max_depths.append(max_depth)
    # print("For depth=", max_depth, "average CV score = ", average_cv_score)

import matplotlib.pyplot as plt
plt.xkcd()
plt.plot(max_depths,scores_avgs)
plt.xkcd()
plt.xlabel('Max Depth')
plt.xkcd()
plt.ylabel('Average Score')

plt.show()
import matplotlib.pyplot as plt
plt.xkcd()
plt.plot(max_depths,scores_avgs)
plt.xkcd()
plt.xlabel('Max Depth')
plt.xkcd()
plt.ylabel('Average Score')

plt.show()
# plt.savefig('neat_graph.png')

try:
    best_depth_ind = scores_avgs.index(max(scores_avgs))[0]
except:
    best_depth_ind = scores_avgs.index(max(scores_avgs))
best_depth = max_depths[best_depth_ind]

MAX_DEPTH = best_depth  # choose a MAX_DEPTH based on cross-validation...
print("\nChoosing MAX_DEPTH =", MAX_DEPTH, " at ",max(scores_avgs)*100,'% accuracy')

#Splitting up Training and Testing Data
X_unknown = X_all[0:9,0:63]              # the final testing data
X_train = X_all[9:,0:63]              # the training data

y_unknown = y_all[0:9]                  # the final testing outputs/labels (unknown)
y_train = y_all[9:]                  # the training outputs/labels (known)

# our decision-tree classifier...
dtree = tree.DecisionTreeClassifier(max_depth=MAX_DEPTH)
dtree = dtree.fit(X_train, y_train)

#Here we can see how accurate it is
print("Decision-tree predictions:\n")
predicted_labels = dtree.predict(X_unknown)
answer_labels = answers
#
# formatted printing! (docs.python.org/3/library/string.html#formatstrings)
#
s = "{0:<11} | {1:<11}".format("Predicted","Answer")
#  arg0: left-aligned, 11 spaces, string, arg1: ditto
print(s)
s = "{0:<11} | {1:<11}".format("-------","-------")
print(s)
# the table...
for p, a in zip( predicted_labels, answer_labels ):
    s = "{0:<11} | {1:<11}".format(p,a)
    print(s)

feature_names = []
target_names = []
for i in np.linspace(1,63,63):
    feature_names.append(str(i))
for i in range(10):
    target_names.append(str(i))

#This is the script saving the best decision tree as a dot file
filename = 'tree_for_digits5_depth' + str(max_depth) + '.dot'
tree.export_graphviz(dtree, out_file=filename,   # the filename constructed above...!
                        feature_names=feature_names,  filled=True,
                        rotate=False, # LR vs UD
                        class_names=target_names,
                        leaves_parallel=True )  # lots of options!
#
# now, model from iris5.py to try DTs and RFs on the digits dataset!
#
