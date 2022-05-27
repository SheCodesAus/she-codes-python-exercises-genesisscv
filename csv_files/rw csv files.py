# Q1

# import csv

# with open("csv_files\colours_20_simple.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print()  # print line

# colours = []

# with open("csv_files\colours_20_simple.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours.append(line)
#         print()  # print colours

# for colour in colours:
#     print(colour[0], colour[1], colour[2])

# Q2

# colours = []

# with open("csv_files\colours_20_simple.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours.append(line)

# colours.pop(-0)  # removing header

# for colour in colours:
#     print(f"{colour[2]}, Hex: {colour[1]}, RGB: {colour[0]}")

# Q3 (I think there's a typo on the question?)

# # Q4
# import csv

# with open("csv_files\colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print()  # print row

# colours2 = []
# red_counter = 0
# green_counter = 0
# blue_counter = 0
# yellow_counter = 0

# with open("csv_files\colours_20.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours2.append(line)
#     print()  # print colours2

# for colour in colours2:
#     red = colour[4].find("red")
#     green = colour[4].find("green")
#     blue = colour[4].find("blue")
#     yellow = colour[4].find("yellow")

#     if red >= 0:
#         red_counter += 1
#     if green >= 0:
#         green_counter += 1
#     if blue >= 0:
#         blue_counter += 1
#     if yellow >= 0:
#         yellow_counter += 1
# print(f"Red: {red_counter} \nGreen:{green_counter} \nBlue:{blue_counter} \nYellow:{yellow_counter}")

# Opening a different file

# import csv

# with open("csv_files\colours_213.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print()  # print row

# colours3 = []
# red_counter = 0
# green_counter = 0
# blue_counter = 0
# yellow_counter = 0

# with open("csv_files\colours_213.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours3.append(line)
#     print()  # print colours2

# for colour in colours3:
#     red = colour[4].find("red")
#     green = colour[4].find("green")
#     blue = colour[4].find("blue")
#     yellow = colour[4].find("yellow")

#     if red >= 0:
#         red_counter += 1
#     if green >= 0:
#         green_counter += 1
#     if blue >= 0:
#         blue_counter += 1
#     if yellow >= 0:
#         yellow_counter += 1
# print(f"Red: {red_counter} \nGreen:{green_counter} \nBlue:{blue_counter} \nYellow:{yellow_counter}")


# Q5
import csv
with open("csv_files\galaxies.csv") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print()  # print row

velocities = []

with open("csv_files\galaxies.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        velocities.append(row)
    print()  # velocities

minimum = velocities[0]
for number in velocities:
    if minimum > number:
        minimum = number
print(minimum)
