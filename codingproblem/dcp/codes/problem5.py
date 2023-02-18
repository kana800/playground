"""
Problem #5
"""

# cons implementation
def cons(a,b):
    return lambda f: f(a,b)


def car(func):
    f1 = lambda a,b :a
    return func(f1)

def cdr(func):
    f2 = lambda a,b:b
    return func(f2)


if __name__ == "__main__":
    assert car(cons(3,4)) == 3
    assert cdr(cons(3,4)) == 4
