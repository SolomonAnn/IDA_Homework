# -*- coding: utf-8 -*-
import csv

def main():
    records = []
    header = read_csv(records)
    result = handle(records)
    write_csv(header, result)

# read the 'diabetic_data.csv'
def read_csv(records):
    with open("diabetic_data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        # records.append(header)
        for row in csv_reader:
            records.append(row)
        # diag_3
        header.pop(20)
        # diag_2
        header.pop(19)
        # medical_specialty
        header.pop(11)
        # payer_code
        header.pop(10)
        # weight
        header.pop(5)
        return header

# write the 'tmp.csv' after preprocessing
def write_csv(header, records):
    with open("tmp.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, lineterminator = "\n")
        csv_writer.writerow(header)
        csv_writer.writerows(records)

def handle(records):
    result = []
    for record in records:
        # delete 'Expired/Hospice' records
        if record[7] not in ["11", "13", "14", "19", "20", "21"]:
            result.append(record)
    for item in result:
        # fill the gap in 'race'
        if item[2] == "?":
            item[2] = "Caucasian"
        # remove 'diag_2' and 'diag_3'
        item.pop(20)
        item.pop(19)
        # remove 'medical_specialty'
        item.pop(11)
        # remove 'payer_code'
        item.pop(10)
        # remove 'weight'
        item.pop(5)
    return result

if __name__ == '__main__':
    main()
