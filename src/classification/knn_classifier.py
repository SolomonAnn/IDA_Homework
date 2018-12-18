# -*- coding: utf-8 -*-
import csv
import random
import numpy as np
import math
import sys
import time

def main(argv):
    filename = "tmp.csv"
    dataset = []
    ratio = float(argv[1])
    k = float(argv[2])

    try:
        start = time.time()
        header = read_csv(filename, dataset)
        (trainset, testset) = split_dataset(dataset, ratio)
        max_min = calculate_max_and_min(trainset)
        knn(max_min, testset, trainset, k)
        end = time.time()
        print("Cost: {0} min {1} s".format((end - start) / 60, (end - start) % 60))
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

# split the data set
def split_dataset(dataset, ratio):
    trainset_capacity = int(len(dataset) * ratio)
    trainset = []
    testset = list(dataset)
    count = 0

    while count < trainset_capacity:
        index = random.randrange(0, len(testset))
        trainset.append(testset.pop(index))
        count += 1

    print("Split the Dataset Successfully!")
    print("Train Set: {0} rows".format(len(trainset)))
    print("Test Set: {0} rows".format(len(testset)))
    print("**********")
    return (trainset, testset)

# calculate max and min
def calculate_max_and_min(dataset):
    max_min = {}
    copyset = []
    index = set([16]) | set(range(8, 15))

    for item in dataset:
        record = []
        for i in index:
            record.append(float(item[i]))
        copyset.append(record)

    max_list = np.amax(copyset, axis=0)
    min_list = np.amin(copyset, axis=0)
    for i in range(len(max_list)):
        max_min[index.pop()] = max_list[i] - min_list[i]
    return max_min

# calculate the distance between two vectors
def calculate_distance(max_min, vector_1, vector_2):
    num = 0
    index = set([16]) | set(range(8, 15))

    for i in range(len(vector_1)):
        if i in {0, 1, 44}:
            continue;
        elif i == 15:
            if "390" <= vector_1[i] <= "459" or vector_1[i] == "785":
                if "390" <= vector_2[i] <= "459" or vector_2[i] == "785":
                    num += 1
            elif "460" <= vector_1[i] <= "519" or vector_1[i] == "786":
                if "460" <= vector_2[i] <= "519" or vector_2[i] == "786":
                    num += 1
            elif "520" <= vector_1[i] <= "579" or vector_1[i] == "787":
                if "520" <= vector_2[i] <= "579" or vector_2[i] == "787":
                    num += 1
            elif vector_1[i][0:3] == "250":
                if vector_2[i][0:3] == "250":
                    num += 1
            elif "800" <= vector_1[i] <= "999":
                if "800" <= vector_2[i] <= "999":
                    num += 1
            elif "710" <= vector_1[i] <= "739":
                if "710" <= vector_2[i] <= "739":
                    num += 1
            elif "580" <= vector_1[i] <= "629" or vector_1[i] == "788":
                if "580" <= vector_2[i] <= "629" or vector_2[i] == "788":
                    num += 1
            elif "140" <= vector_1[i] <= "239":
                if "140" <= vector_2[i] <= "239":
                    num += 1
            else:
                if "390" <= vector_2[i] <= "579" \
                    or vector_2[i] in {"785", "786", "787", "788"} \
                    or vector_2[i][0:3] == "250" \
                    or "800" <= vector_2[i] <= "999" \
                    or "710" <= vector_2[i] <= "739" \
                    or "580" <= vector_2[i] <= "629" \
                    or "140" <= vector_2[i] <= "239":
                    continue;
                else:
                    num += 1
        elif i in index:
            num += math.pow((float(vector_1[i]) - float(vector_2[i])) / max_min[i], 2)
        else:
            if vector_1[i] == vector_2[i]:
                continue;
            else:
                num += 1
    return math.sqrt(num)

# knn
def knn(max_min, testset, trainset, k):
    count = 0
    n = 0
    for vector_test in testset:
        n += 1
        print("{0}".format(n))
        distance = 0
        choices = {}
        distance_limit = sys.maxsize
        for vector_train in trainset:
            distance = calculate_distance(max_min, vector_test, vector_train)
            if len(choices) == 0:
                distance_limit = distance
                choices[distance] = vector_train
            elif len(choices) < k:
                distance_limit = np.max([distance_limit, distance])
                choices[distance] = vector_train
            elif len(choices) == k:
                if distance < distance_limit:
                    choices.pop(distance_limit)
                    distance_limit = distance
                    choices[distance_limit] = vector_train
            else:
                print("Failed!")
        no_count = 0
        gt_count = 0
        lt_count = 0
        for item in choices:
            if choices[item][-1] == "NO":
                no_count += 1
            elif choices[item][-1] == ">30":
                gt_count += 1
            else:
                lt_count += 1
        if no_count > gt_count:
            if no_count > lt_count:
                if vector_test[-1] == "NO":
                    count += 1
            else:
                if vector_test[-1] == "<30":
                    count += 1    
        else:
            if gt_count > lt_count:
                if vector_test[-1] == ">30":
                    count += 1
            else:
                if vector_test[-1] == "<30":
                    count += 1
        
    print("Accuracy: {0}".format(count / len(testset)))
    print("**********")
    return 

if __name__ == '__main__':
    main(sys.argv)
