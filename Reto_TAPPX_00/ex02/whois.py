import sys

def select_answer(num):
    if (num == 0):
        print("I'm Zero")
    elif (num % 2 == 0):
        print("I'm Even")
    else:
        print("I'm Odd")

def isinteger(num):
    if (num[0] == '+' or num[0] == '-'):
        return num[1::].isdigit()
    else:
        return num.isdigit()

def whois(argv):
    if (len(argv) < 2):
        print("Usage: python3 whois.py <Integer>")
    else:
        if (isinteger(argv[1]) == False):
            print("AssertionError: argument is not an integer")
        elif (len(argv) != 2):
            print("AssertionError: more than one argument are provided")
        else:
            select_answer(int(argv[1]))

whois(sys.argv)
exit(0)
