# # Q1

# def temperature_calculator(f):
#     calculator = (f - 32) * 5/9
#     return calculator


# print(temperature_calculator(32))


# Q2

# def odd_or_even(number):

#     if (number % 2) == 0:
#         print("False")
#     else:
#         print("True")
#     return


# print(odd_or_even(3))


# Q3

# def mean_of_list(n1, n2, n3, n4):
#     mean = (n1+n2+n3+n4)/4
#     return mean


# print(mean_of_list(4, 3, 2, 6))


# Q4

def cost_calculator(price_per_unit, num_units):
    total = price_per_unit * num_units
    return (f"{total},$")


print(cost_calculator(4.25, 3))
