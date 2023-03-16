class CsvReader:
    
    def __init__(self, filename = None, sep=',', header = False, skip_top = 0, skip_bottom = -1):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
    
    def __enter__(self):
        try:
            self.fd = open(self.filename, 'r')
            self.file = self.fd.readlines()
            col = len(self.file[0])
            for i in range(0, len(self.file)):

                self.file[i] = self.file[i].split(',')
                for j in range(0, len(self.file[i])):
                    self.file[i][j] = self.file[i][j].replace("\"", "")
                else:
                    if (j != col):
                        return (None)

            self.g_header = self.file[0]
            if (self.header == False):
                self.file.pop(0)
            self.file = self.file[self.skip_top:self.skip_bottom]
            self.data = self.file
            return (self)
        except FileNotFoundError:
            self.fd = None
            return (self)

    def __exit__(self, *args):
        self.fd.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom. Return:
        """
        return (self.data)

    def getheader(self):
        """ Retrieves the header from csv file. Returns:
        list: representing the data (when self.header is True). None: (when self.header is False).
        """
        return (self.g_header)

if (__name__ == "__main__"):
    archivo = input("Introduzca el nombre del archivo:\n>> ")
    with CsvReader(archivo, ',', False, 0, 2) as var:
        if (var == None):
            print ("Files is corrupted")
            exit(1)
        print("var.getdata(): ", var.getdata())
        print("var.getheader(): ", var.getheader())
