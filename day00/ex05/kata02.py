from datetime import datetime

time = (3, 30, 2019, 9, 25)
model = '{:%m/%d/%Y %H:%M}'
print(model.format(datetime(time[2], time[3], time[4], time[0], time[1])))
