from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData
loader = FileLoader()

data = loader.load("./athlete_events.csv")
sp = SpatioTemporalData(data)

sp.where(1896)
sp.where(2016)
sp.when('Athina')
sp.when('Paris')
