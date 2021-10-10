import sys

def mortgage_payment(principal,r,N):
    r = (r * 0.01) / 12
    N = N * 12
    fraction = (r*((1+r)**N))/(((1+r)**N)-1)
    return principal * fraction


if __name__ == "__main__":
    print(mortgage_payment(100000,6.5,30))
