class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            return (-1)
        res = 0
        for elem in zip(coefs, words):
            if (isinstance(elem[0], str) == True):
                res += len(elem[0]) *elem[1]
            else:
                res += len(elem[1]) *elem[0]
        return (res) 
    
    @staticmethod
    def enumerate_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            return (-1)
        if (isinstance(coefs[0], str) == True):
            tmp = words
            words = coefs
            coefs = tmp
        res = 0
        for elem in enumerate(words, 0):
            res += len(elem[1]) * coefs[elem[0]]
        return (res) 

