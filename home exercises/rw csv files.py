# Q1
import csv

with open("colours_20_simple.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)
