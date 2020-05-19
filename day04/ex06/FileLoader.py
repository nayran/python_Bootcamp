import pandas


class FileLoader:
    @staticmethod
    def load(path):
        df = pandas.read_csv(path)
        print(f'Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}')
        return df

    @staticmethod
    def display(df, n):
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(-n))
