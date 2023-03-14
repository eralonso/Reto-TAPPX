import sys

def isinteger(num):
    if (num[0] == '+' or num[0] == '-'):
        return num[1::].isdigit()
    else:
        return num.isdigit()

def operations(num1, num2):
    res_sum = num1 + num2
    print("Sum: %i" % res_sum)
    res_dif = num1 - num2
    print("Difference: %i" % res_dif)
    res_prod = num1 * num2
    print("Product: %i" % res_prod)
    if (num2 == 0):
        print("ERROR (division by zero)")
    else:
        res_quot = round(num1 / num2, 3)
        print("Quotient: %f" % res_quot)
    if (num2 == 0):
        print("ERROR (modulo by zero)")
    else:
        res_rem = num1 % num2
        print("Remainder: %i" % res_rem)

if (__name__ == '__main__'):
    argv = sys.argv
    if (len(argv) == 1):
        print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    elif (len(argv) < 3):
        print("AssertionError: too few arguments")
    elif (len(argv) > 3):
        print("AssertionError: too many arguments")
    elif (isinteger(argv[1]) == False or isinteger(argv[2]) == False):
        print("AssertionError: only integers")
    else:
        operations(float(argv[1]), float(argv[2]))
    exit(0)
