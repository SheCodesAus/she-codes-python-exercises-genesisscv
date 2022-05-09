import csv

with open("dogs.txt", mode="r") as file:  # create a file since we don't have it
    # delimiter is how you want to separate items in a list, in this case space
    file_reader = csv.reader(file, delimiter=" ")
    for row in file_reader:
        print(row[0])
        # print(row) to get it as lists

# next example

cats = ["cats are nice", " but dogs are better"]
