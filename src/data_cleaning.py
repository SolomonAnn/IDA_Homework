# -*- coding: utf-8 -*-
import csv

def main():
    records = []
    header = read_csv(records)
    # count_gender(records)
    # count_weight(records)
    handle_race(records)
    handle_weight(records)
    write_csv(header, records)

def read_csv(records):
    with open("diabetic_data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        # records.append(header)
        for row in csv_reader:
            records.append(row)
        return header

def write_csv(header, records):
    with open("tmp.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, lineterminator = "\n")
        csv_writer.writerow(header)
        csv_writer.writerows(records)

def count_race(records):
    count_Total = 0
    count_AfricanAmerican = 0
    count_Asian = 0
    count_Caucasian = 0
    count_Hispanic = 0
    count_Other = 0
    for record in records:
        count_Total += 1
        if record[2] == "AfricanAmerican":
            count_AfricanAmerican += 1
        elif record[2] == "Asian":
            count_Asian += 1
        elif record[2] == "Caucasian":
            count_Caucasian += 1
        elif record[2] == "Hispanic":
            count_Hispanic += 1
        elif record[2] == "Other":
            count_Other += 1
    print ("AfricanAmerican:" + str(count_AfricanAmerican))
    print ("Asian:" + str(count_Asian))
    print ("Caucasian:" + str(count_Caucasian))
    print ("Hispanic:" + str(count_Hispanic))
    print ("Other:" + str(count_Other))
    print ("Total:" + str(count_Total))

def count_gender(records):
    count_Total = 0
    count_Female = 0
    count_Male = 0
    count_Unknown_or_Invalid = 0
    for record in records:
        count_Total += 1
        if record[3] == "Female":
            count_Female += 1
        elif record[3] == "Male":
            count_Male += 1
        else:
            count_Unknown_or_Invalid += 1
    print ("Female:" + str(count_Female))
    print ("Male:" + str(count_Male))
    print ("Unknown/Invalid:" + str(count_Unknown_or_Invalid))
    print ("Total:" + str(count_Total))

def count_weight(records):
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

def handle_race(records):
    for record in records:
        if record[2] == "?":
            record[2] = "Caucasian"

def handle_weight(records):
    for record in records:
        if record[5] == "?":
            if record[3] == "Unknown/Invalid":
                record[5] = "[75-100)"
            elif record[3] == "Male":
                if record[4] == "[0-10)":
                    record[5] = "[0-25)"
                elif record[4] == "[10-20)" or record[4] == "[90-100)":
                    record[5] = "[50-75)"
                else:
                    record[5] = "[75-100)"
            else:
                if record[4] == "[0-10)":
                    record[5] = "[25-50)"
                elif record[4] == "[10-20)" or record[4] == "[80-90)" or record[4] == "[90-100)":
                    record[5] = "[50-75)"
                else:
                    record[5] = "[75-100)"

if __name__ == '__main__':
    main()