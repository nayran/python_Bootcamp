x = (0, 4, 132.42222, 10000, 12345.67)

model = 'day_{:02d}, ex_{:02d} : {:.2f}, '.format(x[0], x[1], x[2])
model2 = '{:.2e}, {:.2e}'.format(x[3], x[4])
print(model + model2)
