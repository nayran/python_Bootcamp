def proportionBySport(data, year, sport, gender):
    year_s = data['Year'] == year
    sport_s = data['Sport'] == sport
    gender_s = data['Sex'] == gender
    one_s = data[year_s & sport_s & gender_s]
    one_s = len(one_s.drop_duplicates('Name', keep='first'))
    all_s = data[year_s & gender_s]
    all_s = len(all_s.drop_duplicates('Name', keep='first'))
    print(one_s/all_s)
    return one_s/all_s
