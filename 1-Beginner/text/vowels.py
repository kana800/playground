'''
Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.
'''

def vowels(n):
    v = ["a","e","i","o","u"]
    summer = 0
    store_letters = []
    for i in n:
        if i in v:
            store_letters.append((i,n.count(i)))
            summer += 1
    return summer,sorted(list(set(store_letters)))




print(vowels("aeiouaaa"))
