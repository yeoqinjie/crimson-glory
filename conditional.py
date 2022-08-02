# a = 10
# b = 10
# if a >= 0:
#     a -= 5
# else:
#     print(f"{a} is a negative number")
#
#     print(a)
# c = 10
# d = 10
#
# if c > d:
#     print("c is bigger than d")
# elif c < d:
#     print("c is smaller than d")
# else:
#     print("c is same as d")

today = 'Tuesday'
#
# if today == 'Monday':
#     print('Today no class')
# elif today == 'Tuesday':
#     print('Today has App Dev class')
# elif today == 'Wednesday':
#     print('Today no class')
# elif today == 'Thursday':
#     print('Today no class')
# elif today == 'Friday':
#     print('Today no class')
# elif today == 'Saturday':
#     print('Today no class')
# else:
#     print('Today no class')

u = 'tuesday'
sunny = False
w = True
x = 5.06
y = 10.12
z = -5

# if today == u and x < y:  # and / or
#     print('both statements are true')
# else:
#     print('both or one of the statements is False')

if x < y or y < z:
    print('one or both statements are true')
else:
    print('both statements are false')

if 5 <= y <= 15:
    print('y is between 5 and 15')

if x * 2 == y - 1:
    print('they have the same value')

# Shorthand for if else statements
print('i will go to the beach') if sunny else print('i will stay at home')
