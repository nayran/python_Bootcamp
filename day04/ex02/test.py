from FileLoader import FileLoader
from ProportionBySport import proportionBySport
loader = FileLoader()

data = loader.load("./athlete_events.csv")
proportionBySport(data, 2004, 'Tennis', 'F')
