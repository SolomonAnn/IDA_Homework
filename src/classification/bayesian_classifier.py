# -*- coding: utf-8 -*-
import csv
import random
import numpy
import math
import time
import sys

def main(argv):
    filename = "tmp.csv"
    records = []
    ratio = float(argv[1])
    try:
        start = time.time()
        header = read_csv(filename, records)
        (trainset, testset) = split_dataset(records, ratio)
        seperation = seperate_trainset(trainset)
        counter = standardize_attributes(seperation)
        probabilities = calculate_probabilities(seperation, counter)
        predict_testset(testset, probabilities)
        end = time.time()
        print("Cost: {0} s".format(end - start))
        print("**********")
    except (IOError, TypeError, ValueError) as identifier:
        print(identifier)

# read the 'tmp.csv'
def read_csv(filename, records):
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            if row[15][0:3] == "250":
                records.append(row)
        print("**********")
        print("Data Loaded Successfully!")
        print("{0}: {1} rows".format(filename, len(records)))
        print("**********")
    return header

# split the dataset
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

# seperate the trainset according to 'readmitted'
def seperate_trainset(dataset):
    seperation = {}
    for record in dataset:
        if record[-1] not in seperation:
            seperation[record[-1]] = []
        seperation[record[-1]].append(record)
    print("Seperate the Train Set Successfully!")
    for key in seperation:
        print("{0}: {1} rows".format(key, len(seperation[key])))
    print("**********")
    return seperation  

# standardize values of attributes
def standardize_attributes(seperation):
    # standardize discrete attributes
    counter = {}
    for key in seperation:
        for index in set(range(2, 8)) | set(range(17, 44)):
            attr_map = {}
            for item in seperation[key]:
                if item[index] not in attr_map:
                    attr_map[item[index]] = 0
                attr_map[item[index]] += 1
            if key not in counter:
                counter[key] = []
            counter[key].append(attr_map)
    # standardize 'diag_1'
    for key in seperation:
        attr_map = {}
        for item in seperation[key]:
            if "390" <= item[15] <= "459" or item[15] == "785":
                if "circulatory" not in attr_map:
                    attr_map["circulatory"] = 0
                attr_map["circulatory"] += 1
            elif "460" <= item[15] <= "519" or item[15] == "786":
                if "respiratory" not in attr_map:
                    attr_map["respiratory"] = 0
                attr_map["respiratory"] += 1
            elif "520" <= item[15] <= "579" or item[15] == "787":
                if "digestive" not in attr_map:
                    attr_map["digestive"] = 0
                attr_map["digestive"] += 1
            elif item[15][0:3] == "250":
                if "diabetes" not in attr_map:
                    attr_map["diabetes"] = 0
                attr_map["diabetes"] += 1
            elif "800" <= item[15] <= "999":
                if "injury" not in attr_map:
                    attr_map["injury"] = 0
                attr_map["injury"] += 1
            elif "710" <= item[15] <= "739":
                if "musculoskeletal" not in attr_map:
                    attr_map["musculoskeletal"] = 0
                attr_map["musculoskeletal"] += 1
            elif "580" <= item[15] <= "629" or item[15] == "788":
                if "genitourinary" not in attr_map:
                    attr_map["genitourinary"] = 0
                attr_map["genitourinary"] += 1
            elif "140" <= item[15] <= "239":
                if "neoplasms" not in attr_map:
                    attr_map["neoplasms"] = 0
                attr_map["neoplasms"] += 1
            else:
                if "other" not in attr_map:
                    attr_map["other"] = 0
                attr_map["other"] += 1
        counter[key].append(attr_map)
    # standardize continuous attributes 
    for key in seperation:
        for index in set([16]) | set(range(8, 15)):
            attr_map = {}
            value_list = []
            for item in seperation[key]:
                value_list.append(int(item[index]))
            attr_map["mean"] = numpy.mean(value_list)
            attr_map["var"] = numpy.var(value_list)
            counter[key].append(attr_map)
    print("Standardize Attributes Successfully!")
    print("**********")
    return counter

