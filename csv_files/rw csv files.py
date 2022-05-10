import csv

with open("2016_pilbara.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)

colours = []

with open("2016_pilbara.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

print(colours)
print()

for age_group in colours:
    print(f"{age_group[0]} {age_group[1]}")

# writing to csv file
with open("colours.csv", mode="w", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file, delimeter=",")

    for age_group in colours:
        csv_writer.writerow([age_group[1], age_group[0]])
