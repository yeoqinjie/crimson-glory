class Calculator:
    val_a = ''
    val_b = ''

    def __init__(self, a, b):
        self.val_a = a
        self.val_b = b

    def add(self):
        return self.val_a + self.val_b

    def minus(self):
        return self.val_a - self.val_b

    @classmethod
    def add_two(cls, a, b):
        print(f'{a} + {b}')
        return a + b
