import sys

i = 1
k = 0
aux = []
final = []
trans = {
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
        "F": "..-. ", "N": "-. ", "O": "--- ", "P": ".--. ", "Q": "--.- ",
        "R": ".-. ", "S": "... ", "G": "--. ", "T": "- ", "H": ".... ",
        "U": "..- ", "I": ".. ", "V": "...- ", "J": ".--- ", "W": ".-- ",
        "K": "-.- ", "X": "-..- ", "L": ".-.. ", "Y": "-.-- ", "M": "-- ",
        "Z": "--.. ", " ": "/ ", "1": "·---- ", "2": "··--- ", "3": "···-- ",
        "4": "····- ", "5": "····· ", "6": "-···· ", "7": "--··· ",
        "8": "---·· ", "9": "----· ", "0": "----- ",
}
while (i < len(sys.argv)):
    test = 1
    while (k < len(sys.argv[i])):
        if sys.argv[i][k].isalnum() is False and sys.argv[i][k] != ' ':
            print("ERROR")
            test = 0
        k += 1
    if (test == 1):
        x = sys.argv[i].upper()
        if(i + 1 != len(sys.argv)):
            aux.append(x + ' ')
        else:
            aux.append(x)
    i += 1
i = 0
k = 0
while(i < len(aux)):
    while (k < len(aux[i])):
        final.append(trans[aux[i][k]])
        k += 1
    i += 1
    k = 0
i = 0
for i in range(0, len(final)):
    sys.stdout.write('{}'.format(final[i]))
