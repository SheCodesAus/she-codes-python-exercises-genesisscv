# Part A

# n1 = (input("Enter a number:"))
# n2 = (input("Enter a number:"))
# n3 = (input("Enter a number:"))

# n1_n2_n3 = str(n1 + n2 + n3)

# list = [n1, n2, n3]

# sum_of_nrs = int(n1) + int(n2) + int(n3)
# print(list)
# # print(n1_n2_n3)
# # print(sum_of_nrs)

# Part B
number = "not nothing"
list = []
while number != "":
    number = input("Enter a number: ")
    list.append(number)
list.pop()
# List comprehension - recreating the list with str
list = [int(i) for i in list]
# Converting list to str using list comprehension
numbers = ''.join([str(item) for item in list])
print(numbers)
print(sum(list))
print(list)
