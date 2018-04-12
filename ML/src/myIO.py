import os
import sys
import csv
from itertools import islice
from myInit import *

def write_csv(number, results, labelDict):
    with open('../data/result.csv', 'w') as f:
        writer = csv.writer(f)
        for num, prob in zip(number, results):
            row = [int(num)]
            for i in range(3, 45):
                if str(i) in labelDict:
                    row.append("%.2f" % (prob[labelDict[str(i)]] + 1.0/len(labelDict)))
            row.append("%.2f" % (prob[labelDict[str(999)]] + 1.0/len(labelDict)))
            writer.writerow(row)

def read_csv(file_path):
    X = {}
    Y = {}

    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')

        next(reader) #ignore header

        for row in reader:
            if len(row) == 6 or len(row) == 7:
                if len(row) == 7: #train
                    #Y
                    visitNumber = row[1]
                    Y[visitNumber] = row[0]
                    row = row[1:]

                visitNumber = row[0]

                #X
                if visitNumber not in X:
                    X[visitNumber] = [row[1:]]
                else:
                    X[visitNumber].append(row[1:])
            else:
                print('Invalid input file')
                sys.exit(0)

    return X, Y