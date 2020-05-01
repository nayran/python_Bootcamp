class CsvReader():
    def __init__(self, name, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = name
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.openfile = open(self.filename, "r")
        self.lines = self.openfile.readlines()
        self.skip_bottom = len(self.lines) - skip_bottom
        pass

    def __enter__(self):
        self.data = self.getdata()
        if self.data is None:
            return None
        return self

    def __exit__(self, type, value, traceback):
        self.openfile.close()

    def getdata(self):
        if self.header is True:
            header = self.getheader()
            aux = header
            self.skip_top += 1
        else:
            aux = ""
        self.args = self.args_num(self.lines[0])
        for i in self.lines[self.skip_top:self.skip_bottom]:
            if self.args != self.args_num(i):
                return None
            i = self.separator(i)
            aux += str(i)
        return aux

    def getheader(self):
        header = self.separator(self.lines[self.skip_top])
        aux = ""
        for i in header:
            aux += str(i)
        return aux

    def separator(self, line):
        if line is None:
            return None
        x = 0
        aux = ""
        j = 0
        while(line[x] != "\n"):
            if line[x + 1] == "\n":
                aux += line[j:x+2]
                j = x
            if line[x] is self.sep:
                aux += line[j:x]
                j = x + 1
            x += 1
        return aux

    def args_num(self, line):
        if line is None:
            return None
        x = 0
        self.args = 1
        while(line[x] != "\n"):
            if line[x] is self.sep:
                self.args += 1
            x += 1
        return self.args
