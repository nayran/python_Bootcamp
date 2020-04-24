from datetime import datetime


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    i = 0
    j = 0
    aux = []
    if (option != "ordered" and option != "shuffle" and option != "unique" and
            option is not None or text is None):
        return 'ERROR'
    while(i < len(text)):
        if(text[i] == sep or i + 1 == len(text)):
            for r in range(j, i + 1):
                if(r == j):
                    aux2 = text[r]
                else:
                    aux2 += text[r]
            aux.append(aux2)
            j = i + 1
        i += 1
    if(option is None):
        return(aux)
    elif(option == "ordered"):
        final = ordered(aux)
    elif(option == "unique"):
        final = unique(aux)
    elif(option == "shuffle"):
        final = shuffle(aux)
    for i in final:
        yield i


def shuffle(aux):
    final = []
    for i in aux:
        x = datetime.now().microsecond
        x = x % len(aux)
        final.insert(x, i)
    return final


def unique(aux):
    final = []
    for i in aux:
        if i not in final:
            final.append(i)
    return final


def ordered(aux):
    aux.sort(key=str.lower)
    return aux
