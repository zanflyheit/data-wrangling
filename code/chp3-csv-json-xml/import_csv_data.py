import csv

with open('data-wrangling\data\chp3\data-text.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
