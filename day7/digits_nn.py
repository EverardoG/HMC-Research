# !conda update scikit-learn

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier

import numpy as np
import pandas as pd

print("+++ Start of digits example +++\n")
df = pd.read_csv('digits.csv',header = 0)
df.head()
df.info()

print("+++ Converting to numpy arrays... +++")
# Data needs to be in numpy arrays - these next two lines convert to numpy arrays
X_data_complete = df.iloc[:,0:64].values         # iloc == "integer locations" of rows/cols
y_data_complete = df[ '64' ].values       # individually addressable columns (by name)

X_unknown = X_data_complete[:22,:]
y_unknown = y_data_complete[:22]
actual_digits = [0,0,0,1,7,2,3,4,0,1,9,9,5,5,6,5,0,9,8,9,8,4]

X_known = X_data_complete[22:,:]
y_known = y_data_complete[22:]

KNOWN_SIZE = len(y_known)
indices = np.random.permutation(KNOWN_SIZE)  # this scrambles the data each time
X_known = X_known[indices]
y_known = y_known[indices]

#
# from the known data, create training and testing datasets
#
TRAIN_FRACTION = 0.85
TRAIN_SIZE = int(TRAIN_FRACTION*KNOWN_SIZE)
TEST_SIZE = KNOWN_SIZE - TRAIN_SIZE   # not really needed, but...
X_train = X_known[:TRAIN_SIZE]
y_train = y_known[:TRAIN_SIZE]

X_test = X_known[TRAIN_SIZE:]
y_test = y_known[TRAIN_SIZE:]

#
# it's important to keep the input values in the 0-to-1 or -1-to-1 range
#    This is done through the "StandardScaler" in scikit-learn
#
USE_SCALER = True
if USE_SCALER == True:
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X_train)   # Fit only to the training dataframe
    # now, rescale inputs -- both testing and training
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    X_unknown = scaler.transform(X_unknown)

# scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
#
# mlp = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=400, alpha=1e-4,
#                     solver='sgd', verbose=10, tol=1e-4, random_state=1)
mlp = MLPClassifier(hidden_layer_sizes=(100,100), max_iter=200, alpha=1e-4,
                    solver='sgd', verbose=True, shuffle=True, early_stopping = False, # tol=1e-4,
                    random_state=None, # reproduceability
                    learning_rate_init=.03, learning_rate = 'adaptive')

print("\n\n++++++++++  TRAINING  +++++++++++++++\n\n")
mlp.fit(X_train, y_train)


print("\n\n++++++++++++  TESTING  +++++++++++++\n\n")
print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))

# let's see the coefficients -- the nnet weights!
# CS = [coef.shape for coef in mlp.coefs_]
# print(CS)

# predictions:
predictions = mlp.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print("\nConfusion matrix:")
print(confusion_matrix(y_test,predictions))

print("\nClassification report")
print(classification_report(y_test,predictions))

# unknown data rows...
#
unknown_predictions = list(mlp.predict(X_unknown))
print("Unknown predictions:")
print("  Correct values:  ", actual_digits)
print("  Our predictions: ", unknown_predictions)

i = 0
total_right = 0
for digit in actual_digits:
    if actual_digits[i] == unknown_predictions[i]:
        total_right += 1
    i += 1
avg_right = total_right/len(actual_digits)
print("\nScore on Unkown: ",avg_right*100, "%")

if False:
    L = [5.2, 4.1, 1.5, 0.1]
    row = np.array(L)  # makes an array-row
    row = row.reshape(1,4)   # makes an array of array-row
    if USE_SCALER == True:
        row = scaler.transform(row)
    print("\nrow is", row)
    print("mlp.predict_proba(row) == ", mlp.predict_proba(row))
