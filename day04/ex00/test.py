from FileLoader import FileLoader
loader = FileLoader()

data = loader.load("./adult_data.csv")
loader.display(data, 12)
