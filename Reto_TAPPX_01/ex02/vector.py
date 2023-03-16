class Vector:

    def __init__(self, vect):
        values = list()
        if (isinstance(vect, list) == True):
            y = 0
            x = 0
            if (len(vect) == 0):
                print("AssertionError: Vector is void")
                exit(1)
            y = len(vect)
            if (y == 1):
                for n in vect[0]:
                    if (isinstance(n, float) == False):
                        print("AssertionError: Only floats")
                        exit(1)
                    x += 1
            else:
                i = 0
                while i < y:
                    if (isinstance(vect[i][0], float) == False):
                        print("AssertionError: Only floats")
                        exit(1)
                    i += 1
                x = 1
            if (len(vect) > 1 and len(vect[0]) > 1):
                print("AssertionError: Incorrect size of Vector")
                exit(1)
            shape = (y, x)
            values = vect
        elif (isinstance(vect, int) == True or isinstance(vect, tuple) == True):
            if (isinstance(vect, tuple) == True and len(vect) != 2):
                print("AssertionError: Invalid number of arguments: Vector((start, end))")
                exit(1)
            elif (isinstance(vect, tuple) == True):
                start = vect[0]
                end = vect[1]
            else:
                if (vect <= 0):
                    print("AssertionError: Size of vector must be greater than 0")
                    exit(1)
                start = 0
                end = vect
            if (start > end):
                print("AssertionError: The start value must be lower than end")
                exit(1)
            for num in range(start, end):
                values.append([float(num)])
        else:
            print("AssertionError: Invalid type of argument")
            exit(1)
        self.values = values
        self.shape = shape

    def dot(self, num):
        if (isinstance(num, Vector) == False):
            print("AssertionError: Argument is not a Vector")
            exit(1)
        if (self.shape != num.shape):
            print("AssertionError: Not have the same shape")
        shape = self.shape
        i = 0;
        res = 0
        if (shape[0] == 1):
            while (i < shape[1]):
                res += self.values[0][i] * num.values[0][i]
                i += 1
        else:
            while (i < shape[0]):
                res += self.values[i][0] * num.values[i][0]
                i += 1
        return (res)


    def T(self):
        vect = []
        if (self.shape[0] == 1):
            for elem in self.values[0]:
                vect.append([elem])

        else:
            total = []
            for elem in self.values:
                total.append(float(elem[0]))
            vect = [total]
        new_vect = Vector(vect)
        return (new_vect)
