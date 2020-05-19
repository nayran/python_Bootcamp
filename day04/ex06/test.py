from FileLoader import FileLoader
from MyPlotLib import MyPlotLib as mpl
loader = FileLoader()

data = loader.load("./athlete_events.csv")
x = ["Height", "Weight"]
y = ["Weight", "Height"]
mpl.histogram(data, x)
mpl.density(data, y)
mpl.pair_plot(data, y)
mpl.box_plot(data, y)
