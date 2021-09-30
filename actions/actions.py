def add(*args):
    """
    Return the sum of all arguments
    """
    return sum([arg for arg in args])

def sub(*args):
    """Return all arguments subtracted from each other"""
    return args[0] + sum([-arg for arg in args[1:]])
