from sklearn import tree
from sklearn import ensemble
import csv
import numpy as np
import matplotlib.pyplot as plt
# cross validation
from sklearn import model_selection
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
from sklearn import metrics
from sklearn.feature_extraction import DictVectorizer

from collections import Counter

import pandas as pd 


MODEL = 'Decision Tree'
PARAMETER_NAME = ""
SCORING = 'logloss'  # either logloss or classification
K = 2 # The number of folds in K-Fold cross validation. Must be <= 4.
POSTPROCESS = True

ordering = ["TripType_3","TripType_4","TripType_5","TripType_6","TripType_7","TripType_8","TripType_9","TripType_12","TripType_14","TripType_15","TripType_18","TripType_19","TripType_20","TripType_21","TripType_22","TripType_23","TripType_24","TripType_25","TripType_26","TripType_27","TripType_28","TripType_29","TripType_30","TripType_31","TripType_32","TripType_33","TripType_34","TripType_35","TripType_36","TripType_37","TripType_38","TripType_39","TripType_40","TripType_41","TripType_42","TripType_43","TripType_44","TripType_999"]
ordering = [int(x.split('_')[1]) for x in ordering]

train = pd.read_csv('train.csv')
numTrain = train.shape[0]
test = pd.read_csv('test.csv')

allData = train.append(test)

dummiesAll = pd.get_dummies(allData, dummy_na=True)

# Don't really need these. Too much info
dummiesAll = dummiesAll.drop(['Upc', 'ScanCount', 'FinelineNumber'], axis=1)

# Split back into training and test sets
dummiesTrain = dummiesAll.iloc[:numTrain]
dummiesTest = dummiesAll.iloc[numTrain:]

# Get rid of the TripType category for the test
dummiesTest = dummiesTest.drop(['TripType'], axis=1)

# Group by VisitNumber. Note that TripType is the same across visit numbers
groupedTrain = dummiesTrain.groupby(['VisitNumber', 'TripType'])
groupedTest = dummiesTest.groupby(['VisitNumber'])

X_train = groupedTrain.sum()
X_test = groupedTest.sum()

Y_train = np.array([int(i[1]) for i in X_train.index.values])
train_VisitNumbers = [int(i[0]) for i in X_train.index.values]

test_VisitNumbers = X_test.index.values

truth_values = np.zeros(Y_train.shape[0])
for i, e in enumerate(Y_train):
    truth_values[i] = ordering.index(e)


print("Training...")

if MODEL == 'Naive Bayes':
    print("Naive Bayes...")
    PARAMETER_NAME = "Alpha"
    models = [0.1, 1, 10, 50, 100, 1000]
elif MODEL == 'Logistic Regression':
    print("Logistic Regression...")
    PARAMETER_NAME = "C"
    models = [0.1, 1, 10] # 0.1, 1, 10
elif MODEL == 'K Nearest Neighbors':
    print("K Nearest Neighbors...")
    PARAMETER_NAME = "K"
    models = [3, 5, 10]
elif MODEL == 'Decision Tree':
    PARAMETER_NAME = "Max Depth"
    models = [5, 10, 15, 20]
    print("Decision Tree...")
elif MODEL == "Random Forest":
    PARAMETER_NAME = "Number of Forests"
    models = [5, 10, 20]
    print("Random Forest...")
elif MODEL == "SVM":
    PARAMETER_NAME = "Alpha"
    print("SVM...")


