def howManyMedalsByCountry(data, name):
    dic = {}
    sel = data[data['Team'] == name][['Year', 'Event', 'Medal']]
    for year in sel['Year'].drop_duplicates().sort_values():
        gold = sel[['Medal',
                    'Event']][(sel['Medal'] == 'Gold')
                              & (sel['Year'] == year)].drop_duplicates(
                                      subset='Event')['Medal']
        silv = sel[['Medal',
                    'Event']][(sel['Medal'] == 'Silver')
                              & (sel['Year'] == year)].drop_duplicates(
                                      subset='Event')['Medal']
        bron = sel[['Medal',
                    'Event']][(sel['Medal'] == 'Bronze')
                              & (sel['Year'] == year)].drop_duplicates(
                                      subset='Event')['Medal']
        dic[year] = {'G': gold.count(),
                     'S': silv.count(),
                     'B': bron.count()}
    print(dic)
    return dic
