# !conda update scikit-learn

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier

import numpy as np
import pandas as pd

print("+++ Start of digits example +++\n")
df = pd.read_csv('digits.csv',header = 0)
# df.head()
# df.info()

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

avg_train_scores = []
avg_test_scores = []
avg_pred_scores = []
n_range = []
n_max = 300

for n in range(200,n_max+5,5):
    print("\n+++ Running Simulation Number "+str(n+1)+" +++\n")
    mlp = MLPClassifier(hidden_layer_sizes=(100,n+1), max_iter=200, alpha=1e-4,
                    solver='sgd', verbose=False, shuffle=True, early_stopping = False, # tol=1e-4,
                    random_state=None, # reproduceability
                    learning_rate_init=.03, learning_rate = 'adaptive')
    sim_train_scores = []
    sim_test_scores = []
    sim_pred_scores = []
    for m in range(10):
        mlp.fit(X_train, y_train)
        sim_train_scores.append( mlp.score(X_train, y_train) )
        sim_test_scores.append( mlp.score(X_test,y_test) )
        unknown_predictions = list(mlp.predict(X_unknown))
        i = 0
        total_right = 0
        for digit in actual_digits:
            if actual_digits[i] == unknown_predictions[i]:
                total_right += 1
            i += 1
        sim_pred_scores.append( total_right/len(actual_digits) )

    avg_train_scores.append( sum(sim_train_scores)/len(sim_train_scores) )
    avg_test_scores.append( sum(sim_test_scores)/len(sim_test_scores) )
    avg_pred_scores.append( sum(sim_pred_scores)/len(sim_pred_scores) )
    n_range.append(n+1)

plt.xkcd()
plt.plot(n_range,avg_pred_scores)
plt.xlabel('Number of neurons in Second Layer,\n100 in first')
plt.xkcd()
plt.ylabel('Accuracy on Unknown Numbers')
plt.xkcd()
plt.title('For 2 Hidden Layers')
plt.xlim((1,n_max))
plt.ylim((0,1))
plt.show()

plt.xkcd()
plt.plot(n_range,avg_pred_scores)
plt.xlabel('Number of neurons in Second Layer,\n100 in first')
plt.xkcd()
plt.ylabel('Accuracy on Unknown Numbers')
plt.xkcd()
plt.title('For 2 Hidden Layers')
plt.xlim((1,n_max))
plt.ylim((0,1))
plt.show()

# avg_train_scores = []
# avg_test_scores = []
# avg_pred_scores = []
# n_range = []
# n_max = 20
#
# for n in range(n_max):
#     print("\n+++ Running Simulation Number "+str(n+1+n_max)+" +++\n")
#     mlp = MLPClassifier(hidden_layer_sizes=(n+1,n+1), max_iter=200, alpha=1e-4,
#                     solver='sgd', verbose=False, shuffle=True, early_stopping = False, # tol=1e-4,
#                     random_state=None, # reproduceability
#                     learning_rate_init=.03, learning_rate = 'adaptive')
#     sim_train_scores = []
#     sim_test_scores = []
#     sim_pred_scores = []
#     for m in range(10):
#         mlp.fit(X_train, y_train)
#         sim_train_scores.append( mlp.score(X_train, y_train) )
#         sim_test_scores.append( mlp.score(X_test,y_test) )
#         unknown_predictions = list(mlp.predict(X_unknown))
#         i = 0
#         total_right = 0
#         for digit in actual_digits:
#             if actual_digits[i] == unknown_predictions[i]:
#                 total_right += 1
#             i += 1
#         sim_pred_scores.append( total_right/len(actual_digits) )
#
#     avg_train_scores.append( sum(sim_train_scores)/len(sim_train_scores) )
#     avg_test_scores.append( sum(sim_test_scores)/len(sim_test_scores) )
#     avg_pred_scores.append( sum(sim_pred_scores)/len(sim_pred_scores) )
#     n_range.append(n+1)
#
# plt.xkcd()
# plt.plot(n_range,avg_pred_scores)
# plt.xlabel('Number of neurons per layer')
# plt.xkcd()
# plt.ylabel('Accuracy on Unknown Numbers')
# plt.xkcd()
# plt.title('For 2 Hidden Layers')
# plt.xlim((1,n_max))
# plt.ylim((0,1))
# plt.show()
#
# plt.xkcd()
# plt.plot(n_range,avg_pred_scores)
# plt.xlabel('Number of neurons per layer')
# plt.xkcd()
# plt.ylabel('Accuracy on Unknown Numbers')
# plt.xkcd()
# plt.title('For 2 Hidden Layers')
# plt.xlim((1,n_max))
# plt.ylim((0,1))
# plt.show()