losses = []
averageCV_losses = []
for n in models:

    if MODEL == 'Naive Bayes':
        print ("")
        print ("Naive Bayes, alpha = {}".format( n))
        clf = MultinomialNB(alpha = n) 
    elif MODEL == 'Logistic Regression':
        print("")
        print("LogisticRegression, C = {}".format(n))
        clf = linear_model.LogisticRegression(C=n)
    elif MODEL == 'K Nearest Neighbors':
        print("")
        print("K Nearest Neighbors, k = {}".format(n))
        clf = KNeighborsClassifier(n_neighbors=n)
    elif MODEL == 'Decision Tree':
        print("")
        print("Decision Tree, max_depth = {}".format(n))
        clf = tree.DecisionTreeClassifier(max_depth = n)
    elif MODEL == "Random Forest":
        print("")
        print("Random Forest, number of forests = {}".format(n))
        clf = RandomForestClassifier(n_estimators = n, criterion = 'gini', class_weight = None)
    elif MODEL == "SVM":
        print("")
        print("Linear SVM with multiclass support")
        clf = SVC(probability = True)


    if SCORING == 'logloss':
        scores = model_selection.cross_val_score(clf, X_train, Y_train, cv=K, scoring='log_loss', verbose = 1, n_jobs = 1)
        print('Scores = {}'.format(scores))
        averageCV = np.mean(scores) * -1
        print("Average CV score (Log Loss):{} ".format(averageCV))
    elif SCORING == 'classification':
        scores = model_selection.cross_val_score(clf, X_train, Y_train, cv=K, scoring='accuracy', verbose = 1, n_jobs = 1)
        print('Scores = {}'.format(scores))
        averageCV = np.mean(scores)
        print("Average CV score (classification): {}".format(averageCV))

    averageCV_losses.append(averageCV)

    # Fit the model on all the training data
    clf = clf.fit(X_train, Y_train)

    # Classification
    trainingPredictions = clf.predict(X_train)
    testPredictions = clf.predict(X_test)

    # Log Loss
    training_probabilities = clf.predict_proba(X_train)
    test_probabilities = clf.predict_proba(X_test)

    if SCORING == 'logloss':
        loss = metrics.log_loss(Y_train, training_probabilities)
        print("Training Log Loss:{} ".format(loss))
    elif SCORING == 'classification':
        loss = metrics.accuracy_score(Y_train, trainingPredictions)
        print("Training classification accuracy: {}".format(loss))

    losses.append(loss)


# Plot the Training Loss and the CV loss on the same plot
if SCORING == 'logloss':
    plt.plot(models, losses, '--', color = 'blue', label = 'Training Log Loss')
    plt.plot(models, averageCV_losses, '--', color = 'red', label = 'Validation Log Loss')
    parameter_string = PARAMETER_NAME
    plt.xlabel(parameter_string)
    plt.ylabel('Log Loss')
    title = 'Training vs Validation Log Loss for %s' % MODEL 
    plt.title(title)
    plt.legend(bbox_to_anchor=(0.6, -0.12, 0.5, -1.105), loc=3,ncol=2, mode="expand", borderaxespad=0.)
    plt.show()
elif SCORING == 'classification':
    plt.plot(models, losses, '--', color = 'blue', label = 'Training Accuracy')
    plt.plot(models, averageCV_losses, '--', color = 'red', label = 'Validation Accuracy')
    parameter_string = PARAMETER_NAME
    plt.xlabel(parameter_string)
    plt.ylabel('Accuracy')
    title = 'Training vs Validation Classification Accuracy for %s' % MODEL 
    plt.title(title)
    plt.legend(bbox_to_anchor=(0.6, -0.12, 0.5, -1.105), loc=3,ncol=2, mode="expand", borderaxespad=0.)
    plt.show()


if POSTPROCESS:
    test999_df = pd.read_csv('999users.csv')
    test999 = test999_df.ix[:,0]
    test999_list = test999.tolist()


f = open('walmartDTree.csv','w')
f.write('"VisitNumber","TripType_3","TripType_4","TripType_5","TripType_6","TripType_7","TripType_8","TripType_9","TripType_12","TripType_14","TripType_15","TripType_18","TripType_19","TripType_20","TripType_21","TripType_22","TripType_23","TripType_24","TripType_25","TripType_26","TripType_27","TripType_28","TripType_29","TripType_30","TripType_31","TripType_32","TripType_33","TripType_34","TripType_35","TripType_36","TripType_37","TripType_38","TripType_39","TripType_40","TripType_41","TripType_42","TripType_43","TripType_44","TripType_999"\n')
for (i, e) in enumerate(test_probabilities):
    visitNumber = test_VisitNumbers[i]

    a = ['{:.2f}'.format(x) for x in e] # format floats
    for i,e in enumerate(a):
        if e == '0.00':
            a[i] = '0'

    # If flag set, post process some 999 results
    if POSTPROCESS:
        if visitNumber in test999_list:
            a = ['0'] * 38
            a[37] = '1'

    a_join = ",".join(a) # join by commas
    f.write('%d,%s\n' % (visitNumber, a_join))
f.close()
