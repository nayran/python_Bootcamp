import sys

i = 1
args = []
aux = str


def onearg(arg):
    arg = arg.swapcase()
    arg = arg[::-1]
    print(arg)


def moreargs(args):
    x = 0
    aux = args[x]
    x += 1
    while (len(args) > x):
        aux = aux + " " + args[x]
        x += 1
    aux = aux.swapcase()
    aux = aux[::-1]
    print(aux)


if (len(sys.argv) == 2):
    onearg(sys.argv[i])
elif (len(sys.argv) > 2):
    while(i < len(sys.argv)):
        args.append(sys.argv[i])
        i += 1
    moreargs(args)
