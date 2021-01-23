import math
import exchange


def _func():
    a = input("Please enter a number: ")
    b = math.sqrt(a)
    print(b)


# for i in range(4):
#     _func()

a = 2.1
# print("this costs ${:.2f}".format(a))


print(exchange.ExchangeRate.sgd_to_usd(a))


