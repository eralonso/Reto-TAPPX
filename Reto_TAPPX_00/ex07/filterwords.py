import sys
import string

def isinteger(num):
    if (num[0] == '+' or num[0] == '-'):
        return num[1::].isdigit()
    else:
        return num.isdigit()

def filter_words(text, n):
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = [word for word in text.split(' ') if len(word) > n]
    print(words)

if (__name__ == "__main__"):
    argv = sys.argv
    argv.pop(0)
    if (len(argv) < 2):
        print("AssertionError: too few arguments")
    elif (len(argv) > 2):
        print("AssertionError: too many arguments")
    else:
        if (isinteger(argv[0]) == False and isinteger(argv[1]) == True):
            filter_words(argv[0], int(argv[1]))
        else:
            print("AssertionError: Invalid arguments")
    exit(0)
