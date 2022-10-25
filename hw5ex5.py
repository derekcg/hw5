import argparse
import csv

# interpret user options to determine which file to read
parser = argparse.ArgumentParser(description='Find Most Popular Favorites')
parser.add_argument('-i', '--infile', help='input file with student favorite things in multiple catagories', default='binary_patient_data.csv')
args = parser.parse_args()

with open(args.infile, 'r') as f:  # read file. parse as a list (each element is a row) of dictionaries (each key is a column)
    patient_data = []
    for row in csv.DictReader(f):
        patient_data.append(row)

male_old_pos = 0
male_old_neg = 0
male_young_pos = 0
male_young_neg = 0
female_old_pos = 0
female_old_neg = 0
female_young_pos = 0
female_young_neg = 0
for patient in patient_data:
    patient['age'] = int(patient['age'])
    if patient['gender']=='M':
        if patient['age'] >= 65 and patient['test']=='P':
            male_old_pos = male_old_pos + 1
        if patient['age'] >= 65 and patient['test']=='N':
            male_old_neg = male_old_neg + 1
        if patient['age'] < 65 and patient['test']=='P':
            male_young_pos = male_old_pos + 1
        if patient['age'] < 65 and patient['test']=='N':
            male_young_neg = male_young_neg + 1
    else:
        if patient['age'] >= 65 and patient['test']=='P':
            female_old_pos = female_old_pos + 1
        if patient['age'] >= 65 and patient['test']=='N':
            female_old_neg = male_old_neg + 1
        if patient['age'] < 65 and patient['test']=='N':
            female_young_pos = female_old_pos + 1
        if patient['age'] < 65 and patient['test']=='N':
            female_young_neg = female_young_neg + 1
print(female_old_neg)
print(female_young_pos)
male_or = (male_old_pos*male_young_neg)/(male_old_neg*male_young_pos)
female_or = (female_old_pos*female_young_neg)/(female_old_neg*female_young_pos)

print('Association between old age (65 or older) and positive test result, among males: OR = ', male_or)
print('Association between old age (65 or older) and positive test result, among females: OR = ', female_or)