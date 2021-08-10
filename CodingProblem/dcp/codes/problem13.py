import string as alphabet

def substringWithKDistinctCharacters(string, k):
    """
    Returns the substring with k distinct characters
    args:
        string -> str
        k -> int
    """
    # store the maximum length of the substring 
    length = 0

    # holds the length of the boundaries
    longeststart = 0
    longestend = 0

    # holds the pointer (window sliders)
    start = 0
    end = 0

    # data structure to distinct characters
    windowslider = set()

    # stores the times the character appeared in the string
    lowercase = alphabet.ascii_lowercase
    frequency = {}
    for letter in lowercase:
        frequency[letter] = 0

    while len(string) > end:
        # adding the number to the set
        windowslider.add(string[end])
        # iterating the counter of the value
        frequency[string[end]] = frequency.get(string[end], 0) + 1

        # if pointer exceeds k characters, move to left
        while len(windowslider) > k:
            # iterating the counter of the value
            frequency[string[start]] = frequency.get(string[start], 0) - 1
            # removing the character from dictionary if its zero
            if frequency[string[start]] == 0:
                windowslider.remove(string[start])
            # reduce the window slider (move to left)
            start += 1
        # calculate the maximum length
        length = max(length, end - start + 1)
        # updating the boundaries
        if length > longestend - longeststart + 1:
            longestend = end
            longeststart = start
        # increase the windowslider
        end += 1
    return string[longeststart: longestend + 1]



if __name__ == "__main__":
    string = "abcbbbabbcbbadd"
    k = 2
    print(substringWithKDistinctCharacters(string, k))
