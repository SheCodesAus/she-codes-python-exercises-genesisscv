# Data Types - Str, Int, Float, Boolean
from pkg_resources import compatible_platforms


b1 = True
b2 = False
# print(type(b1))

knows_password = True
knows_username = False
login = knows_password and knows_username
# print(type(login))
# print(login)
# print(not knows_password)

# Booleran Operators - NOT, AND, OR
recover = knows_password or knows_username

# Thinkific

is_raining = True
is_cold = True

# print(type(is_raining))
# print(type(is_cold))

# print(not is_raining)
# print(is_raining and is_cold)
# print(is_raining and not is_cold)

# Comparison Operators
# ==Equal
# !=Not Equal
# >Greater than
# >Less than
# >= Greater than or equal
# <= Less than or equal

# print(10 > 5)
# print(1 > 1.5)

# print("asli" == "asli")

# if 5 > 4
# print("Hello")

name = "Asli"
if name == "Asli":
    print("Hello again")
elif name == "Camila":
    print(f"Hello{name}, how's it going?")
else:
    print("Hellooooo")
