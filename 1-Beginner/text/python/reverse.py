'''
Enter a string and the program will reverse it and print it out.
'''


def reverse(n):
    return n[::-1]



try:
    print(reverse(str(input("Enter Word\n"))))
except ValueError:
    print("Shame \n")
