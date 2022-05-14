# Q1

# input_number = input("enter a number: ")
# completed_list = []
# print(input_number)
# print(completed_list)

# while input_number != "":
#     completed_list.append(int(input_number))
#     input_number = input("Enter a number: ")

# print(completed_list)

# Q1 take two~
# number = "not nothing"
# list = []
# while number != "":
#     number = input("Enter a number: ")
#     list.append(number)
# list.pop()
# # List comprehension - recreating the list with int instead of str
# list = [int(i) for i in list]
# print(sum(list))

# Q2

# maximum = int(input(" Please Enter the Maximum Value : "))

# number = 0

# while number <= maximum:
#     if(number % 2 != 0):
#         print("{0}".format(number))
#     number = number + 1

# Q3

# i = 25
# num = int(input("Enter a number: "))

# while num != i:
#     num = int(input("Enter a number: "))
#     if num < i:
#         print("Too low!")
#     elif num > i:
#         print("Too high!")
#     elif num == i:
#         print("Correct!")
