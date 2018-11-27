# -*- coding: utf-8 -*-
import csv
from operator import itemgetter
from itertools import groupby

def main():
    records = []
    read_csv(records)
    count_age(records)
    count_race(records)
    count_gender(records)
    # count_weight(records)
    count_admission_type(records)
    count_diagnosis(records)
    count_discharge_disposition(records)

# Read the 'tmp.csv'.
def read_csv(records):
    with open("tmp.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            records.append(row)

# age
def count_age(records):
    print ("age")
    records.sort(key = itemgetter(4))
    groups = groupby(records, itemgetter(4))
    for key, group in groups:
        print (key, len(list(group)))
    print ("------")

# race
def count_race(records):
    print ("race")
    records.sort(key = itemgetter(2))
    groups = groupby(records, itemgetter(2))
    for key, group in groups:
        print (key, len(list(group)))
    print ("------")

# gender
def count_gender(records):
    print ("gender")
    records.sort(key = itemgetter(3))
    groups = groupby(records, itemgetter(3))
    for key, group in groups:
        print (key, len(list(group)))
    print ("------")

# weight(based on different races and ages)
def count_weight(records):
    print ("weight(based on different races and ages)")
    gender_list = ["Male", "Female"]
    age_list = ["[0-10)", "[10-20)", "[20-30)", "[30-40)", "[40-50)",
                "[50-60)", "[60-70)", "[70-80)", "[80-90)", "[90-100)"]
    weight_list = ["[0-25)", "[25-50)", "[50-75)", "[75-100)", "[100-125)",
                   "[125-150)", "[150-175)", "[175-200)", ">200"]
    for gender in gender_list:
        for age in age_list:
            for weight in weight_list:
                tmp_list = list(filter(lambda x:(x[3] == gender and x[4] == age and x[5] == weight), records))
                print (gender + " " + age + " " + weight + ":")
                print (len(tmp_list))
    print ("------")

# admission type
def count_admission_type(records):
    print ("admission type")
    dictionary = {"1": "Emergency", "2": "Urgent",
                  "3": "Elective", "4": "Newborn",
                  "5": "Not Available", "6": "NULL",
                  "7": "Trauma Center", "8": "Not Mapped"}
    records.sort(key = itemgetter(5))
    groups = groupby(records, itemgetter(5))
    for key, group in groups:
        print (dictionary[key], len(list(group)))
    print ("------")

# diagnosis 1
def count_diagnosis(records):
    print ("diagnosis 1")
    circulatory_num = 0
    respiratory_num = 0
    digestive_num = 0
    diabetes_num = 0
    injury_num = 0
    musculoskeletal_num = 0
    genitourinary_num = 0
    neoplasms_num = 0
    other_num = 0
    records.sort(key = itemgetter(17))
    groups = groupby(records, itemgetter(17))
    for key, group in groups:
        if "390" <= key <= "459" or key == "785":
            circulatory_num += len(list(group))
        elif "460" <= key <= "519" or key == "786":
            respiratory_num += len(list(group))
        elif "520" <= key <= "579" or key == "787":
            digestive_num += len(list(group))
        # elif "250" <= key < "251":
        elif key[0:3] == "250":
            diabetes_num += len(list(group))
        elif "800" <= key <= "999":
            injury_num += len(list(group))
        elif "710" <= key <= "739":
            musculoskeletal_num += len(list(group))
        elif "580" <= key <= "629" or key == "788":
            genitourinary_num += len(list(group))
        elif "140" <= key <= "239":
            neoplasms_num += len(list(group))
        else:
            other_num += len(list(group)) 
    print ("Circulatory", circulatory_num)
    print ("Respiratory", respiratory_num)
    print ("Digestive", digestive_num)
    print ("Diabetes", diabetes_num)
    print ("Injury", injury_num)
    print ("Musculoskeletal", musculoskeletal_num)
    print ("Genitourinary", genitourinary_num)
    print ("Neoplasms", neoplasms_num)
    print ("Other", other_num)
    print ("------")

# discharge disposition
def count_discharge_disposition(records):
    print ("discharge disposition")
    records.sort(key = itemgetter(6))
    groups = groupby(records, itemgetter(6))
    for key, group in groups:
        print (key, len(list(group)))
    print ("------")

if __name__ == '__main__':
    main()
