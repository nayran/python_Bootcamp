def howManyMedals(data, name):
    dic = {}
    sel = data[data['Name'] == name][['Year', 'Medal']]
    for year in sel['Year'].drop_duplicates():
        gold = sel['Medal'][(sel['Medal'] == 'Gold') & (sel['Year'] == year)]
        silv = sel['Medal'][(sel['Medal'] == 'Silver') & (sel['Year'] == year)]
        bron = sel['Medal'][(sel['Medal'] == 'Bronze') & (sel['Year'] == year)]
        dic[year] = {'G': gold.count(),
                     'S': silv.count(),
                     'B': bron.count()}
    print(dic)
    return dic
