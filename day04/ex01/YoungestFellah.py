def youngestFellah(data, year):
    f = data['Age'][(data['Sex'] == 'F') & (data['Year'] == year)].min()
    m = data['Age'][(data['Sex'] == 'M') & (data['Year'] == year)].min()
    dic = {'f': f, 'm': m}
    print(dic)
    return dic
