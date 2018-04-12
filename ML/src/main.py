import os
from myInit import *
from myIO import *
from feature import *
from classifier import *
from evaluatiom import *

if __name__ == '__main__':
    ##data
    X_train, Y_train = read_csv(train_file_path)
    X_test, _ = read_csv(test_file_path)
    train_num = len(X_train)

    X_all1 = list(X_test.values())
    X_all = list(X_train.values())
    X_all.extend(X_all1)

    print('Read {} training samples'.format(len(X_train)))
    print('Read {} testing samples'.format(len(X_test)))

    ##feature
    feature, featureDicts = extract_feature(X_all, [{}, {}, {}])
    feature_train = feature[0:train_num]
    feature_test = feature[train_num:]
    label = list(Y_train.values())

    print('Extracted {} training samples'.format(len(feature_train)))
    print('Extracted {} testing samples'.format(len(feature_test)))

    labelDigit, labelDict = convert_label_digit(list(Y_train.values()))
    labelVec = convert_label_vector(labelDigit, labelDict)

    # X, y_digit, y_vector = concate_data(feature, labelDigit, labelVec)

    clf = get_clf()
    # score = k_fold_validate(clf, feature_train, labelDigit, labelVec, 5)
    # feature_test, testDicts = extract_feature(X_test, trainDicts)

    clf.fit(feature_train, labelDigit)
    prob_test = clf.predict_proba(feature_test)
    print('Write data into the file')
    write_csv(X_test.keys(), prob_test, labelDict)
    print('Finished')

