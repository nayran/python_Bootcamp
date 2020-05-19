from FileLoader import FileLoader
from HowManyMedalsByCountry import howManyMedalsByCountry
loader = FileLoader()

data = loader.load("./athlete_events.csv")
print('Brazilian data:')
howManyMedalsByCountry(data, 'Brazil')
