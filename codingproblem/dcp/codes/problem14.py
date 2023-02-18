import random

def piMonteCarlo(numberofsamples, radius):
    """
    Returns the pi value to 3 decimal places
    using montecarlomethod
    """
    numberofpointsincircle = 0
    r = radius
    for n in range(0, numberofsamples):
        # selecting a random number of x^2
        # and y^2
        x = random.uniform(-1,1) * radius
        y = random.uniform(-1,1) * radius
        print(x,y)
        if (x**2) + (y**2) < (r**2):
            numberofpointsincircle += 1

    return round(4 * numberofpointsincircle/numberofsamples,3)

print(piMonteCarlo(1000000,2))
