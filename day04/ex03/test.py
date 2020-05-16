from FileLoader import FileLoader
from HowManyMedals import howManyMedals
loader = FileLoader()

data = loader.load("./athlete_events.csv")
howManyMedals(data, 'Kjetil Andr Aamodt')
