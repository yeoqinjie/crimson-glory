try:
    x = input('Enter a positive number: ')
    x = int(x)
    if x < 0:
        raise ValueError
    y = 10 / x
    print(y)
except TypeError:
    print('Please enter a number')
except ValueError:
    print('Please enter a positive number')
except ZeroDivisionError:
    print('Please enter a positive non-zero number')
