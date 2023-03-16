import random

def generator(text, sep = " ", option = None):
    text = text.split(sep)
    if (option == "shuffle"):
        final_text = list()
        used_num = list()
        for i in range(0, len(text)):
            num = random.randint(0, len(text) - 1)
            while (used_num.count(num) != 0):
                num = random.randint(0, len(text) - 1)
            used_num.append(num)
            final_text.append(text[num])
        text = final_text
    elif (option == "unique"):
        final_text = list()
        for word in text:
            if (final_text.count(word) == 0):
                final_text.append(word)
        text = final_text
    elif (option == "ordered"):
        text.sort()
    return (text)
