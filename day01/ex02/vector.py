def error(x):
    raise ValueError(x)


class Vector:
    def __init__(self, values, size=0):
        if isinstance(values, list):
            self.values = values
            self.size = len(values)
        if isinstance(values, int):
            aux = []
            while(size < values):
                aux.append(float(size))
                size += 1
            self.size = size + 1
            self.values = aux
        if isinstance(values, tuple):
            i = int(values[0])
            aux = []
            while(i < values[1]):
                aux.append(float(i))
                i += 1
            self.size = i + 1
            self.values = aux

    def __add__(self, add):
        i = 0
        aux = []
        while (i < len(self.values)):
            final = self.values[i] + add
            aux.append(final)
            i += 1
        return aux

    def __radd__(self, add):
        i = len(self.values) - 1
        aux = []
        while (i >= 0):
            final = self.values[i] + add
            aux.append(final)
            i -= 1
        return aux

    def __sub__(self, add):
        i = 0
        aux = []
        while (i < len(self.values)):
            final = self.values[i] - add
            aux.append(final)
            i += 1
        return aux

    def __rsub__(self, add):
        i = len(self.values) - 1
        aux = []
        while (i >= 0):
            final = self.values[i] - add
            aux.append(final)
            i -= 1
        return aux

    def __truediv__(self, add):
        i = 0
        aux = []
        while (i < len(self.values)):
            final = self.values[i] / add
            aux.append(final)
            i += 1
        return aux

    def __rtruediv__(self, add):
        i = len(self.values) - 1
        aux = []
        while (i >= 0):
            final = self.values[i] / add
            aux.append(final)
            i -= 1
        return aux

    def __mul__(self, add):
        i = 0
        aux = []
        while (i < len(self.values)):
            final = self.values[i] * add
            aux.append(final)
            i += 1
        return aux

    def __rmul__(self, add):
        i = len(self.values) - 1
        aux = []
        while (i >= 0):
            final = self.values[i] * add
            aux.append(final)
            i -= 1
        return aux

    def __str__(self):
        return """A vector calculator"""

    def __repr__(self, obj):
        final = "\tobj_type: " + str(type(obj))
        final += "\n\t\t\tobj_name: " + __name__
        final += "\n\t\t\tobj_address: " + str(hex(id(obj)))
        return final

    def __name__(self):
        return(str(self))
