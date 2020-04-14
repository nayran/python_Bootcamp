import string


def text_analyzer(text=None):
    ''' This is a random text. Input something next time '''
    chara = 0
    upper = 0
    lower = 0
    space = 0
    punct = 0
    if text is None:
        text = input("Write something: ")
    print("\n" + text)
    while (chara < len(text)):
        i = 0
        if (text[chara].isupper()):
            upper += 1
        elif (text[chara].islower()):
            lower += 1
        if (text[chara] == ' '):
            space += 1
        while (i < len(string.punctuation)):
            if (text[chara] == string.punctuation[i]):
                punct += 1
            i += 1
        chara += 1
    print("\nThe text contains %d characters" % chara)
    print("%d upper letters" % upper)
    print("%d lower letters" % lower)
    print("%d punctuation marks" % punct)
    print("%d spaces" % space)
