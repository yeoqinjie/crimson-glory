# list


# list are ordered
# li1 = [1, 2, 3]
# li2 = [1, 2, 3]
# dictionary
# properties about a car
# di = {"wheels": 4, "doors": 2, "color": "black", "brand": "honda"}

# tuple
# tu = ("hello", True, 3, [1, ["a", "b"], 3])
# print(tu[0])

# loops
# li = ["hello", True, 3, [1, ["a", "b"], 3]]
# li2 = [1, 2, 3, 4, 5]
# t = 0
# for i in li2:
#     t += i  # t = t + i
#
# di = {"wheels": 4, "doors": 2, "color": "black", "brand": "honda"}
#
# # ("wheels", 4), ("doors", 2)
# for a, b in di.items():
#     print(a, b)

# for i in range(10):
#     i = i ** 2
#
#
# rows = 5
# cols = 7
# z = 9
#
# count = 0
#
# for r in range(rows):
#     for c in range(cols):
#         for z1 in range(z):
#             count += 1
#
# print(count)

# a = 934
# while a < 0:
#     print(a)
#     a -= 57

# Condition

a = True
b = False

# v1 = int(input("type number 1: "))
# v2 = int(input("type number 2: "))

# if v1 == v2:
#     print("v1 and v2 is equal")
# elif v1 < v2:
#     print("v1 is smaller")
# else:
#     print("v2 is smaller")

is_raining = True
is_weekday = True
is_happy = True

clothes = 0

if is_raining and is_weekday and is_happy:
    clothes = 1
elif not is_raining and is_weekday or is_happy:
    clothes = 2
elif is_raining or is_weekday and not is_happy:
    clothes = 3

print(clothes)
