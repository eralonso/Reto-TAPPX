import sys

def letter_to_morse(letter):
    dict_morse = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "CH": "----",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "Ñ": "--.--",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            " ": "/"
    }
    if (letter in dict_morse):
        return (dict_morse[letter])
    else:
        return ("")

def sos(text):
    to_translate = ""
    for word in text:
        to_translate += word + " "
    to_translate = to_translate.upper()[0:-1]
    translate = ""
    for c in to_translate:
        char = letter_to_morse(c)
        if (char == ""):
            print("ERROR")
            return
        translate += char + " "
    print(translate)

if (__name__ == "__main__"):
    argv = sys.argv
    argv.pop(0)
    if (len(argv) == 0):
        print("AssertionError: too few arguments")
    else:
        sos(argv)
    exit(0)
