def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
def percentage(x, y):
    return (x / y) * 100