import sys
import string


i = -1
k = -1
j = 0
n = 0
aux = []
if (len(sys.argv) != 3):
    print("ERROR")
elif sys.argv[1].isdigit() is True or sys.argv[2].isalpha() is True:
    print("ERROR")
else:
    x = int(sys.argv[2])
    eol = len(sys.argv[1])
    while (i < eol):
        i += 1
        k += 1
        if (i == eol or string.punctuation == sys.argv[1][i]
                or sys.argv[1][i] == ' '):
            if (n > x):
                aux.append(sys.argv[1][j:k])
            j = k + 1
            n = 0
        else:
            n += 1
    print(aux)
