from csvreader import CsvReader

# x = CsvReader('good.csv', header=True).getheader()
# print(x)
# x = CsvReader('good.csv', header=True, skip_bottom=3, skip_top=2).getdata()
# print(x)
# x = CsvReader('good.csv').getdata()
# print(x)

if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")

if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
print("header:\n" + header)
print('data:\n' + data)
