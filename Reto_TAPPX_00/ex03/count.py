import sys
import string

def text_analyzer(arr = None):
    """\n    This function counts the number of upper characters, 
    lower characters, punctuation and spaces in a given text."""
    if (arr == None):
        arr = input("What is the text to analyze?\n>> ")
    if (isinstance(arr, str) == False):
        print("AssertionError: argument is not a string")
        return
    n_spaces = 0
    n_upcase = 0
    n_lowcase = 0
    n_pmarks = 0
    for i in arr:
        if (i == ' '):
            n_spaces += 1
        elif (i.islower()):
            n_lowcase += 1
        elif (i.isupper()):
            n_upcase += 1
        elif (i in string.punctuation):
            n_pmarks += 1

    print("The text contains %i character(s):" % len(arr))
    print("- %i upper letter(s)" % n_upcase)
    print("- %i lower letter(s)" % n_lowcase)
    print("- %i punctuation mark(s)" % n_pmarks)
    print("- %i space(s)" % n_spaces)

if (__name__ == '__main__'):
    if (len(sys.argv) > 2):
        print("Too many arguments")
        exit(0)
    arr = None
    if (len(sys.argv) > 1):
        arr = sys.argv[1]
    text_analyzer(arr)
    exit(0)
