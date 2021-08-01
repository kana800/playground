"""
Number of possibilites of the decoded string
"""

def decodedPermutations(message):
    """
    returns the number of possible
    decoded message
    """
    # checking if the message arr is empty
    if len(message) == 0:
        return 1

    # stores the count 
    count = 0

    for letter in range(1, 27):
        if message.startswith(str(letter)):
            count += decodedPermutations(message[len(str(letter)):])
    return count
