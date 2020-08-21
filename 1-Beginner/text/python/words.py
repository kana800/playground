'''
Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.
'''



def words(n):
    print(n.split())
    return len(n.split())


print(words("Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary."))
