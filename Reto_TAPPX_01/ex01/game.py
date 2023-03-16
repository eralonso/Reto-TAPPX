class GotCharacter:
    def __init__(self, first_name = None, is_alive = True):
        self._first_name = first_name
        self._is_alive = is_alive

    @property
    def first_name(self):
        return (self._first_name)

    @first_name.setter
    def first_name(self, first_name):
        if (isinstance(first_name, str) == False):
            print("AsssertionError: Class: \'GotCharacter\', Property: \'first_name\', Error: must be a str")
        self._first_name = first_name

    @property
    def is_alive(self):
        return (self._is_alive)

    @is_alive.setter
    def is_alive(self, is_alive):
        if (isinstance(is_alive, bool) == False):
            print("AsssertionError: Class: \'GotCharacter\', Property: \'is_alive\', Error: must be a bool")
            exit(1)
        else:
            self._is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people.""" 
    def __init__(self, first_name = None, is_alive = True):
        super().__init__(first_name, is_alive)
        self._family_name = "Stark"
        self._house_words = "Winter is coming"

    @property
    def family_name(self):
        return (self._family_name)

    @family_name.setter
    def family_name(self, family_name):
        if (isinstance(family_name, str) == False):
            print("AsssertionError: Class: \'Stark\', Property: \'family_name\', Error: must be a str")
        else:
            self._family_name = family_name
    
    @property
    def house_words(self):
        return (self._house_words)

    @house_words.setter
    def house_words(self, house_words):
        if (isinstance(house_words, str) == False):
            print("AsssertionError: Class: \'Stark\', Property: \'house_words\', Error: must be a str")
        else:
            self._house_words = house_words
    
    def print_house_words(self):
        print(self.house_words)

    def die(self):
        if (self.is_alive == False):
            print(f"{self.first_name} is already dead")
        else:
            self.is_alive = False
            print(f"You kill {self.first_name}")

    def resurrect(self):
        if (self.is_alive == True):
            print(f"{self.first_name} is already live")
        else:
            self.is_alive = True 
            print(f"You resurerct {self.first_name}")

