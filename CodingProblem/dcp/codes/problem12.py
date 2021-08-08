def getstaircount(numberofstairs, stepsize):
    # base case:
    # checking if the number of stairs is
    # one or less than one
    if numberofstairs < 0:
        return 0
    if numberofstairs == 0:
        # only takes one step to
        # reach one stair
        return 1
    elif numberofstairs in stepsize:
        # if we only need to take numberofstairs is X steps
        # f(n) = f(n-stepsize[0]) + f(n-stepsize[1]) ... + f(n-stepsize[N])
        return 1 + sum(getstaircount(numberofstairs - stepstaken, stepsize) for
                   stepstaken in stepsize if stepstaken < numberofstairs)
    else:
        return sum(getstaircount(numberofstairs - stepstaken, stepsize) for
                   stepstaken in stepsize if stepstaken < numberofstairs)

assert getstaircount(4,[1,2]) == 5
