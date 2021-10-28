def add(*args):
    """
    Return the sum of all arguments
    """
    return sum([arg for arg in args])


def sub(*args):
    """Return all arguments subtracted from each other"""
    return args[0] + sum([-arg for arg in args[1:]])


def power(a, b):
    """return a to the power of b"""
    return a ** b


def div(a, b):
    """returns a / b"""
    return a / b

def mul(a, b):
    """return a * b"""
    return a * b
