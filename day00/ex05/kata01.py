languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }
i = 0
lang = [*languages]
while (i < len(languages)):
    model = '{} was created by {}'.format(lang[i], languages[lang[i]])
    print(model)
    i += 1
