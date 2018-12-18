# -*- coding: utf-8 -*-
from pyecharts import Bar, Pie

def main():
    generate_age()
    generate_race()
    generate_gender()
    generate_admission_type()
    generate_diagnosis_1()
    generate_discharge_disposition()

# [0-10): 160
# [10-20): 690
# [20-30): 1649
# [30-40): 3764
# [40-50): 9607
# [50-60): 17060
# [60-70): 22059
# [70-80): 25331
# [80-90): 16434
# [90-100): 2589
def generate_age():
    attr = ["[0-10)", "[10-20)", "[20-30)", "[30-40)", "[40-50)",
            "[50-60)", "[60-70)", "[70-80)", "[80-90)", "[90-100)"]
    val = [160, 690, 1649, 3764, 9607, 17060, 22059, 25331, 16434, 2589]
    bar = Bar("Age", title_pos = "center", width = 1500)
    bar.add(
        "", 
        attr, 
        val, 
        is_stack=True
    )
    bar.render("./html/age.html")

# AfricanAmerican: 18772
# Asian: 628
# Caucasian: 76454
# Hispanic: 2017
# Other: 1472
def generate_race():
    attr = ["AfricanAmerican", "Asian", "Caucasian", "Hispanic", "Other"]
    val = [18772, 628, 76454, 2017, 1472]
    pie = Pie("Race", title_pos = "center", width = 1500)
    pie.add(
        "", 
        attr, 
        val, 
        label_pos = "right",
        is_label_show = True,
        label_text_color = None,
        legend_orient="vertical",
        legend_pos = "left"
    )
    pie.render("./html/race.html")

# Female: 53454
# Male: 45886
# Unknown/Invalid: 3
def generate_gender():
    attr = ["Female", "Male", "Unknown/Invalid"]
    val = [53454, 45886, 3]
    pie = Pie("Gender", title_pos = "center", width = 1500)
    pie.add(
        "", 
        attr, 
        val, 
        label_pos = "right",
        is_label_show = True,
        label_text_color = None,
        legend_orient="vertical",
        legend_pos = "left"
    )
    pie.render("./html/gender.html")

# Emergency: 52371
# Urgent: 18132
# Elective: 18668
# Newborn: 10
# Not Available: 4617
# NULL: 5207
# Trauma Center: 18
# Not Mapped: 320
def generate_admission_type():
    attr = ["Emergency", "Urgent", "Elective", "Newborn", "Not Available", "NULL", "Trauma Center", "Not Mapped"]
    val = [52371, 18132, 18668, 10, 4617, 5207, 18, 320]
    bar = Bar("Admission Type", title_pos = "center", width = 1500)
    bar.add(
        "", 
        attr, 
        val,
        is_stack=True
    )
    bar.render("./html/admission_type.html")

# Circulatory 29730
# Respiratory 13976
# Digestive 9399
# Diabetes 8661
# Injury 6925
# Musculoskeletal 4935
# Genitourinary 5003
# Neoplasms 3133
# Other 17581
def generate_diagnosis_1():
    attr = ["Circulatory", "Respiratory", "Digestive", "Diabetes", "Injury", "Musculoskeletal", "Genitourinary", "Neoplasms", "Other"]
    val = [29730, 13976, 9399, 8661, 6925, 4935, 5003, 3133, 17581]
    bar = Bar("First Diagnosis", title_pos = "center", width = 1500)
    bar.add(
        "", 
        attr, 
        val,
        is_stack=True
    )
    bar.render("./html/diagnosis_1.html")

# 1(Discharged to home): 60234
# 2(Discharged/transferred to another short term hospital): 2128
# 3(Discharged/transferred to SNF): 13954
# 4(Discharged/transferred to ICF): 815
# 5(Discharged/transferred to another type of inpatient care institution): 1184
# 6(Discharged/transferred to home with home health service): 12902
# 7(Left AMA): 623
# 8(Discharged/transferred to home under care of Home IV provider): 108
# 9(Admitted as an inpatient to this hospital): 21
# 10(Neonate discharged to another hospital for neonatal aftercare): 6
# 12(Still patient or expected to return for outpatient services): 3
# 15(Discharged/transferred within this institution to Medicare approved swing bed): 63
# 16(Discharged/transferred/referred another institution for outpatient services): 11
# 17(Discharged/transferred/referred to this institution for outpatient services): 14
# 18(NULL): 3691
# 22(Discharged/transferred to another rehab fac including rehab units of a hospital .): 1993
# 23(Discharged/transferred to a long term care hospital.): 412
# 24(Discharged/transferred to a nursing facility certified under Medicaid but not certified under Medicare.): 48
# 25(Not Mapped): 989
# 27(Discharged/transferred to a federal health care facility.): 5
# 28(Discharged/transferred/referred to a psychiatric hospital of psychiatric distinct part unit of a hospital): 139
def generate_discharge_disposition():
    attr = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
            "10", "12", "15", "16", "17", "18", "22", "23",
            "24", "25", "27", "28"]
    val = [60234, 2128, 13954, 815, 1184, 12902, 623, 108, 21,
           6, 3, 63, 11, 14, 3691, 1993, 412,
           48, 989, 5, 139]
    bar = Bar("Discharge Disposition", title_pos = "center", width = 1500)
    bar.add(
        "", 
        attr, 
        val,
        is_stack=True
    )
    bar.render("./html/discharge_disposition.html")

if __name__ == '__main__':
    main()
