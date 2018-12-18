# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression as LR
import time
import csv

def main():
    filename = "tmp.csv"
    dataset = []

    try:
        start = time.time()
        header = read_csv(filename, dataset)
        write_csv(header, dataset)
        logistic_regression()
        end = time.time()
        print("Cost: {0} s".format(end - start))
        print("**********")
    except (IOError, TypeError, ValueError) as identifier:
        print(identifier)

# read the 'tmp.csv'
def read_csv(filename, dataset):
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            if row[15][0:3] == "250":
                dataset.append(row)

        print("**********")
        print("Data Loaded Successfully!")
        print("{0}: {1} rows".format(filename, len(dataset)))
        print("**********")
    return header

# write the 'regression.csv'
def write_csv(header, records):
    with open("regression.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, lineterminator = "\n")
        csv_writer.writerow(header)
        csv_writer.writerows(records)

def logistic_regression():
    filename = 'regression.csv'
    dataset = pd.read_csv(filename)
    x = dataset.iloc[:,2:44].values
    y = dataset.iloc[:,44].values

    for i in set(range(0, 6)) | set(range(15, 42)):
        value = 0
        value_dict = {}
        for item in x:
            if item[i] not in value_dict.keys():
                value_dict[item[i]] = value
                value += 1
            item[i] = value_dict[item[i]]
            
    for item in x:
        for i in range(len(item)):
            if item[i] == "unknown":
                print("1")
    
    for i in range(len(y)):
        if y[i] == "NO":
            y[i] = 1
        else:
            y[i] = 0

    lr = LR()
    lr.fit(x, y.astype("int"))
    print("Accuracy: {0}".format(lr.score(x, y.astype("int"))))
    print("**********")

if __name__ == '__main__':
    main()
