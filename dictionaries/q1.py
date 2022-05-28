from xml.etree.ElementTree import tostring


prices = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2
}
for key in prices:
    print(key)
    print("price: %s" % prices[key])
    print("stock: %s" % quantity[key])

total = 0
for key in prices:
    value = prices[key] * quantity[key]
    print(value)
    total = total + value
print(total)


# I have to modify this