# calculate probabilities in each case
def calculate_probabilities(seperation, counter):
    probabilities = {}
    for key in counter:
        length = len(seperation[key])
        for dictionary in counter[key]:
            attr_map = {}
            for item in dictionary:
                if "mean" in dictionary.keys() and "var" in dictionary.keys():
                    attr_map = dictionary
                    break;
                else:
                    attr_map[item] = float(dictionary[item]) / length
            if key not in probabilities:
                probabilities[key] = []
            probabilities[key].append(attr_map)
    print("Calculate Probabilities Successfully!")
    print("**********")
    return probabilities
                
# predict the test set
def predict_testset(testset, probabilities):
    actual_values = []
    predicted_values = []
    count = 0
    for record in testset:
        actual_values.append(record[-1])
    for record in testset:
        value_dict = {}
        # NO
        no_probability = calculate_prediction("NO", probabilities, record)
        value_dict[no_probability] = "NO"
        # <30
        lt_probability = calculate_prediction("<30", probabilities, record)
        value_dict[lt_probability] = "<30"
        # >30
        gt_probability = calculate_prediction(">30", probabilities, record)
        value_dict[gt_probability] = ">30"
        predicted_values.append(value_dict[max(no_probability, lt_probability, gt_probability)])
    for i in range(len(actual_values)):
        if actual_values[i] == predicted_values[i]:
            count += 1
    print("Accuracy: {0}".format(count / len(actual_values)))
    print("**********")

# calculate gaussian distribution
def calculate_gaussian_distribution(value, mean, var):
    return math.exp(0 - math.pow((value - mean) / math.sqrt(2) / var, 2)) \
            / math.sqrt(2 * math.pi) / var / var

# calculate prediction
def calculate_prediction(item, probabilities, record):
    probability = 1
    count = 0
    for i in set(range(2, 8)) | set(range(17, 44)):
        if record[i] not in probabilities[item][count]:
            probability *= 0
        else:
            probability *= probabilities[item][count][record[i]]
        count += 1
    if "390" <= record[15] <= "459" or record[15] == "785":
        if "circulatory" not in probabilities[item][count]:
            probability *= 0
        else:
            probability *= probabilities[item][count]["circulatory"]
    elif "460" <= record[15] <= "519" or record[15] == "786":
        if "respiratory" not in probabilities[item][count]:
            probability *= 0
        else:
            probability *= probabilities[item][count]["respiratory"]
    elif "520" <= record[15] <= "579" or record[15] == "787":   
        if "digestive" not in probabilities[item][count]:
            probability *= 0
        else:
            probability *= probabilities[item][count]["digestive"]
    elif record[15][0:3] == "250":
        if "diabetes" not in probabilities[item][count]:
            probability *= 0
        else:
            probability *= probabilities[item][count]["diabetes"]
    elif "800" <= record[15] <= "999":
        if "injury" not in probabilities[item][count]:
            probability *= 0
        else:
            probability *= probabilities[item][count]["injury"]
    elif "710" <= record[15] <= "739":
        if "musculoskeletal" not in probabilities[item][count]:
            probability *= 0
        else:
            probability *= probabilities[item][count]["musculoskeletal"]
    elif "580" <= record[15] <= "629" or record[15] == "788":
        if "genitourinary" not in probabilities[item][count]:
            probability *= 0
        else:
            probability *= probabilities[item][count]["genitourinary"]
    elif "140" <= record[15] <= "239":
        if "neoplasms" not in probabilities[item][count]:
            probability *= 0
        else:
            probability *= probabilities[item][count]["neoplasms"]
    else:
        if "other" not in probabilities[item][count]:
            probability *= 0
        else:
            probability *= probabilities[item][count]["other"]
    count += 1
    for i in set([16]) | set(range(8, 15)):
        probability *= calculate_gaussian_distribution(float(record[i]), probabilities[item][count]["mean"], probabilities[item][count]["var"])
        count += 1
    return probability

if __name__ == '__main__':
    main(sys.argv)
