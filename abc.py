list = [1, 2, 3]

for v1 in list:
    v1 += 5  # v1 = v1 + 5
    v1 *= 2.4
    print(v1)

# items in the list/dict
apple = {"color": "red", "qty": 20, "cost": 2.45}
orange = {"color": "orange", "qty": 10, "cost": 3.90, 'sweetness': 10}

for i, j in apple.items():
    print(f'{i} is {j}')

# number of times
for n in range(6):
    print(n)

# rows = [1, 2, 3]
# columns = [1, 2, 3]
# depth = [1, 2, 3, 4]
#
# for r in rows:
#     for c in columns:
#         for d in depth:
#             print(f'r:{r}, c:{c}, d:{d}')

a = int(input("Please enter a number: "))

while a % 3 == 0:
    print(a / 3)
    a = int(input("Please enter another number: "))



